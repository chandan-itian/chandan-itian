import bpy, math, os
from mathutils import Vector
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
def mat(name,color,metal=0.0,rough=.35,emission=0):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough
 if emission:p.inputs['Emission Color'].default_value=(*color,1);p.inputs['Emission Strength'].default_value=emission
 return m
navy=mat('Midnight ceramic',(.024,.045,.09),.45);cyan=mat('Cyan light',(.04,.75,.85),.35,emission=.5);blue=mat('Blue aluminium',(.05,.19,.45),.7);white=mat('Code silver',(.64,.8,.87),.3);violet=mat('Violet',(.38,.19,.85),.4)
def cube(name,loc,scale,material,bevel=.12):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(material);b=o.modifiers.new('Rounded edges','BEVEL');b.width=bevel;b.segments=4;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL');return o
for z,s,ma in [(0,5.5,navy),(.26,5.1,blue),(.44,4.75,navy)]:cube('Layered platform',(0,0,z),(s,3.8,.25),ma)
# Freestanding terminal with tangible thickness, bevels and luminous syntax.
cube('Terminal case',(0,.45,2.65),(4.9,.3,3.5),blue)
cube('Terminal glass',(0,.25,2.65),(4.65,.10,3.23),navy)
for i,ma in enumerate([violet,cyan,white]):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,radius=.07,location=(-1.98+i*.24,.15,3.96));bpy.context.object.data.materials.append(ma)
for row,width in enumerate([1.5,2.8,2.1,3.0,1.75,2.5]):
 cube('Syntax line',(-1.93+width/2+(row%2)*.22,.12,3.48-row*.35),(width,.055,.075),cyan if row%3==0 else white,.025)
# Code emblem as extruded typography.
def text(body,loc,size,ma):
 c=bpy.data.curves.new('Extruded code','FONT');c.body=body;c.align_x='CENTER';c.size=size;c.extrude=.055;c.bevel_depth=.009;o=bpy.data.objects.new(body,c);bpy.context.collection.objects.link(o);o.location=loc;o.rotation_euler=(math.pi/2,0,0);o.data.materials.append(ma)
cube('Floating code tile',(-2.8,-1.1,1.6),(1.55,.26,1.4),navy);text('</>',(-2.8,-1.255,1.35),.66,cyan)
cube('Floating API tile',(2.65,-.2,3.8),(1.65,.26,1.2),navy);text('API',(2.65,-.355,3.58),.57,white)
bpy.ops.mesh.primitive_torus_add(major_radius=.58,minor_radius=.09,location=(2.0,-1.3,1.2),rotation=(1.05,.3,.2));bpy.context.object.data.materials.append(cyan)
for loc,r,ma in [((-2.6,1.0,4.6),.22,violet),((2.9,1.3,1.0),.25,cyan)]:
 bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=r,location=loc);bpy.context.object.data.materials.append(ma);bpy.ops.object.shade_smooth()
world=bpy.context.scene.world;world.use_nodes=True;world.node_tree.nodes['Background'].inputs[0].default_value=(.025,.045,.08,1);world.node_tree.nodes['Background'].inputs[1].default_value=.4
for loc,power,color,size in [((1,-7,9),1800,(.65,.85,1),7),((-6,-2,5),1300,(.12,.7,1),5),((3,5,7),2100,(.45,.3,1),4)]:
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,2))-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(8,-14,9));cam=bpy.context.object;cam.rotation_euler=(Vector((0,0,2.2))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=9.3
s=bpy.context.scene;s.camera=cam;s.render.engine='CYCLES';s.cycles.samples=64;s.cycles.use_denoising=False;s.render.resolution_x=1000;s.render.resolution_y=850;s.render.resolution_percentage=100;s.render.film_transparent=True;s.render.image_settings.file_format='PNG';s.render.filepath=P+'/assets/scene.png';s.view_settings.view_transform='AgX';bpy.ops.wm.save_as_mainfile(filepath=P+'/source/profile-scene.blend');bpy.ops.render.render(write_still=True)
