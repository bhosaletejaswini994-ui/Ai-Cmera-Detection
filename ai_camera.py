
import cv2
import os
import time
from datetime import datetime
from ultralytics import YOLO

# Create photo folder on Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
save_folder = os.path.join(desktop, "AI_Camera_Photos")
os.makedirs(save_folder, exist_ok=True)

# Load AI model
print("Loading AI model...")
model = YOLO("yolo11n.pt")

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera not found.")
    raise SystemExit

print("AI Camera is running.")
print("Press Q to exit.")

last_capture = 0
cooldown = 5

try:
    while True:
        success, frame = camera.read()

        if not success:
            print("Unable to read camera.")
            break

        # Detect people
        results = model(frame, classes=[0], verbose=False)
        person_detected = False

        for result in results:
            for box in result.boxes:
                person_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame, (x1, y1), (x2, y2),
                    (0, 255, 0), 2
                )

                cv2.putText(
                    frame,
                    f"Person {float(box.conf[0]):.0%}",
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2
                )

        # Capture a photo at most every five seconds
        current_time = time.time()

        if person_detected and current_time - last_capture >= cooldown:

            # Get date and time of capture
            capture_datetime = datetime.now()

            timestamp = capture_datetime.strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            filename = f"person_{timestamp}.jpg"
            filepath = os.path.join(save_folder, filename)

            # Add date and time visibly to the photo
            date_time_text = capture_datetime.strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )

            cv2.putText(
                frame,
                date_time_text,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # Save the photo
            if cv2.imwrite(filepath, frame):
                print("Photo saved:", filepath)
                print("Capture date and time:", date_time_text)
                last_capture = time.time()

        # Display live camera
        cv2.imshow("AI Camera - Press Q to Exit", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()
    print("AI Camera stopped.")
