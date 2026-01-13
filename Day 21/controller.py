import time
import random

# ---------------- VEHICLE CONSTANTS ----------------
WHEEL_CIRCUMFERENCE = 2.0     # meters
PULSES_PER_REV = 20          # pulses per one wheel rotation
SPEED_LIMIT = 60             # km/h


# ---------------- SENSOR ----------------
def wheel_sensor():
    """
    Simulates wheel rotation by generating variable pulses
    """
    # Simulate how fast the wheel is rotating (slow to fast)
    rotations = random.uniform(2, 15)     # wheel rotations per second

    # Convert rotations to pulses
    pulses = int(rotations * PULSES_PER_REV)

    return pulses


# ---------------- ECU SPEED CALCULATION ----------------
def calculate_speed(pulses):
    rotations = pulses / PULSES_PER_REV
    distance = rotations * WHEEL_CIRCUMFERENCE   # meters per second
    speed = distance * 3.6                       # convert to km/h
    return round(speed, 2)


# ---------------- CONTROLLER ----------------
def speed_controller(speed):
    return speed > SPEED_LIMIT


# ---------------- ACTUATOR ----------------
def alarm_actuator(alarm, speed):
    print(f"\nVehicle Speed = {speed} km/h")

    if alarm:
        print("🚨 OVER SPEED!")
        print("🔔 Buzzer ON")
        print("💡 Warning Lamp ON")
    else:
        print("Speed OK")
        print("Buzzer OFF")
        print("Warning Lamp OFF")


# ---------------- MAIN ECU LOOP ----------------
print("Vehicle Speed Monitoring ECU Started 🚗")

while True:
    pulses = wheel_sensor()               # Wheel rotation sensed
    speed = calculate_speed(pulses)       # ECU calculates speed
    alarm = speed_controller(speed)       # ECU checks limit
    alarm_actuator(alarm, speed)          # Actuators react

    print("-----------------------------------")
    time.sleep(2)
