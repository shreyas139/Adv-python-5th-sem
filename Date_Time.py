import cv2
from datetime import datetime

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # ===== Border =====
    cv2.rectangle(frame, (5, 5), (w-5, h-5), (0, 255, 0), 2)

    # ===== Center Crosshair =====
    cx, cy = w // 2, h // 2
    cv2.line(frame, (cx-20, cy), (cx+20, cy), (0, 255, 255), 2)
    cv2.line(frame, (cx, cy-20), (cx, cy+20), (0, 255, 255), 2)

    # ===== Recording Indicator =====
    cv2.circle(frame, (30, 30), 8, (0, 0, 255), -1)
    cv2.putText(frame, "REC", (45, 36),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 0, 255), 2)

    # ===== Resolution =====
    resolution = f"Resolution: {w} x {h}"
    cv2.putText(frame, resolution, (10, h - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 0, 0), 2)

    # ===== Date and Time =====
    current_time = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    cv2.putText(frame, current_time, (10, h - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 0, 0), 2)

    # Display video
    cv2.imshow("Webcam Information Dashboard", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 