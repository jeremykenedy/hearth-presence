#extension GL_OES_EGL_image_external : require
precision highp float;
uniform samplerExternalOES fire;
uniform sampler2D diffuseMap;
uniform sampler2D normalMap;
uniform mat4 videoMatrix;
uniform vec2 resolution;
uniform float time;
uniform float material;
uniform float opening;
uniform float hue;
uniform float light;
uniform float ash;
uniform float drift;
uniform float gas;
uniform float linear;
uniform float frameless;
uniform float frameThickness;
uniform float flameScale;
uniform vec3 ashParticles[12];
varying vec2 uv;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+1.),f.x),f.y);}
float grain(vec2 p){return noise(p)*.55+noise(p*3.1)*.25+noise(p*9.7)*.13+noise(p*30.)*.07;}
void main(){
 vec2 p=(uv-.5)*2.; p.x*=resolution.x/resolution.y;
 float breathe=1.+.004*sin(time*.019)*drift;
 p*=breathe; p+=drift*vec2(.012*sin(time*.013),.008*cos(time*.017));
 vec2 box=vec2(1.30,.73125)*opening;
 if(gas>.5)box=vec2(1.38,.6396875)*opening;
 if(linear>.5)box=vec2(1.42,.399375)*opening;
 vec2 q=abs(p)-box;
 float edge=max(q.x,q.y);
 float flicker=.91+.045*sin(time*2.7)+.035*sin(time*5.3)+.015*sin(time*11.);
 vec3 color;
 if(edge<0. || frameless>.5){
   vec2 f=(p/box+1.)*.5;
   if(frameless>.5){
     f=uv;
     float sourceAspect=linear>.5?3.555556:gas>.5?2.157303:1.777778;
     float viewAspect=resolution.x/resolution.y;
     if(viewAspect>sourceAspect)f.y=(f.y-.5)*sourceAspect/viewAspect+.5;
     else f.x=(f.x-.5)*viewAspect/sourceAspect+.5;
   }
   // Keep the physical burner bed fixed while changing the flame region above it.
   if(linear>.5 && f.y>.205)f.y=.205+(f.y-.205)/flameScale;
   vec4 coord=videoMatrix*vec4(f.x,f.y,0,1);
   color=f.y>1.?vec3(0.):texture2D(fire,coord.xy).rgb;
   float lum=dot(color,vec3(.299,.587,.114));
   float hot=smoothstep(.18,.7,lum);
   if(hue>.5 && hue<1.5)color=mix(color,vec3(lum*1.2,lum*.69,lum*.22),hot*.75);
   if(hue>1.5 && hue<2.5)color=mix(color,vec3(lum*.18,lum*.61,lum*1.25),hot*.9);
   if(hue>2.5)color=mix(color,vec3(lum*.8,lum*.28,lum*1.25),hot*.9);
   color*=mix(.68,1.1,light);
   // The reveal casts a soft shadow into the firebox.
   if(frameless<.5)color*=smoothstep(0.,.045,-edge);
   if(ash>0.)for(int i=0;i<12;i++){
     vec3 spark=ashParticles[i];
     vec2 distanceToAsh=(p-spark.xy)*vec2(1.,.7);
     float a=max(0.,1.-dot(distanceToAsh,distanceToAsh)*90000.);
     a=a*a*ash*spark.z;
     color+=vec3(.8,.34,.08)*a;
   }
 }else{
   vec2 surfaceUv=p*.5;
   if(material>1.5 && material<2.5)surfaceUv=(abs(p.x)>box.x+.1 && abs(p.y)<box.y+.2)?p*.55:p.yx*.55;
   vec3 stone=texture2D(diffuseMap,surfaceUv).rgb;
   vec3 normal=normalize(texture2D(normalMap,surfaceUv).rgb*2.-1.);
   vec3 toFire=normalize(vec3(-p.x,-p.y,.8));
   float relief=.78+.22*max(0.,dot(normal,normalize(vec3(-.4,.7,1.))));
   stone*=relief;
   if(material>.5 && material<1.5)stone*=1.6;
   if(material>2.5 && material<3.5){
     float slateTone=dot(stone,vec3(.299,.587,.114));
     stone=slateTone*vec3(.85,.93,1.0);
   }
   if(material>1.5 && material<2.5){
     float panel=abs(abs(p.x)-box.x-.17);
     if(panel<.095 && abs(p.y)<box.y+.05)stone*=.65+.35*smoothstep(.0,.02,panel);
   }
   if(material>1.5 && material<2.5){
     float molding=max(abs(p.x)-box.x,abs(p.y)-box.y);
     if(molding>.10 && molding<.24){
       float ridge=sin((molding-.10)/.14*18.85);
       stone*=.76+.18*ridge;
     }
     float column=abs(p.x)-box.x;
     if(column>.27 && column<.43 && p.y<box.y+.10 && p.y>-box.y-.18){
       float flute=sin((column-.27)*155.);
       stone*=.76+.16*flute;
     }
     if(p.y>box.y+.23 && p.y<box.y+.29)stone*=1.18;
     if(p.y>box.y+.29 && p.y<box.y+.32)stone*=.45;
   }
   float inner=max(q.x,q.y)/frameThickness;
   // Layered firebox reveal, a brushed metal lip and shadowed stone bevel.
   if(linear>.5)inner*=1.8;
   if(inner<.027)stone=vec3(.035,.032,.028)+.07*exp(-abs(inner-.014)*190.);
   else if(inner<.075)stone*=.43+.47*(inner-.027)/.048;
   else if(inner<.09)stone*=1.16;
   float room=.33+light*.6;
   float spill=exp(-length(max(q,vec2(0.)))*3.3)*.30*flicker;
   color=stone*room+stone*vec3(1.,.36,.09)*spill*(.6+.4*max(0.,dot(normal,toFire)));
   // The hearth slab catches the fire along its upper edge.
   if(p.y< -box.y-.12 && p.y> -box.y-.20){
     color*=1.12; color+=vec3(.08,.026,.006)*flicker*exp(-abs(p.x)*.9);
   }
 }
 float vignette=1.-.14*pow(length((uv-.5)*1.25),2.);
 color*=vignette;
 gl_FragColor=vec4(color,1.);
}
