import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math
import numpy as np
import urllib.request
import os

# 1. Автоматическое скачивание файла нейросети (если его нет)
model_path = 'hand_landmarker.task'
if not os.path.exists(model_path):
	print("Скачиваем файл модели от Google (около 3 МБ)...")
	url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
	urllib.request.urlretrieve(url, model_path)
	print("Готово! Запускаю камеру...")

# 2. Настройка нового Tasks API
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
	base_options=base_options,
	num_hands=2,
	min_hand_detection_confidence=0.7,
	min_tracking_confidence=0.7
)
detector = vision.HandLandmarker.create_from_options(options)


# Функция для расчета расстояния
def calculate_distance(p1, p2):
	return math.hypot(p1.x - p2.x, p1.y - p2.y)


# Функция проверки кулака
def is_fist(hand_landmarks):
	wrist = hand_landmarks[0]
	tips = [8, 12, 16, 20]
	mcps = [5, 9, 13, 17]
	folded_fingers = 0
	for tip_idx, mcp_idx in zip(tips, mcps):
		if calculate_distance(hand_landmarks[tip_idx], wrist) < calculate_distance(hand_landmarks[mcp_idx], wrist):
			folded_fingers += 1
	return folded_fingers >= 3


# Связи для ручной отрисовки скелета руки (т.к. старый mp_draw теперь не работает)
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
draw_color = colors["p"]  #цвет
brush_size = 15

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

	gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
	_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV)
	frame_bg = cv2.bitwise_and(frame, frame, mask=mask)
	final_frame = cv2.bitwise_or(frame_bg, canvas)

	cv2.imshow("Air Paint", final_frame)

	# 'q' для выхода, 'c' для очистки холста
	key_char = chr(cv2.waitKey(1) & 0xFF)
	if key_char == "q":
		break
	elif key_char == "c":
		canvas = np.zeros((h, w, c), dtype=np.uint8)
	elif key_char in colors:
		draw_color = colors[key_char]


cap.release()
cv2.destroyAllWindows()