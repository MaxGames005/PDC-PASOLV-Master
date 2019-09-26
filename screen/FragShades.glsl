#ifdef GL_ES
    precision highp float;
#endif

varying vec4 normal_vec;
varying vec4 vertex_pos;

uniform mat4 normal_mat;

void main (void){
    //correct normal, and compute light vector (assume light at the eye)
    vec4 v_normal = normalize( normal_mat * normal_vec ) ;
    vec4 v_light = normalize( vec4(0,0,0,1) - vertex_pos );
    //reflectance based on lamberts law of cosine
    float theta = clamp(dot(v_normal, v_light), 0.0, 1.0);
    gl_FragColor = vec4(theta, theta, theta, 1.0);
}