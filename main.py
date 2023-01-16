from util.util import *



# Driver Code
if __name__ == '__main__':
    print("--- main method ---")
    sum = 0
    for f in readDir('E:\\PROJECT_VER_1\\dataset\\train_release\\**\\*.*', True):
        # print(f)
        sum += FrameCapture(f)
    print("Total frames - "+ str(sum))