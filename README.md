# RoomLight

A CLI prototype for a smart hotel lighting control system.
Lights are organized into functional zones (Ambient, Task, Accent)
and controlled through named themes, so the same theme works
regardless of how many fixtures a room has.

## Run

```
python3 src/main.py
```

## Commands

| Command | Description |
|---|---|
| `status` | Show current room state |
| `list-themes` | List available themes |
| `apply <theme name>` | Apply a named theme (F-REQ-02) |
| `flex <brightness> <warmth>` | Guest override, values 0–100 (F-REQ-03) |
| `off` | Turn all lights off (F-REQ-04) |
| `quit` | Exit |

## Example Session

```
$ python3 src/main.py
RoomLight Controller
Commands: status, list-themes, apply <name>, flex <brightness> <warmth>, off, quit
> list-themes
  - Golden Hour
  - Energizing Morning
> apply Golden Hour
Theme 'Golden Hour' applied.
> status
Active theme: Golden Hour
  ambient    brightness=60  warmth=80
  task       brightness=30  warmth=60
  accent     brightness=80  warmth=90
> flex 80 40
[Flex Mode] brightness=80  warmth=40
> apply Golden Hour
Theme 'Golden Hour' applied.
> off
All lights OFF.
> quit
Shutting down.
```

## Run Tests

```
pytest tests/test_main.py -v
```

## Docs

- `docs/01_Press_Release.md` -> product vision
- `docs/03_Requirements.md` -> functional and non-functional requirements
- `docs/03_Prototype_Scope.md` -> what the prototype validates
- `docs/04_Domain_Model.md` -> domain entities
- `docs/05_SW_Design.md` -> software design decisions
- `docs/06_Test_Plan.md` -> test plan
- `docs/06_Test_Cases.md` -> test cases

## Video presentation
https://youtu.be/gNK-0QKnh40