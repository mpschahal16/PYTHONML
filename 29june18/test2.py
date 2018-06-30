import cv2  # importing opencv
from datetime import datetime  # importing datetime for current date and time of system

camera = cv2.VideoCapture(0)  # camera capture initialisation


def get_image(frame):  # function to captute single image
    # (frame is the captured frame when you click c on keyboard)


    cv2.

    file = "/home/manpreet/mps/campture" + str(datetime.now()) + ".png";  # relative address where
    # you want to save the file whih the name by which you want to save it

    ##datetime.now() used in above line will get the current full time with date of the system

    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, frame)

    print("File saved at location :" + file)  ##dprinting the location of the file where it is saved

    #### above function end


while (True):  # infinite loop
    ret, frame = camera.read()  # capturing frame unless while loop break

    print(ret)  ##this print is used to check the value of ret which contain true of frame is retuned else false

    gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)  # this is used to change color format of image read more on internet
    cv2.imshow('frame', gray)  ##this is used to diplay the frame on screen
    if cv2.waitKey(30) == ord('q'):  ###this will get the pressd key of keboard and compare it with q
        break  # terminate

    if cv2.waitKey(30) == ord('c'):  ###this will get the pressd key of keboard and compare it with c
        get_image(frame)  # calling function to save the frame at that instance
        break  # terminate

camera.release()  # releasing camera
cv2.destroyAllWindows()  # releasing cv2


