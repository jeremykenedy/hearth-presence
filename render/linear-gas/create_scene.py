import bpy, math, random
from mathutils import Vector
from pathlib import Path
ROOT=Path(__file__).resolve().parent
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=32
scene.cycles.use_denoising=True
scene.render.resolution_x=1920;scene.render.resolution_y=540;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.render.fps=30;scene.frame_start=1;scene.frame_end=180
scene.world.color=(.015,.015,.018)
scene.view_settings.view_transform='AgX'

def material(name,color,rough=.3,metal=0,transmission=0):
 m=bpy.data.materials.new(name);m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1)
 p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
 p.inputs['Transmission Weight'].default_value=transmission;p.inputs['IOR'].default_value=1.45
 return m
steel=material('Brushed black steel',(.018,.021,.024),.24,.8)
stone=material('Obsidian burner stones',(.024,.028,.032),.22,.24)
glass=material('Smoky crystal glass',(.18,.24,.27),.12,.04,.65)

def cube(name,location,scale,mat,bevel=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=location);o=bpy.context.object;o.name=name;o.dimensions=scale
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 if mat:o.data.materials.append(mat)
 if bevel:
  mod=o.modifiers.new('Soft machined edges','BEVEL');mod.width=bevel;mod.segments=3
  o.modifiers.new('Surface normals','WEIGHTED_NORMAL')
 return o
cube('Steel rear wall',(0,.25,.6),(4.8,.10,1.5),steel,.012)
cube('Polished hearth tray',(0,0,.025),(4.8,.8,.05),steel,.018)
cube('Burner front lip',(0,-.42,.065),(4.8,.045,.13),steel,.008)
random.seed(522)
for i in range(350):
 x=random.uniform(-2.15,2.15);y=random.uniform(-.3,.19)
 bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=random.uniform(.025,.055),location=(x,y,.075+random.random()*.025))
 o=bpy.context.object;o.name='Fire glass' if i%3 else 'Lava stone'
 o.scale=(random.uniform(.8,1.4),random.uniform(.7,1.3),random.uniform(.5,1.1));o.rotation_euler=(random.random()*3,random.random()*3,random.random()*3)
 o.data.materials.append(glass if i%3 else stone)

# Multiple small burner ports produce a clean line with individual flame tongues.
ports=[]
for i in range(25):
 bpy.ops.mesh.primitive_plane_add(size=1,location=(-2.0+i/24*4.0,0,.115))
 o=bpy.context.object;o.scale=(.095,.065,1);ports.append(o)
bpy.ops.object.select_all(action='DESELECT')
for o in ports:o.select_set(True)
bpy.context.view_layer.objects.active=ports[0];bpy.ops.object.join();flow=bpy.context.object
flow.name='Gas burner ports';bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
mod=flow.modifiers.new('Gas fuel inlet','FLUID');mod.fluid_type='FLOW';bpy.context.view_layer.update()
f=mod.flow_settings;f.flow_type='FIRE';f.flow_behavior='INFLOW';f.surface_distance=1.5
f.fuel_amount=1.0;f.temperature=1.5;f.use_plane_init=True
flow.hide_render=True

bpy.ops.mesh.primitive_cube_add(size=1,location=(0,0,.65))
domain=bpy.context.object;domain.name='Gas flame volume';domain.dimensions=(4.65,.65,1.2)
bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
mod=domain.modifiers.new('Fire simulation','FLUID');mod.fluid_type='DOMAIN';bpy.context.view_layer.update()
d=mod.domain_settings;d.domain_type='GAS';d.resolution_max=384
# Separate data and noise caches keep the physical simulation reproducible.
d.cache_type='MODULAR';d.cache_directory=str(ROOT/'cache-hq');d.cache_frame_start=1;d.cache_frame_end=180
d.cache_data_format='OPENVDB';d.use_noise=True;d.noise_scale=2
for name,value in [('burning_rate',1.1),('flame_smoke',.015),('flame_vorticity',.7),('vorticity',.6),('flame_ignition',1.5),('flame_max_temp',3.0)]:
 if hasattr(d,name):setattr(d,name,value)
volume=bpy.data.materials.new('Luminous clean gas fire');volume.use_nodes=True
n=volume.node_tree.nodes;n.clear();l=volume.node_tree.links
out=n.new('ShaderNodeOutputMaterial');v=n.new('ShaderNodeVolumePrincipled')
v.inputs['Density'].default_value=.03
flame=n.new('ShaderNodeAttribute');flame.attribute_name='flame'
strength=n.new('ShaderNodeMath');strength.operation='MULTIPLY';strength.inputs[1].default_value=5
l.new(flame.outputs['Fac'],strength.inputs[0]);l.new(strength.outputs[0],v.inputs['Emission Strength'])
heat=n.new('ShaderNodeAttribute');heat.attribute_name='temperature'
scale=n.new('ShaderNodeMath');scale.operation='MULTIPLY_ADD';scale.inputs[1].default_value=1100;scale.inputs[2].default_value=900
l.new(heat.outputs['Fac'],scale.inputs[0]);black=n.new('ShaderNodeBlackbody');l.new(scale.outputs[0],black.inputs[0]);l.new(black.outputs[0],v.inputs['Emission Color'])
l.new(v.outputs['Volume'],out.inputs['Volume']);domain.data.materials.append(volume)

for i in range(9):
 bpy.ops.object.light_add(type='POINT',location=(-1.8+i*.45,-.02,.2))
 lamp=bpy.context.object;lamp.name='Warm reflected burner light';lamp.data.color=(1,.23,.035);lamp.data.shadow_soft_size=.15
 for frame in range(1,181,4):
  lamp.data.energy=9+4*math.sin(frame*.45+i*2.5)+2*math.sin(frame*.9+i)
  lamp.data.keyframe_insert('energy',frame=frame)
bpy.ops.object.light_add(type='AREA',location=(0,-2,2.5));bpy.context.object.data.energy=110;bpy.context.object.data.shape='RECTANGLE';bpy.context.object.data.size=4
bpy.context.object.rotation_euler=(Vector((0,0,.1))-bpy.context.object.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(0,-6,1.35));camera=bpy.context.object
camera.rotation_euler=(Vector((0,0,.53))-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.type='ORTHO';camera.data.ortho_scale=4.65
scene.camera=camera
scene.render.filepath=str(ROOT/'proof.png')
bpy.context.view_layer.objects.active=domain;domain.select_set(True)
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'linear-gas.blend'))
print('BAKING FIRE DATA',flush=True);bpy.ops.fluid.bake_data();print('BAKING FIRE NOISE',flush=True);bpy.ops.fluid.bake_noise()
scene.frame_set(75);bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'linear-gas.blend'))
print('RENDERING PROOF',flush=True);bpy.ops.render.render(write_still=True)
