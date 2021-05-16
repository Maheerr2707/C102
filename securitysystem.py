import cv2 
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True

    while result:
        ret,frame = videocaptureobject.read() 
        imageName = "Image"+str(number)+".png" 
        cv2.imwrite(imageName,frame)
        start_time = time.time()
        result = False
    
    return imageName()
    print("snapshotTaken")

    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(self,imageName):
        accessToken = "sl.AwsI0bHkoBscvFFZzgjLJUyTH1wAIDfqTbIh4NlzQPJ2NVTVgiykMYtdZhDNMdRoZOFg6RuhJ4YGc9h41kACzaIpgTAaXBFDLLiuYgVYWt7I2uOQmcxANN_Ycywyd2dwdrbA9_s"
        #file = image_counter
        from_file = imageName
        to_file = "/test/"+imageName
        dbx = dropbox.Dropbox(accessToken)
        f = open(from_file,'rb')
        dbx.files_upload(f.read(),to_file, mode=dropbox.files.WriteMode.overWrite)
        print("fileUploaded")

def main():
    while True:
        if((time.time()-start_time)>=10):
            name = take_snapshot()  
            upload_file(name)


main()

