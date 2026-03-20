# RoomLight — Product Requirements
Product requirements based on the RoomLight press release and stakeholder questions.

---

## Functional Requirements
ID | Description | Priority

- F-REQ-01 | **Lighting Zone Tagging** — The Setup App must let hotel staff tag each light fixture with a functional categories like Ambient, Task, or Accent. Themes control these categories, not individual bulbs, so the same theme works correctly no matter how many lights a room has. | MUST

- F-REQ-02 | **Brand Theme Creation and Global Sync** — Staff must be able to create named lighting themes in the Cloud Dashboard e.g. "Golden Hour" by setting brightness and color temperature per zone. A single Sync pushes the active theme to every controller in the network at once. | MUST

- F-REQ-03 | **Guest Flex Mode** — The in-room panel must offer Brightness and Warmth sliders so guests can adjust their lighting. Changes are a temporary override, the panel shows a "Flex Mode" indicator, and a single tap on any theme button returns the room to the brand preset. | SHOULD

- F-REQ-04 | **Bedside Master Off Control** — Every room needs a single control within arm's reach of the bed that turns off all lights at once. It must work even if the network or cloud is down. | MUST

- F-REQ-05 | **Automatic Room Reset on Checkout** — When a guest checks out, the room lighting resets to the hotel's default scene automatically, with no manual work from staff. | SHOULD

- F-REQ-06 | **Time-Aware Welcome Scene** — The welcome scene should adapt to the time of day: bright and warm for daytime arrivals, softer for arrivals after 20:00. | COULD

- F-REQ-07 | **Maintenance Diagnostic Dashboard** — The management interface should show each fixture and controller as online or faulted. For anything faulted, the system should tell you whether the problem is the bulb, the controller, or the network. | SHOULD

---

## Non-Functional Requirements
ID | Description | Priority

- NF-REQ-01 | **Offline Local Operation** — Each controller stores its zone mapping and active theme locally. All guest controls must keep working if the internet or cloud goes down. | MUST

- NF-REQ-02 | **Cybersecurity Compliance** — The system must pass a cybersecurity audit before installation. Devices operate on the hotel's operational VLAN and must never be reachable from the guest Wi-Fi. Network documentation must be delivered to the IT team. | MUST

- NF-REQ-03 | **Hardware Compatibility** — Controllers and panels must fit standard switch boxes and work with existing fixtures, so hotels can install the system during normal renovation cycles without opening walls or rerouting cables. Initial install needs a licensed electrician, all configuration changes after that should be doable remotely by hotel staff. | MUST

- NF-REQ-04 | **Minimal Guest Interface** — The in-room panel must have at most three visible controls. Labels must use clear text or simple icons, guest shouldn't need more than one sentence of explanation to use it. | MUST

- NF-REQ-05 | **Hardware Safety and Longevity** — The product must carry CE marking and meet applicable low-voltage safety directives. Controllers and panels should be designed for a 10-year lifespan, with at least a 5-year warranty and guaranteed spare part availability. | MUST
