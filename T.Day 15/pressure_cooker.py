class PressureCooker:
    def _init_(self):
        self.status = "ready"

    def cook_rice(self, water_level="adequate"):
        if water_level == "adequate":
            self.status = "Rice cooked soft even"
        else:
            self.status = "Rice undercooked"
        return self.status

    def boil_dal(self, load="normal"):
        if load == "normal":
            self.status = "Dal soft veggies tender"
        else:
            self.status = "Dal hard"
        return self.status

    def start_overfull(self):
        return "Heated spilled mess"

    def start_no_water(self):
        return "Shut off error shown"

    def check_lid_pressure(self):
        return "Locked tight"

# Run example
if __name__=="__main__":
    cooker = PressureCooker()
    print("Main output:", cooker.cook_rice())

