# Component references and mechanical constraints

Source: owner-supplied `Component references(1).pdf`. Product references are **options listed by the project**, not proof that each was installed.

## Drivetrain

| Component | Supplier reference | Published specification |
| --- | --- | --- |
| Encoder motor | [DFRobot FIT0450](https://www.gotronic.fr/art-kit-moteur-encodeur-fit0450-27583.htm) | 55 × 48 × 24 mm overall, 5 mm double-flat output shaft, 3–7.5 V motor supply, 2.8 A stall current |
| Four-channel motor shield | [DFRobot DRI0039](https://www.gotronic.fr/art-shield-moteurs-cc-4-x-1-2-a-dri0039-25557.htm) | 53 × 52 mm, 1.2 A continuous per channel, 3.2 A peak, motor supply 2.5–13.5 V |
| Wheels | [Amazon listing B0DQCH5NH2](https://www.amazon.fr/gp/product/B0DQCH5NH2) | Wheel diameter, width, hub bore and offset not yet independently verified |

## Critical engineering checks

1. **Motor fit:** The prior provisional motor-holder script assumes a 23 × 18 mm motor cross-section and 70 mm length. This is not verified against FIT0450. Published overall motor dimensions include the encoder/gearbox; the exact housing profile and mounting points need a dimensioned drawing or measurements before modifying the cradle.
2. **Wheel fit:** Check the wheel hub matches the motor's 5 mm double-flat shaft. Verify wheel diameter and offset before confirming chassis ground clearance.
3. **Motor driver protection:** FIT0450 stall current (2.8 A) exceeds the DRI0039 continuous 1.2 A/channel rating. Peak 3.2 A is not a continuous rating. Consider current limiting, motor load, startup and jam behavior; validate against the actual datasheets.
4. **Power:** The referenced 11.1 V 3S LiPo must not be connected directly to motors specified for 3–7.5 V. Verify regulated rails, fuse, grounding and safe battery handling.
5. **Mechanical assembly:** Print one test holder first; confirm shaft location, cable exit, encoder clearance, fasteners and service access.

## Other components listed in reference PDF

- Controllers: ESP32-S3 DevKitC-1, FireBeetle 2 ESP32-P4, Arduino Uno
- Computer: Raspberry Pi 5 (4 GB)
- Sensors: HC-SR04 ultrasonic, MPU6050 IMU, 12 MP camera
- Actuators: continuous-rotation servos and gripper options
- Power: 3S LiPo and adjustable DC/DC converter
- Expansion: 16-channel servo controller and I²C expansion board

## Sources

- [FIT0450 product page](https://www.gotronic.fr/art-kit-moteur-encodeur-fit0450-27583.htm)
- [DRI0039 product page](https://www.gotronic.fr/art-shield-moteurs-cc-4-x-1-2-a-dri0039-25557.htm)
- Owner-supplied component references PDF

**Status:** Parts identified; mechanical fit and electrical suitability still require validation. Do not label the current CAD as final production-ready.
