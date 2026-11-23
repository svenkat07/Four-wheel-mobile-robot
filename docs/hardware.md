# Hardware overview

This page records components visible in the supplied robot assembly photographs. Exact model numbers, pin assignments, supply ratings and electrical connections should be confirmed against the physical build.

## Observed assembly

- Four-wheel mobile platform with motor mounts and mechanical supports
- Two-level chassis/platform with installed electronics
- Raspberry Pi single-board computer (reported as Raspberry Pi 5)
- Arduino Uno R3
- DFRobot-branded motor-control board
- HC-SR04-style ultrasonic distance sensor on a servo mount
- Power conversion modules and wiring

## Roles to confirm

| Component | Intended role | Verification needed |
| --- | --- | --- |
| Raspberry Pi | Higher-level computation/control | Software, operating system and interface to Arduino |
| Arduino Uno | Low-level motor/sensor interface | Firmware and actual pin mapping |
| Motor driver | Drive wheel motors | Exact model, voltage, current and channel wiring |
| Ultrasonic sensor | Distance sensing | Trigger/echo pins, voltage-level compatibility and measured range |
| Servo | Orient distance sensor | Supply, PWM pin and movement limits |
| DC motors | Four-wheel locomotion | Motor model, gearbox and channel arrangement |
| DC/DC modules | Power regulation | Measured output voltage, current capacity and grounding |

**Safety:** Do not connect 5 V logic outputs directly to Raspberry Pi 3.3 V GPIO. Confirm the ultrasonic echo interface and all power connections before energizing the system.

## Hardware evidence

The owner has supplied photographs showing a physical assembly. These images establish the presence of hardware but do not by themselves demonstrate powered operation, closed-loop control, obstacle avoidance or successful software testing.

## To document next

1. Add original photos to `images/` and label each with what it shows.
2. Confirm exact motor driver, power supply, board versions and pin connections.
3. Add a wiring diagram based on verified connections.
4. Record power-on checks and motor/sensor tests with dates and observations.
