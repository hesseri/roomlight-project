# RoomLight — Test Cases

| REQ | Test Case | Title |
|---|---|---|
| F-REQ-01 | TEST-01 | Theme shows all three zones |
| F-REQ-02 | TEST-02 | Apply sets active theme |
| F-REQ-03 | TEST-03 | Flex mode activates |
| F-REQ-03 | TEST-04 | Apply returns to preset from flex mode |
| F-REQ-04 | TEST-05 | Off turns all lights off |
| NF-REQ-01 | TEST-06 | All commands work without network |

---

**TEST-01**
Title: Theme shows all three zones
Requirement: F-REQ-01
Preconditions: Program running
Steps:
1. Type: `apply Golden Hour`
2. Type: `status`
Expected: status shows ambient, task and accent zones with brightness and warmth values

---

**TEST-02**
Title: Apply sets active theme
Requirement: F-REQ-02
Preconditions: Program running, no active theme
Steps:
1. Type: `apply Golden Hour`
2. Type: `status`
Expected: status shows "Active theme: Golden Hour"

---

**TEST-03**
Title: Flex mode activates
Requirement: F-REQ-03
Preconditions: Program running, Golden Hour applied
Steps:
1. Type: `apply Golden Hour`
2. Type: `flex 80 40`
3. Type: `status`
Expected: status shows "[Flex Mode] brightness=80  warmth=40"

---

**TEST-04**
Title: Apply returns to preset from flex mode
Requirement: F-REQ-03
Preconditions: Program running, flex mode active
Steps:
1. Type: `flex 80 40`
2. Type: `apply Golden Hour`
3. Type: `status`
Expected: status shows "Active theme: Golden Hour", no Flex Mode indicator

---

**TEST-05**
Title: Off turns all lights off
Requirement: F-REQ-04
Preconditions: Program running, Golden Hour applied
Steps:
1. Type: `apply Golden Hour`
2. Type: `off`
3. Type: `status`
Expected: status shows "All lights OFF"

---

**TEST-06**
Title: All commands work without network
Requirement: NF-REQ-01
Preconditions: Network disconnected or disabled
Steps:
1. Disconnect network
2. Start program: `python3 src/main.py`
3. Run TEST-01 through TEST-05
Expected: all commands work normally, no network errors
