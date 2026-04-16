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
    # Interactive loop: controller stays running and holds state, like the real device
    print("RoomLight Controller")
    print("Commands: status, list-themes, apply <name>, off, quit")

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down.")
            break

        if not line:
            continue

        # e.g. "apply Golden Hour" -> "apply", "Golden Hour"]
        parts = line.split(maxsplit=1)
        command = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if command == "quit":
            print("Shutting down.")
            break

        elif command == "status":
            if controller.all_off:
                print("All lights OFF")
            elif controller.active_theme:
                print(f"Active theme: {controller.active_theme.name}")
                for zone, settings in controller.active_theme.zones.items():
                    print(f"  {zone.value:<10} brightness={settings.brightness}  warmth={settings.warmth}")
            else:
                print("No active theme.")

        elif command == "apply":
            # F-REQ-02: apply a named theme to the controller
            if not arg:
                print("Usage: apply <theme name>")
            elif arg not in THEMES:
                print(f"Unknown theme: '{arg}'")
                print("Run 'list-themes' to see available themes.")
            else:
                controller.set_theme(THEMES[arg])
                print(f"Theme '{arg}' applied.")

        elif command == "off":
            # F-REQ-04: bedside master off, turns all lights off instantly
            controller.all_off = True
            controller.active_theme = None
            print("All lights OFF.")

        elif command == "list-themes":
            # F-REQ-02: show available themes
            print("Available themes:")
            for name in THEMES:
                print(f"  - {name}")

        else:
            print(f"Unknown command: '{command}'")
            print("Commands: status, list-themes, apply <name>, off, quit")

if __name__ == "__main__":
    main()
