import time

# ================================
# Global Configuration
# ================================

MAX_CRUISE_SPEED = 70        # Speed limit in km/h
MONITOR_INTERVAL = 2         # Time delay (seconds)

# ================================
# MCAL Layer (Sensor Interface)
# ================================

def mcal_read_speed_sensor():
    """
    Simulates reading raw speed data from hardware sensor.
    In real ECU, this comes from wheel speed sensors.
    """
    try:
        speed = float(input("Enter current vehicle speed (km/h): "))
        return speed
    except ValueError:
        print("Sensor Error: Invalid speed value")
        return None


# ================================
# ECU Abstraction Layer
# ================================

def ecu_get_vehicle_speed():
    """
    Converts raw sensor data into usable vehicle speed.
    """
    speed = mcal_read_speed_sensor()

    if speed is None:
        return None

    if speed < 0:
        print("ECU Error: Speed cannot be negative")
        return None

    return speed


# ================================
# RTE Layer (Data Communication)
# ================================

def rte_send_speed_to_application():
    """
    Transfers vehicle speed data to Application Layer.
    """
    return ecu_get_vehicle_speed()


def rte_send_alert_to_bsw(alert_status):
    """
    Transfers alert request from Application to BSW.
    """
    bsw_handle_alert(alert_status)


# ================================
# BSW Services Layer (Actuators)
# ================================

def bsw_handle_alert(alert_status):
    """
    Controls buzzer or warning lamp.
    """
    if alert_status:
        print("🚨 BSW: Overspeed Warning Activated!")
    else:
        print("🟢 BSW: Speed Normal")


# ================================
# Application Layer (Cruise Control Logic)
# ================================

def cruise_control_application():
    """
    Main Cruise Control logic.
    Compares speed against threshold.
    """
    vehicle_speed = rte_send_speed_to_application()

    if vehicle_speed is None:
        return

    print(f"Current Speed: {vehicle_speed} km/h")

    if vehicle_speed > MAX_CRUISE_SPEED:
        rte_send_alert_to_bsw(True)
    else:
        rte_send_alert_to_bsw(False)


# ================================
# System Scheduler (Main Loop)
# ================================

def system_scheduler():
    """
    Simulates ECU cyclic task execution.
    """
    print("\nCruise Control Speed Monitoring Started...\n")

    while True:
        cruise_control_application()
        print("-" * 40)
        time.sleep(MONITOR_INTERVAL)


# ================================
# Program Entry Point
# ================================

if __name__ == "__main__":
    system_scheduler()