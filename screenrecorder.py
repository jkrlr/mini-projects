import numpy as np      # pip install numpy
import cv2              # pip install opencv-python
import pyautogui        # pip install pyautogui


# display screen resolution, get it from your OS settings
screen_size = (1920,1080)

# define the frames to be captured per sec
frames_per_second = 20.0

# define the codec
video_codec = cv2.VideoWriter_fourcc(*'XVID')

# create the video write object
output = cv2.VideoWriter('out.avi',video_codec,frames_per_second,screen_size)

while True:
    # make a screenshot
    image = pyautogui.screenshot()

     # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(image)
    
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    # write the frame   
    output.write(frame)
    
    # show the frame
    cv2.imshow("screenshot", frame)
    
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited   
cv2.destroyAllWindows()
output.release()
