# RoomLight — Test Plan

## Scope
Prototype scope requirements:
- F-REQ-01: zone-based theme applies correctly
- F-REQ-02: apply command sets active theme
- F-REQ-03: flex mode overrides theme, apply returns to preset
- F-REQ-04: off command turns all lights off
- NF-REQ-01: controller state works without network (in-memory)

Out of scope: hardware requirements, not applicable to CLI simulation:
- NF-REQ-02: cybersecurity compliance (VLAN, network isolation)
- NF-REQ-03: hardware compatibility (switch boxes, fixtures)
- NF-REQ-05: hardware safety and longevity (CE marking, lifespan)

## Approach
Manual system testing, run the program, follow test cases, record pass/fail in docs/06_Test_Results.md

## Environment
- macOS terminal
- Python 3.14.3
- Run: python3 src/main.py

## Pass/Fail Criteria
Each test case in 06_Test_Cases.md must produce the expected output.
All prototype scope requirements must have at least one passing test case.

## Risks
- State resets on every run, tests must be run in a single session.
