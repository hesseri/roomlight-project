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
    # Brightness and warmth are configurable per zone — F-REQ-02, F-REQ-03
    brightness: int  # 0–100
    warmth: int      # 0–100 (cool to warm)

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
