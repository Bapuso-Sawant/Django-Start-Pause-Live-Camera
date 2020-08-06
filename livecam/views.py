from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import cv2


def dashboard(request):
    return render(request,'livecam/mainpage.html')

def startcam(request):
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    flg = 0
    while True:
        ret, img = cam.read()
        cv2.imshow("Start",img)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            cv2.destroyAllWindows()
            while True:
                cv2.imshow("Pause",img)
                if cv2.waitKey(1) & 0xFF == ord('s'): #to start
                    cv2.destroyAllWindows()
                    break

                if cv2.waitKey(1) & 0xFF == ord('q'): #to quite/stop
                    flg = 1
                    break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if flg == 1:
            break
    cam.release()
    cv2.destroyAllWindows()

    return render(request,'livecam/mainpage.html')
