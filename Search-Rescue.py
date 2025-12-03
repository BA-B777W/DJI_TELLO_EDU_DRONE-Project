import time
from djitellopy import Tello
# import tello library and time (to pause the code for periods of time)
tello = Tello()
# sets new variable program uses
tello.connect()
# connects to tello drone
time.sleep(2)
# pause code for 2 seconds
while True:
    try:
        i = int(input('Please Enter Length of Search Grid in cm (x): '))

        if i % 20 == 0:
            print('\n   Length (x): ' + str(i))
            forward_repeats = i / 20
            print('   Forward Repeats: ' + str(forward_repeats) + '\n')
            break
        else:
            print('   Error: ' + str(i) + ' is not a multiple of 20. Please try again.')
    except ValueError:
        print("   Error: Invalid input. Please enter a whole number that is a multiple of 20.")
# determines how many times the drone should move forwards in a grid pattern (initially)
# prompts user to input a multiple of 20, as the drone will move forward by increments of 20 cm
# divides the distance the user inputs (multiple of 20), to determine how many times the drone
# should move forward by 20 cm
# 3 types of conditions, user inputs a multiple of 20 (success), user inputs a value that isn't a
# multiple of 20 (fail), user enters a decimal instead of integer (error)
while True:
    try:
        j = int(input('Please Enter Width of Search Grid in cm (y): '))

        if j % 20 == 0:
            print('\n   Width (y): ' + str(j))
            lateral_repeats = j / 20
            print('   Lateral Repeats: ' + str(lateral_repeats) + '\n')
            break
        else:
            print('   Error: ' + str(j) + ' is not a multiple of 20. Please try again.')
    except ValueError:
        print("   Error: Invalid input. Please enter a whole number that is a multiple of 20.")
# determines how many times the drone should move sideways in a grid pattern (initially)
        time.sleep(1)
tello.turn_motor_on()
time.sleep(1)
input("Press Enter to continue...")
print("Starting flight")
print("battery level: " + str(tello.get_battery()))
# displays battery level to the user and waits for imput to start the drone search program
tello.turn_motor_off()
tello.takeoff()
tello.move_down(50)
tello.enable_mission_pads()
# enables search for mission pads
tello.set_mission_pad_detection_direction(0)
# defines which camera will search for the pads (1 forwards, 0 down)
pad_dist = tello.get_mission_pad_distance_x
# variable for requesting the mission pad distance from the drone (only works once the drone has found a mission pad)

def move(lr, fr):
    # defines the search grid pattern function
        for ii in range(int(fr)):
            tello.disable_mission_pads()
            tello.move_forward(20)
            tello.enable_mission_pads()
            time.sleep(1)
            # the drone will move forwards by 20 cm, stop to search for the pad, and then continue, repeating until
            # it has moved forwards as many times as defined by the variable "fr"
            if abs(int(pad_dist())) < 20:
                print('Successfully found')
                print('Mission Pad ID: ' + str(tello.get_mission_pad_id()))
                # if the drone finds the mission pad (after hovering over it), it will be able to request the distance
                # of the mission pad, allowing the user to see that the pad has been found
                tello.end()
                # ends drone process
                break
            if fr <= 0:
                # if the variable "fr" (forward repeats) is less than or equal to zero, the drone will not move forward
                # to search for the mission pad
                break
        tello.rotate_counter_clockwise(90)
        # rotates the drone to face a new direction to search for the mission pad
        for jj in range(int(lr)):
            tello.disable_mission_pads()
            tello.move_forward(20)
            tello.enable_mission_pads()
            time.sleep(1)
            if abs(int(pad_dist())) < 20:
                print('Successfully found')
                print('Mission Pad ID: ' + str(tello.get_mission_pad_id()))
                tello.end()
                break
            if lr <= 0:
                break
        tello.rotate_counter_clockwise(90)


move(lateral_repeats, forward_repeats)
lateral_repeats = lateral_repeats - 1

# subtracts just from the lateral repeat value due to the search patterns path

while True:
    move(lateral_repeats, forward_repeats)
    lateral_repeats = lateral_repeats - 1
    # each time the drone completes its move function, its path will shrink (subtracts one from each variable) until
    # the drone has covered the entire grid area searching for the mission pad
    forward_repeats = forward_repeats - 1
    if lateral_repeats <= 0 and forward_repeats <= 0:
        tello.land()
        tello.end()
        time.sleep(1)
        print('Search Unsuccessful')
        # if the drone completes all of its "move" cycles and continues not to find the mission pad, it will
        # automatically land and notify the user that the search failed
        break