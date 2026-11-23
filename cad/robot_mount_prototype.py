"""Generate provisional four motor cradles and chassis mounting holes.
Requires: pip install cadquery
Input: cad/Robot_Chassis.FCStd, exported from FreeCAD.
Outputs: STEP/STL files beside this script.
Dimensions are assumed, not validated against physical motors.
"""
from pathlib import Path
import tempfile
import zipfile
import cadquery as cq

OUT = Path(__file__).resolve().parent
FC = OUT / "Robot_Chassis.FCStd"
MOTOR_WIDTH = 23.0
MOTOR_HEIGHT = 18.0
MOTOR_LENGTH = 70.0
CLEARANCE = 0.8
MOUNT_Y = {"rear": -70.0, "front": 75.0}
HOLE_D = 3.4

def block(x0, x1, y0, y1, z0, z1):
    return (cq.Workplane("XY").box(x1-x0, y1-y0, z1-z0)
            .translate(((x0+x1)/2, (y0+y1)/2, (z0+z1)/2)).val())

def mount(side, cy):
    inner = MOTOR_WIDTH/2 + CLEARANCE/2
    outer = inner + 3.0
    body = block(20, 70, cy-25, cy+25, -4, 0)
    for sign in (-1, 1):
        ya, yb = (cy+inner, cy+outer) if sign == 1 else (cy-outer, cy-inner)
        body = body.fuse(block(29, 68, ya, yb, -(MOTOR_HEIGHT+6), -4))
        ya2, yb2 = (cy+inner-3, cy+outer) if sign == 1 else (cy-outer, cy-inner+3)
        body = body.fuse(block(29, 68, ya2, yb2, -(MOTOR_HEIGHT+6), -(MOTOR_HEIGHT+3)))
    for x in (28, 58):
        for y in (cy-19, cy+19):
            body = body.cut(cq.Solid.makeCylinder(HOLE_D/2, 8, cq.Vector(x,y,-6), cq.Vector(0,0,1)))
    body = body.clean()
    return body.mirror("YZ") if side == "left" else body

if not FC.is_file():
    raise FileNotFoundError("Place original Robot_Chassis.FCStd next to this script")
with zipfile.ZipFile(FC) as archive:
    with tempfile.NamedTemporaryFile(suffix=".brep") as tmp:
        tmp.write(archive.read("Body001.Shape.brp"))
        tmp.flush()
        chassis = cq.Shape.importBrep(tmp.name)

mounts = []
for side in ("left", "right"):
    for label, cy in MOUNT_Y.items():
        holder = mount(side, cy)
        mounts.append(holder)
        stem = OUT / f"PROTOTYPE_holder_{side}_{label}"
        cq.exporters.export(holder, str(stem)+".stl", tolerance=0.12, angularTolerance=0.15)
        cq.exporters.export(holder, str(stem)+".step")
        for x in (28,58):
            for y in (cy-19,cy+19):
                hx = -x if side == "left" else x
                chassis = chassis.cut(cq.Solid.makeCylinder(HOLE_D/2,9,cq.Vector(hx,y,-2),cq.Vector(0,0,1)))

chassis = chassis.clean()
cq.exporters.export(chassis,str(OUT/"PROTOTYPE_chassis_with_holes.stl"),tolerance=0.12,angularTolerance=0.15)
cq.exporters.export(chassis,str(OUT/"PROTOTYPE_chassis_with_holes.step"))
cq.exporters.export(cq.Compound.makeCompound([chassis]+mounts),str(OUT/"PROTOTYPE_full_assembly.step"))
print("Generated chassis, four motor holders, and assembly")
