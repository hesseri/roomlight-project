# RoomLight — Software Design

## Overview
Python CLI prototype, no external dependencies.
All code in a single file: src/main.py

## Structure
Single file. The prototype is short enough that splitting into modules would add unnecessary complexity. Course guidance: split when it hurts.

## Domain Model
- LightingZone: enum, three functional zones: Ambient, Task, Accent
- ZoneSettings: brightness and warmth per zone (0–100)
- Theme: named lighting configuration, defines ZoneSettings per zone
- Controller: holds runtime state: active theme, flex override, all_off

## Interactive Loop
The main loop runs until the user quits, keeping the Controller instance alive in memory. This mirrors how a real device works, always on, waiting for input.

## Limitations
- State resets on every run, a real controller would persist to local storage.
- No hardware control. Lighting output is simulated in the terminal.
