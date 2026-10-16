"""Build the original static burner bed with Blender 4.5 LTS. No fluid bake."""

import bpy, bmesh, math, random
from mathutils import Vector
from pathlib import Path

ROOT = Path(__file__).resolve().parent
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.eevee.taa_render_samples = 64
scene.eevee.use_raytracing = True
scene.render.resolution_x = 1920
scene.render.resolution_y = 540
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.fps = 30
scene.frame_start = 1
scene.frame_end = 180
scene.world.color = (0.015, 0.015, 0.018)
scene.view_settings.view_transform = "AgX"


def material(name, color, rough=0.3, metal=0, transmission=0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    p = m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value = (*color, 1)
    p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal
    p.inputs["Transmission Weight"].default_value = transmission
    p.inputs["IOR"].default_value = 1.45
    return m


steel = material("Brushed black steel", (0.018, 0.021, 0.024), 0.24, 0.8)


def cube(name, location, scale, mat, bevel=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    o = bpy.context.object
    o.name = name
    o.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat:
        o.data.materials.append(mat)
    if bevel:
        mod = o.modifiers.new("Soft machined edges", "BEVEL")
        mod.width = bevel
        mod.segments = 3
        o.modifiers.new("Surface normals", "WEIGHTED_NORMAL")
    return o


cube("Steel rear wall", (0, 0.25, 0.6), (4.8, 0.10, 1.5), steel, 0.012)
cube("Polished hearth tray", (0, 0, 0.025), (4.8, 0.8, 0.05), steel, 0.018)
cube("Burner front lip", (0, -0.42, 0.065), (4.8, 0.045, 0.13), steel, 0.008)
# Shared beveled glass and smooth stone meshes keep the small bed detailed.
glass = material("Clear smoky fireglass", (0.12, 0.16, 0.19), 0.08, 0.02, 0.92)
black = material("Polished black fireglass", (0.008, 0.012, 0.014), 0.10, 0.3, 0.12)
stone = material("Smooth small obsidian", (0.008, 0.01, 0.012), 0.22, 0.15)
meshes = []
for name, mat, kind in [
    ("Clear glass chips", glass, "glass"),
    ("Dark polished chips", black, "glass"),
    ("Smooth obsidian", stone, "stone"),
]:
    bm = bmesh.new()
    if kind == "glass":
        bmesh.ops.create_cube(bm, size=2)
        bmesh.ops.bevel(
            bm, geom=list(bm.edges), offset=0.15, segments=2, affect="EDGES"
        )
    else:
        bmesh.ops.create_icosphere(bm, subdivisions=3, radius=1)
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    mesh.materials.append(mat)
    if kind == "stone":
        for polygon in mesh.polygons:
            polygon.use_smooth = True
    meshes.append(mesh)
random.seed(522)
for i in range(2600):
    x = random.uniform(-2.19, 2.19)
    y = random.uniform(-0.31, 0.19)
    radius = random.uniform(0.008, 0.025)
    obj = bpy.data.objects.new(
        "Fireglass", meshes[2 if i % 7 == 0 else 1 if i % 3 == 0 else 0]
    )
    scene.collection.objects.link(obj)
    obj.location = (x, y, 0.065 + random.random() * 0.035)
    obj.scale = (
        radius * random.uniform(0.65, 1.4),
        radius * random.uniform(0.7, 1.2),
        radius * random.uniform(0.45, 1.1),
    )
    obj.rotation_euler = (random.random() * 3, random.random() * 3, random.random() * 3)
rear = bpy.data.objects["Steel rear wall"]
rear_material = rear.data.materials[0].copy()
shader = rear_material.node_tree.nodes.get("Principled BSDF")
shader.inputs["Roughness"].default_value = 0.95
shader.inputs["Metallic"].default_value = 0
rear.data.materials[0] = rear_material
for i in range(9):
    bpy.ops.object.light_add(type="POINT", location=(-1.8 + i * 0.45, -0.02, 0.2))
    lamp = bpy.context.object
    lamp.name = "Warm reflected burner light"
    lamp.data.color = (1, 0.23, 0.035)
    lamp.data.shadow_soft_size = 0.15
    for frame in range(1, 181, 4):
        lamp.data.energy = (
            9 + 4 * math.sin(frame * 0.45 + i * 2.5) + 2 * math.sin(frame * 0.9 + i)
        )
        lamp.data.keyframe_insert("energy", frame=frame)
bpy.ops.object.light_add(type="AREA", location=(0, -2, 2.5))
bpy.context.object.data.energy = 30
bpy.context.object.data.shape = "RECTANGLE"
bpy.context.object.data.size = 4
bpy.context.object.rotation_euler = (
    (Vector((0, 0, 0.1)) - bpy.context.object.location)
    .to_track_quat("-Z", "Y")
    .to_euler()
)
bpy.ops.object.camera_add(location=(0, -6, 1.35))
camera = bpy.context.object
camera.rotation_euler = (
    (Vector((0, 0, 0.53)) - camera.location).to_track_quat("-Z", "Y").to_euler()
)
camera.data.type = "ORTHO"
camera.data.ortho_scale = 4.65
scene.camera = camera
scene.frame_set(50)
scene.render.filepath = str(ROOT / "burner-bed.png")
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / "burner-bed.blend"))
bpy.ops.render.render(write_still=True)
