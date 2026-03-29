# RoomLight — Domain Model

Nouns listed below are collected from this products' requirements.

---

## Key Concepts

### Hotel
A property (or chain of properties) that installs and operates the RoomLight system. A hotel has one or more rooms and is managed by hotel staff.

### Room
A physical guest room within a hotel. A room contains one or more light fixtures and one or more controllers. A room has a current active theme and may be in a normal or Flex Mode state.

### Light Fixture
A physical lighting unit installed in a room (e.g. a bedside lamp) Each fixture belongs to exactly one lighting zone. A room may have a variable number of fixtures.

### Lighting Zone
A functional category assigned to one or more light fixtures. Examples: Ambient, Task, Accent. Zones abstract away individual bulbs so that themes work regardless of how many fixtures a room has. A fixture belongs to one zone, a zone can contain many fixtures.

### Controller
A hardware device installed in a room that manages the fixtures. The controller stores the zone mapping and active theme locally, enabling offline operation. A room has at least one controller. The controller communicates with the cloud when a network is available and operates independently when it is not.

### In-Room Panel
The physical user interface inside the room accessible to the guest. It offers theme buttons and (in Flex Mode) Brightness and Warmth sliders. One panel is associated with one room. The panel includes a bedside master off control.

### Bedside Master Off Control
A dedicated single-action control reachable from the bed that turns off all lights in the room. It operates without network or cloud connectivity.

### Theme
A named lighting configuration (e.g. "Energizing Morning") that defines brightness and color temperature values per lighting zone. Themes are created by hotel staff in the Cloud Dashboard and are pushed to controllers via a sync operation. A hotel owns many themes; one theme can be active in many rooms simultaneously.

### Active Theme
The theme currently applied to a room. A room has exactly one active theme at any given time, unless it is in Flex Mode, in which case the active theme is temporarily overridden.

### Flex Mode
A guest-initiated state in which the room's lighting deviates from the active theme via manual slider adjustments. The panel shows a "Flex Mode" indicator while in this state. Returning to any theme button exits Flex Mode and restores the brand preset.

### Welcome Scene
A special theme variant applied automatically when a guest arrives. It adapts to the time of day: bright and warm for daytime arrivals, softer for arrivals after 20:00.

### Brightness
A configurable lighting attribute representing the intensity of light output. Set per zone in a theme; also adjustable by the guest in Flex Mode.

### Warmth (Color Temperature)
A configurable lighting attribute representing the warmth or coolness of the light. Set per zone in a theme; also adjustable by the guest in Flex Mode via the Warmth slider.

### Cloud Dashboard
A web-based management interface used by hotel staff to create and manage themes, trigger global syncs, and view system diagnostics. It communicates with controllers over the network.

### Setup App
A configuration tool used by hotel staff (or an electrician during initial installation) to tag each light fixture with a lighting zone. Used once per room during setup or renovation.

### Sync
An operation triggered from the Cloud Dashboard that pushes the currently active theme to every controller in the hotel network simultaneously.

### Hotel Staff
Personnel who configure and manage the RoomLight system. They use the Setup App and the Cloud Dashboard. They do not need technical expertise to perform day-to-day operations after initial installation.

### Guest
The person staying in a room. Guests interact only with the in-room panel. They can select a theme or enter Flex Mode; they cannot create or edit themes.

### Checkout Event
A system event triggered when a guest checks out of a room. It causes the room to reset to the hotel's default scene automatically, without manual staff intervention.

### Diagnostic Dashboard
A view within the management interface that shows the status (online or faulted) of each fixture and controller. For faulted devices it indicates whether the problem is the bulb, the controller, or the network.

### VLAN (Operational Network)
The hotel's internal operational network on which RoomLight devices operate. Controllers and panels must never be reachable from the guest Wi-Fi network.

---

## Key Relationships

| Entity A | Relationship | Entity B |
|---|---|---|
| Hotel | has many | Rooms |
| Hotel | owns many | Themes |
| Room | contains many | Light Fixtures |
| Room | has at least one | Controller |
| Room | has one | In-Room Panel |
| Room | has one | Active Theme |
| Light Fixture | belongs to one | Lighting Zone |
| Lighting Zone | is part of | Theme (defines values per zone) |
| Theme | defines | Brightness and Warmth per Lighting Zone |
| Controller | stores locally | Zone Mapping and Active Theme |
| Controller | receives | Sync from Cloud Dashboard |
| In-Room Panel | used by | Guest |
| In-Room Panel | contains | Bedside Master Off Control |
| In-Room Panel | triggers | Flex Mode |
| Flex Mode | temporarily overrides | Active Theme |
| Cloud Dashboard | used by | Hotel Staff |
| Cloud Dashboard | triggers | Sync |
| Setup App | used by | Hotel Staff |
| Setup App | assigns | Light Fixture to Lighting Zone |
| Checkout Event | resets | Room to default Theme |
| Diagnostic Dashboard | monitors | Controllers and Light Fixtures |

---

## Boundary Notes

- **Guest scope:** Guests interact only with the in-room panel. They cannot access themes, zone configuration, or diagnostics.
- **Offline boundary:** The controller is the offline boundary. Everything above it (Cloud Dashboard, Sync) requires network connectivity; everything it manages locally (zone mapping, active theme, guest controls) must work without it.
- **Hardware boundary:** Initial installation requires a licensed electrician. All post-install configuration is done remotely by hotel staff via software tools.
