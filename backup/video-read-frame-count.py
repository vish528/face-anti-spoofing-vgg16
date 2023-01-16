# Program To Read video
# and Extract Frames
# give frame count in a video

import cv2

# Function to extract frames
def FrameCapture(path):
    print("--- inside FrameCapture ---")

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0
    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        # cv2.imwrite("frame%d.jpg" % count, image)

        count += 1
    
    print("Number of frames - "+ str(count))


# Driver Code
if __name__ == '__main__':
    print("--- main method ---")

    # Calling the function
    FrameCapture("E:\\PROJECT_VER_1\\dataset\\test_release\\1\\1.avi")
