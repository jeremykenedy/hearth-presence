precision highp float;
uniform vec2 resolution;
uniform float time;
uniform float drift;
uniform float opening;
uniform float gas;
uniform float linear;
uniform float frameless;
uniform float ash;
varying vec3 particle;
void main(){
 vec2 uv=gl_FragCoord.xy/resolution;
 vec2 p=(uv-.5)*2.;p.x*=resolution.x/resolution.y;
 p*=1.+.004*sin(time*.019)*drift;
 p+=drift*vec2(.012*sin(time*.013),.008*cos(time*.017));
 vec2 box=vec2(1.30,.73125)*opening;
 if(gas>.5)box=vec2(1.38,.6396875)*opening;
 if(linear>.5)box=vec2(1.42,.399375)*opening;
 vec2 q=abs(p)-box;
 if(frameless<.5 && max(q.x,q.y)>=0.)discard;
 vec2 distanceToAsh=(p-particle.xy)*vec2(1.,.7);
 float a=max(0.,1.-dot(distanceToAsh,distanceToAsh)*90000.);
 a=a*a*ash*particle.z;
 vec2 v=(uv-.5)*1.25;
 float vignette=1.-.14*dot(v,v);
 gl_FragColor=vec4(vec3(.8,.34,.08)*a*vignette,0.);
}
