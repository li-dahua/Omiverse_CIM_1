import omni
from pxr import Gf, UsdGeom
import random


# Create a cube mesh in the stage
stage = omni.usd.get_context().get_stage()

for i in range(3):
    result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
    size=random.randint(0,20)
    loca1=random.randint(-500,500)
    loca2=random.randint(-1000,1000)
    loca3=random.randint(-1500,1500)

    # Get the prim and set its transform matrix
    cube_prim = stage.GetPrimAtPath(path)
    UsdGeom.XformCommonAPI(cube_prim).SetTranslate(Gf.Vec3d(loca1,loca2,loca3))
    UsdGeom.XformCommonAPI(cube_prim).SetScale(Gf.Vec3f(size,size, size))