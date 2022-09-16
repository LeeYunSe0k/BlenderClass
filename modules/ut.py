import bpy

def select(objName):
    bpy.ops.object.select_all(action="DESELECT")
    bpy.data.objects[objName].select_set(True)
    
def activate(objName):
    bpy.context.view_layer.objects.active = bpy.data.objects[objName]
    
class sel:
    def translate(v):
        bpy.ops.transform.translate(value=v, constraint_axis=(True, True, True))
        
    def scale(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))
        
    def rotate_x(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')
    
    def rotate_y(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')    
            
    def rotate_z(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')
        
class act:
    def location(v):
        bpy.context.object.location = v
    
    def scale(v):
        bpy.context.object.scale = v
    
    def rotation(v):
        bpy.context.object.rotation_euler = v
    
    def rename(objName):
        bpy.context.object.name = objName
        
class spec:
    def scale(objName, v):
        bpy.data.objects[objName].scale = v
    
    def location(objName, v):
        bpy.data.objects[objName].location = v
        
    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v
        
class create:
    def cube(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0,0,0))
        act.rename(objName)
        
    def sphere(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0,0,0))
        act.rename(objName)
        
    def cone(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0,0,0))
        act.rename(objName)
        
def delete(objName):
    select(objName)
    bpy.ops.object.delete(use_global=False)
    
def delete_all():
    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
if __name__ == "__main__":
    create.cube('PerfectCube')
    sel.translate((0, 1, 2))
    
    sel.scale((1, 1, 2))
    sel.scale((0.5, 1, 1))
    
    sel.rotate_x(3.1415 / 8)
    sel.rotate_y(3.1415 / 5)
    sel.rotate_z(3.1415 / 3)
    
    create.cone('PointyCone')
    act.location((-2, -2, 0))
    spec.scale('PointyCone', (1.5, 2.5, 2))
    
    create.sphere('SmoothSphere')
    spec.location('SmoothSphere', (2,2,0))
    act.rotation((0, 0, 3.1415 / 3))
    act.scale((1, 3, 1))