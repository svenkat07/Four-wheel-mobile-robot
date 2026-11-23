# Four-wheel robot chassis CAD

The original FreeCAD file `3d prototype final project.FCStd` was inspected. Its `Body001` solid is **200 × 250 × 5 mm**. The original document has a Part Design Pad, rounded fillets, and pocket features.

A reproducible CadQuery script is available at [robot_mount_prototype.py](robot_mount_prototype.py). It generates:

- A chassis with 16 nominal 3.4 mm M3 mounting holes
- Four separate underside motor cradles (left/right, front/rear)
- STEP and STL files for the chassis and holders
- A combined STEP assembly

The generator was executed against the original FreeCAD archive. Exported parts are valid solids, and the motor-holder geometry does not intersect the chassis solid. The original FCStd source was preserved without modification.

## Regenerate

Place the original FreeCAD file in this folder named `Robot_Chassis.FCStd`, install CadQuery, then run:

```sh
python -m pip install cadquery
python robot_mount_prototype.py
```

## Verification still required

The holder dimensions assume a **23 × 18 mm** motor cross-section and approximately **70 mm** length. These are provisional, not measurements. Verify wheel and shaft clearance, motor retention, screw lengths, access for nuts, electrical component mounts, print orientation and material strength before printing or assembly. First print one holder and test the actual motor fit.

The complete CAD package, including the original FreeCAD source and exported STEP/STL models, has been prepared for download separately. The large binary CAD files are **not yet uploaded to this GitHub repository**.
