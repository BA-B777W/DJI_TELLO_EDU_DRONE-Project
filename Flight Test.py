import time
import cv2
from djitellopy import Tello

tello = Tello()
# assigns variable tello to the drone
tello.connect()
# connects drone
tello.turn_motor_on()
input("Press Enter to continue...")
print("Starting flight")
print("battery level: " + str(tello.get_battery()))
# awaits user input to start flight
tello.turn_motor_off()
tello.takeoff()
while True:
    if tello.get_distance_tof() < 50:
        tello.move_up(20)
        print(str(tello.get_distance_tof()+20))
    else:
        tello.move_down(20)
        print(str(tello.get_distance_tof()+20))
        break
# moves drone up and down until it is about 50 cm above the ground
tello.flip_forward()
tello.flip_back()
# drone performs tricks
while True:
    if tello.get_flight_time() < 20:
        tello.go_xyz_speed(50,0, 0,100)
#x: Forward (+), Backwards (-)
#y: Left (+), Right (-)
#z: Up (+), Down (-)
    else:
        tello.go_xyz_speed(-50,0,0,100)
        tello.land()
        tello.end()
# if the drone is flying for more than 20 seconds, it will move backwards and land
