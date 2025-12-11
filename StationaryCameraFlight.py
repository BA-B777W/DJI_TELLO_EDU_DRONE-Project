from djitellopy import tello
import cv2

drone = tello.Tello()
# defines the drone for the program

def process_tello_video(drone):
# Sets the process that turns on the drone camera
    print("Press q to end survey")
    drone.streamon()
    # Tells the drone to broadcast its camera

    while True:
    # Sets a loop that will continuously stream the drone camera to the computer
        frame = drone.get_frame_read().frame
        cv2.imshow('tello', frame)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # if q is pressed, then it break the loop
            break
    drone.streamoff()
    # has the drone turn off the stream


def main():
    drone.connect()
        # connects the drone to the internet
    print ("Battery:", drone.get_battery(), "%" )
        # tells us the current drone battery percentage

    # WRITE THE ACTUAL CODE HERE!!!!
    # everytime you want the drone to turn on its camera, run : process_tello_video(drone)
    drone.takeoff()
    drone.move_forward(50)
    process_tello_video(drone)
    drone.rotate_counter_clockwise(180)
    process_tello_video(drone)
     drone.move_forward(50)

    # Final parts of the actual code
    drone.land()
    cv2.destroyAllWindows()

# leave this in but idk why
#Idk what this means
if __name__ == '__main__':
    main()
