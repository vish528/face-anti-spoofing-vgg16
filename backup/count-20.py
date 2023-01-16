# Program To Read video
# and Extract Frames

import cv2
import glob

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


# Driver Code
if __name__ == '__main__':
    print("--- main method ---")
    sum = 0
    for f in glob.glob('E:\\PROJECT_VER_1\\dataset\\train_release\\**\\*.*', recursive=True):
        # print(f)
        sum += FrameCapture(f)
    print("Total frames - "+ str(sum))
    # for path in Path('E:\\PROJECT_VER_1\\dataset\\test_release').rglob('*.'):
    #     print(path.name)
    #     # Calling the function
    #     FrameCapture(path.name)
