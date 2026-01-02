import pytest
from pressure_cooker import PressureCooker

class TestPressureCooker:
    def test_cook_rice(self):
        cooker = PressureCooker()
        actual = cooker.cook_rice("adequate")
        expected = "Rice cooked soft even"
        assert actual == expected
        print("Test 1 PASS Score 10")

    def test_boil_dal(self):
        cooker = PressureCooker()
        actual = cooker.boil_dal("normal")
        expected = "Dal soft veggies tender"
        assert actual == expected
        print("Test 2 PASS Score 9")

    def test_overfull_pot(self):
        cooker = PressureCooker()
        actual = cooker.start_overfull()
        assert "spilled" in actual  # Expects fail condition
        print("Test 3 FAIL Score 5")

    def test_no_water(self):
        cooker = PressureCooker()
        actual = cooker.start_no_water()
        assert "error" in actual.lower()
        print("Test 4 PASS Score 10")

    def test_lid_half_open(self):
        cooker = PressureCooker()
        actual = cooker.check_lid_pressure()
        assert "Locked" in actual
        print("Test 5 PASS Score 8")