import sys
sys.path.insert(0, "src")

from main import Controller, THEMES, LightingZone


def test_theme_has_all_three_zones():
    # TEST-01: F-REQ-01: theme defines settings for all three functional zones
    theme = THEMES["Golden Hour"]
    assert LightingZone.AMBIENT in theme.zones
    assert LightingZone.TASK in theme.zones
    assert LightingZone.ACCENT in theme.zones


def test_apply_sets_active_theme():
    # TEST-02: F-REQ-02: apply command sets active theme
    controller = Controller()
    controller.set_theme(THEMES["Golden Hour"])
    assert controller.active_theme.name == "Golden Hour"


def test_flex_mode_activates():
    # TEST-03: F-REQ-03: flex command sets override with given brightness and warmth
    controller = Controller()
    controller.set_flex(80, 40)
    assert controller.flex_override is not None
    assert controller.flex_override.brightness == 80
    assert controller.flex_override.warmth == 40


def test_apply_clears_flex_mode():
    # TEST-04: F-REQ-03: applying a theme returns room to preset, clears flex override
    controller = Controller()
    controller.set_flex(80, 40)
    controller.set_theme(THEMES["Golden Hour"])
    assert controller.flex_override is None
    assert controller.active_theme.name == "Golden Hour"


def test_off_turns_all_lights_off():
    # TEST-05: F-REQ-04: off sets all_off flag and clears active theme
    controller = Controller()
    controller.set_theme(THEMES["Golden Hour"])
    controller.all_off = True
    controller.active_theme = None
    assert controller.all_off is True
    assert controller.active_theme is None


def test_controller_state_is_local():
    # TEST-06: NF-REQ-01: controller holds state in memory, no network needed
    controller = Controller()
    controller.set_theme(THEMES["Golden Hour"])
    controller.set_flex(70, 50)
    assert controller.active_theme is not None
    assert controller.flex_override is not None
