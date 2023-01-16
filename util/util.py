# Program To Read video
# and Extract Frames

import cv2
import glob

def readDir(basepath, recursiveFlag):
    return glob.glob(basepath, recursive=recursiveFlag)

# Function to extract frames
def FrameCapture(path):
    # print("--- inside FrameCapture ---")

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
        if(count == 20):
            break
    
    # print("Path" + path + " - "+ str(count))
    return count

# Function to detect faces
def DetectFace(path):
    print("--- inside face detection --")

# Function to Generate Patch 
def GeneratePatch(path):
    print("--- inside GeneratePatch --")
