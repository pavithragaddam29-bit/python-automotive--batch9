

MAX_SPEED = 60   # Speed limit in km/h


# -------- SENSOR --------
def read_speed_sensor():
    """
    Simulates reading speed from a vehicle speed sensor
    """
    speed = int(input("Enter current vehicle speed (km/h): "))
    return speed


# -------- CONTROLLER (ECU Logic) --------
def speed_controller(speed):
    """
    AUTOSAR Application Logic:
    Checks if speed is greater than 60 km/h
    """
    if speed > MAX_SPEED:
        return True   # Alarm ON
    else:
        return False  # Alarm OFF


# -------- ACTUATOR --------
def alarm_actuator(alarm_status):
    """
    Controls buzzer, warning lamp and dashboard display
    """
    if alarm_status:
        print("🔔 BUZZER ON")
        print("💡 WARNING LAMP ON")
        print("📺 Dashboard: OVER SPEED WARNING!")
    else:
        print("Buzzer OFF")
        print("Warning Lamp OFF")
        print("Dashboard: Speed Normal")


# -------- MAIN LOOP --------
print("Vehicle Over-Speed Alarm System Started 🚗")

while True:
    speed = read_speed_sensor()          # Sensor
    alarm = speed_controller(speed)     # Controller
    alarm_actuator(alarm)                # Actuator

    print("-" * 40)
