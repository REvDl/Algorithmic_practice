import random
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math
import numpy as np
import urllib.request
import os

model_path = 'hand_landmarker.task'
if not os.path.exists(model_path):
    url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
    urllib.request.urlretrieve(url, model_path)

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2,
    min_hand_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
detector = vision.HandLandmarker.create_from_options(options)

face_model_path = 'face_landmarker.task'
if not os.path.exists(face_model_path):
    url = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
    urllib.request.urlretrieve(url, face_model_path)

face_options = vision.FaceLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=face_model_path),
    num_faces=1,
    min_face_detection_confidence=0.7
)
face_detector = vision.FaceLandmarker.create_from_options(face_options)

friend_face = cv2.imread('drun.png', cv2.IMREAD_UNCHANGED)

def calculate_distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def is_fist(hand_landmarks):
    wrist = hand_landmarks[0]
    tips = [8, 12, 16, 20]
    mcps = [5, 9, 13, 17]
    folded_fingers = 0
    for tip_idx, mcp_idx in zip(tips, mcps):
       if calculate_distance(hand_landmarks[tip_idx], wrist) < calculate_distance(hand_landmarks[mcp_idx], wrist):
          folded_fingers += 1
    return folded_fingers >= 3

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17)
]

cap = cv2.VideoCapture(0)
canvas = None
colors = {"r":(0, 0, 255),
         "b":(255, 0, 0),
         "g":(0, 255, 0),
         "w":(255, 255, 255),
         "l":(0, 0, 0),
         "y":(0, 255, 255),
         "a":(255, 255, 0),
         "p":(255, 0, 255)}
draw_color = colors["p"]
brush_size = 15
images = ["foto_for_track.png", "one.png", "two.png", "three.png", "four.png", "five.png"]

def random_photo():
    img = cv2.imread(random.choice(images))
    if img is not None:
        overlay_img = cv2.resize(img, (200, 200))
        return overlay_img
    return None

overlay_img = random_photo()

def random_region(img_size, box_size=200):
    h, w = img_size
    y = random.randint(0, h - box_size)
    x = random.randint(0, w - box_size)
    return slice(y, y + box_size), slice(x, x + box_size)

def is_fixiki(hand_landmarks):
    wrist = hand_landmarks[0]

    def is_up(tip_idx, mcp_idx):
       return calculate_distance(hand_landmarks[tip_idx], wrist) > calculate_distance(hand_landmarks[mcp_idx], wrist)

    index_up = is_up(8, 5)
    middle_up = is_up(12, 9)
    ring_down = not is_up(16, 13)
    pinky_down = not is_up(20, 17)
    thumb_down = calculate_distance(hand_landmarks[4], hand_landmarks[17]) < 0.15

    return index_up and middle_up and ring_down and pinky_down and thumb_down

current_coords = None
was_showing = False
press_key = False
face_key = False

while True:
    success, frame = cap.read()
    if not success:
       break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    if canvas is None:
       canvas = np.zeros((h, w, c), dtype=np.uint8)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    detection_result = detector.detect(mp_image)
    show_photo = False

    if detection_result.hand_landmarks:
       for hand_landmarks in detection_result.hand_landmarks:

          for connection in HAND_CONNECTIONS:
             p1 = hand_landmarks[connection[0]]
             p2 = hand_landmarks[connection[1]]
             cv2.line(frame, (int(p1.x * w), int(p1.y * h)), (int(p2.x * w), int(p2.y * h)), (0, 255, 0), 2)
          for lm in hand_landmarks:
             cv2.circle(frame, (int(lm.x * w), int(lm.y * h)), 4, (0, 0, 255), -1)

          if is_fist(hand_landmarks):
             center_point = hand_landmarks[9]
             cx, cy = int(center_point.x * w), int(center_point.y * h)
             cv2.circle(canvas, (cx, cy), brush_size, draw_color, cv2.FILLED)

          if is_fixiki(hand_landmarks):
             show_photo = True

    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV)
    frame_bg = cv2.bitwise_and(frame, frame, mask=mask)
    final_frame = cv2.bitwise_or(frame_bg, canvas)

    if show_photo and press_key and overlay_img is not None:
       if not was_showing or current_coords is None:
          current_coords = random_region(final_frame.shape[:2], box_size=200)
          new_photo = random_photo()
          if new_photo is not None:
              overlay_img = new_photo

       y_slice, x_slice = current_coords
       final_frame[y_slice, x_slice] = overlay_img
       was_showing = True
    else:
       was_showing = False
       current_coords = None

    face_mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    face_result = face_detector.detect(face_mp_image)

    if face_result.face_landmarks and face_key and friend_face is not None:
       landmarks = face_result.face_landmarks[0]
       nose = landmarks[1]
       nx, ny = int(nose.x * w), int(nose.y * h)

       eye_dist = calculate_distance(landmarks[33], landmarks[263])
       mask_scale = int(eye_dist * 3000 )

       if mask_scale > 20:
           resized_friend = cv2.resize(friend_face, (mask_scale, mask_scale))
           fh, fw = resized_friend.shape[:2]
           y1 = ny - int(fh // 1.7)
           x1 = nx - fw // 2
           y2 = y1 + fh
           x2 = x1 + fw

           if y1 >= 0 and y2 < h and x1 >= 0 and x2 < w:
               if resized_friend.shape[2] == 4:
                   friend_rgb = resized_friend[:, :, :3]
                   friend_alpha = resized_friend[:, :, 3] / 255.0
               else:
                   friend_rgb = resized_friend[:, :, :3]
                   friend_alpha = np.ones((fh, fw))

               roi = final_frame[y1:y2, x1:x2]
               final_frame[y1:y2, x1:x2] = (friend_rgb * friend_alpha[:, :, np.newaxis] +
                                            roi * (1.0 - friend_alpha[:, :, np.newaxis])).astype(np.uint8)

    cv2.imshow("Air Paint", final_frame)

    key = cv2.waitKey(1) & 0xFF
    if key != 255:
       key_char = chr(key)
       if key_char == "q":
          break
       elif key_char == "c":
          canvas = np.zeros((h, w, c), dtype=np.uint8)
       elif key_char == "e":
          press_key = not press_key
       elif key_char == "d":
          face_key = not face_key
       elif key_char in colors:
          draw_color = colors[key_char]

cap.release()
cv2.destroyAllWindows()