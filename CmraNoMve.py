import cv2
from djitellopy import tello
from multiprocessing import Process

# Tells cv2 to process and show the drone camera
# Has a loop that continuously loads the photo frames read by the drone
def process_tello_video(drone):
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow('tello', frame)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
# if q is pressed, then it break the loop
            break
    cv2.destroyAllWindows()
# this terminates the video window when 1 is pressed
    drone.end()

# The Main code for the drone to run
def main():
    drone = tello.Tello()
    # Assigns the "drone" variable as the
    drone.connect()
    # Connects the drone to the internet
    drone.streamon()
    # has the drone turn on it's camera
    # this is required for the video to process!
    process_tello_video(drone)

#Idk what this means
if __name__ == '__main__':
    main()
