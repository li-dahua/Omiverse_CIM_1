import omni
from pxr import Gf, UsdGeom

# Create a cube mesh in the stage
stage = omni.usd.get_context().get_stage()
result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")

# Get the prim and set its transform matrix
cube_prim = stage.GetPrimAtPath(path)
UsdGeom.XformCommonAPI(cube_prim).SetTranslate(Gf.Vec3d(100,100 ,100))
UsdGeom.XformCommonAPI(cube_prim).SetScale(Gf.Vec3d(2, 2, 2))