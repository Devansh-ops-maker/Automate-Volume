import mediapipe as mp
import cv2
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

   
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
           
            x_palm = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x

           
            volume_level = np.interp(x_palm, [0, 1], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(volume_level, None)

            
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            cv2.putText(frame, f"Volume: {int(np.interp(volume_level, [min_vol, max_vol], [0, 100]))}%", 
                        (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Volume Control", frame)

    
    if cv2.waitKey(1) & 0xFF == 13:
        break


cap.release()
cv2.destroyAllWindows()
