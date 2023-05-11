import cv2
import numpy as np
from gtts import gTTS
import os
import keyboard


MIN_MATCHES = 10
detector = cv2.ORB_create(nfeatures=5000)


index_params = dict(algorithm=1, trees=3)
search_params = dict(checks=100)
flann = cv2.FlannBasedMatcher(index_params, search_params)
imgarray = ['D:\\2.jpeg', 'D:\\3.jpeg', 'D:\\4.jpeg', 'D:\\1.jpeg', 'D:\\5.jpeg']
signarray = ["Zebra Crossing", "Gap In Median", "School Ahead", "Right Intersection", "Speed Limit 20"]

def load_input(i):

        input_image = cv2.imread(i)
        input_image = cv2.resize(input_image, (400, 550), interpolation=cv2.INTER_AREA)
        gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

        keypoints, descriptors = detector.detectAndCompute(gray_image, None)

        return gray_image, keypoints, descriptors



def compute_matches(descriptors_input, descriptors_output):
    if (len(descriptors_output) != 0 and len(descriptors_input) != 0):
        matches = flann.knnMatch(np.asarray(descriptors_input, np.float32), np.asarray(descriptors_output, np.float32), k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.68 * n.distance:
                good.append([m])
        return good
    else:
        return None



if __name__ == '__main__':
    input_image = ['', '', '', '', '']
    input_descriptors = ['', '', '', '', '']
    input_keypoints = ['', '', '', '', '']


flag=0
while(flag==0):

    #while(i >=0):
    for i in range(-1,len(imgarray)):
        i=(i+1)%5
        count=0
        input_image[i], input_keypoints[i], input_descriptors[i] = load_input(imgarray[i])


        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        while (ret):

            ret, frame = cap.read()


            if (len(input_keypoints[i]) < MIN_MATCHES):
                continue

            frame = cv2.resize(frame, (700, 600))
            frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


            output_keypoints, output_descriptors = detector.detectAndCompute(frame_bw, None)
            matches = compute_matches(input_descriptors[i], output_descriptors)

            if (matches != None and len(matches)>15):
                output_final = cv2.drawMatchesKnn(input_image[i], input_keypoints[i], frame, output_keypoints, matches,
                                                  None,
                                                  flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                #cv2.imshow(f'{i+1} object is detected', output_final)
                if(i==0):
                    tts = gTTS(text="Caution"+signarray[0]+"Ahead", lang="en")
                    tts.save("hello1.mp3")
                    os.system("start hello1.mp3")
                    cv2.imshow(signarray[0], output_final)
                    break
                    # continue
                elif(i==1):
                    tts = gTTS(text=signarray[1], lang="en")
                    tts.save("hello1.mp3")
                    os.system("start hello1.mp3")
                    cv2.imshow(signarray[1], output_final)
                    break
                    # continue
                elif (i == 2):
                    tts = gTTS(text=signarray[2], lang="en")
                    tts.save("hello1.mp3")
                    os.system("start hello1.mp3")
                    cv2.imshow(signarray[2], output_final)
                    break
                    # continue
                elif (i == 3):
                    tts = gTTS(text=signarray[3], lang="en")
                    tts.save("hello1.mp3")
                    os.system("start hello1.mp3")
                    cv2.imshow(signarray[3], output_final)
                    break
                    # continue
                elif (i == 4):
                    tts = gTTS(text=signarray[4], lang="en")
                    tts.save("hello1.mp3")
                    os.system("start hello1.mp3")
                    cv2.imshow(signarray[4], output_final)
                    break
                    # continue


            else:
                cv2.imshow('Not matched', frame)
                key = cv2.waitKey(50)
                continue

                if (key == 27):
                    break



