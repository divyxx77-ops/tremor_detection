import cv2
import mediapipe as mp
import numpy as np
import time
from collections import deque

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6)
mp_draw = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)

# Store fingertip positions and timestamps
positions = deque(maxlen=150)
timestamps = deque(maxlen=150)

print("Press 'q' to quit...")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally (mirror view)
    frame = cv2.flip(frame, 1)

    # Convert to RGB for Mediapipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Use index fingertip (landmark 8)
            x = hand_landmarks.landmark[8].x
            y = hand_landmarks.landmark[8].y

            positions.append((x, y))
            timestamps.append(time.time())

            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if len(positions) > 2:
            dx = np.diff([p[0] for p in positions])
            dy = np.diff([p[1] for p in positions])
            
            # Proper Euclidean displacement
            disp = np.sqrt(dx**2 + dy**2)

            tremor_level = np.std(disp) * 1000  # scale for visibility

            # Color based on tremor intensity
            color = (0, 255, 0) if tremor_level < 1 else (0, 0, 255)

            # Show tremor level
            cv2.putText(frame, f"Tremor Level: {tremor_level:.2f}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Hand Tremor Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
