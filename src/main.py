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

class Controller:
    # NF-REQ-01: stores active theme locally so guest controls work without network
    def __init__(self):
        self.active_theme: Theme | None = None
        self.all_off: bool = False  # F-REQ-04: bedside master off state

    def set_theme(self, theme: Theme):
        # F-REQ-02: apply a named theme; also re-enables lights if they were off
        self.active_theme = theme
        self.all_off = False

# Single controller instance representing the room
controller = Controller()

def main():
    # RoomLight controller entry point
    pass

if __name__ == "__main__":
    main()
