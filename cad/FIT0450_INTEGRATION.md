# FIT0450 chassis integration: CAD revision status

**Manufacturer:** [DFRobot FIT0450](https://www.dfrobot.com/product-1457.html)

The manufacturer's product page provides a **motor dimension drawing** and a **SolidWorks file** under Documents. Those are the appropriate references for precise motor-housing geometry, mounting features, shaft position and encoder clearance.

## Confirmed data

- 6 V nominal; 3–7.5 V motor range
- 160 rpm no-load at 6 V; 120:1 gearbox
- 0.2 kgf·cm rated torque; 0.8 kgf·cm stall torque
- 2.8 A maximum stall current
- 5 mm double-flat output shaft (from owner's supplier description)
- 55 × 48 × 24 mm overall (from owner's supplier description)
- Separate 2-pin motor and 4-pin encoder leads
- Encoder supply 4.5–7.5 V

## Existing design

The original FreeCAD chassis and exported four-holder STEP/STL assembly have been preserved in the downloadable CAD package. The earlier holder script uses an **assumed 23 × 18 mm cross-section** and **does not establish a FIT0450 fit**.

## Release gate for final fabrication

1. Import manufacturer dimension drawing or CAD solid.
2. Align shaft axes and verify actual gearbox/encoder envelope.
3. Confirm holder retention without obstructing gearbox, encoder or cable exits.
4. Confirm wheel-hub interface and chassis/wheel clearance.
5. Check chassis fastener holes and print one fit-test bracket.
6. Verify motor-driver current protection and 6 V regulated motor supply.

**Status: mechanically modeled prototype, not fit-validated fabrication release.** Do not use overall 55 × 48 × 24 mm as a substitute for a mounting drawing.

## Manufacturer CAD source located

- [Official FIT0450 dimension drawing (PDF)](https://github.com/Arduinolibrary/DFRobot_Micro_DC_Geared_Motor_with_Encoder/blob/master/FIT0450%20Micro%20DC%20Motor%20with%20Encoder-SJ01.pdf)
- [Official FIT0450 SolidWorks package](https://github.com/Arduinolibrary/DFRobot_Micro_DC_Geared_Motor_with_Encoder/blob/master/FIT0450%20Solidworks%20File.zip)

These files are hosted in the repository linked by the DFRobot manufacturer. The available connector confirmed their presence, but could not retrieve the binary CAD for direct geometric fit checking. **The original provisional mount geometry has therefore not been relabeled as FIT0450-fit-verified.**
