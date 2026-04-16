import argparse
from dataclasses import dataclass
from enum import Enum

class LightingZone(Enum):
    # F-REQ-01: fixtures are tagged as one of three functional zones
    AMBIENT = "ambient"
    TASK = "task"
    ACCENT = "accent"

@dataclass
class ZoneSettings:
    # F-REQ-02, F-REQ-03: Brightness and warmth are configurable per zone
    brightness: int  # 0–100
    warmth: int      # 0–100 (cool to warm)

@dataclass
class Theme:
    # F-REQ-02: named lighting configuration with per-zone settings
    name: str
    zones: dict[LightingZone, ZoneSettings]


# Demo themes, used to validate zone-based approach
THEMES = {
    "Golden Hour": Theme(
        name="Golden Hour",
        zones={
            LightingZone.AMBIENT: ZoneSettings(brightness=60, warmth=80),
            LightingZone.TASK:    ZoneSettings(brightness=30, warmth=60),
            LightingZone.ACCENT:  ZoneSettings(brightness=80, warmth=90),
        }
    ),
    "Energizing Morning": Theme(
        name="Energizing Morning",
        zones={
            LightingZone.AMBIENT: ZoneSettings(brightness=90, warmth=30),
            LightingZone.TASK:    ZoneSettings(brightness=100, warmth=20),
            LightingZone.ACCENT:  ZoneSettings(brightness=70, warmth=30),
        }
    ),
}


def main():
    # RoomLight controller entry point
    parser = argparse.ArgumentParser(description="RoomLight controller")
    parser.add_argument("command", choices=["status"])
    args = parser.parse_args()

    if args.command == "status":
        # Placeholder
        print("RoomLight controller running. No active theme.")

if __name__ == "__main__":
    main()
