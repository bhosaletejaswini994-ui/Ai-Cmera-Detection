# AI Camera – Person Detection and Automatic Photo Capture

## 1. Project Overview

The **AI Camera** is a Python-based computer vision project that uses a webcam and the YOLO11 AI model to detect people in real time.

When a person is detected, the application automatically captures and saves a photo. Each photo contains the date and time of capture, making it useful for basic monitoring and record-keeping.

The application uses OpenCV to access the webcam, YOLO11 to detect people, and Python libraries to save photos with timestamps.

## 2. Features

- **Real-time person detection:** Detects people through a webcam using AI.
- **Automatic photo capture:** Captures a photo when a person is detected.
- **Five-second cooldown:** Saves photos at most once every five seconds while a person continues to be detected.
- **Date and time stamp:** Displays the capture date and time on each saved photo.
- **Automatic folder creation:** Creates a folder named `AI_Camera_Photos` on the Desktop.
- **Person detection box:** Draws a green rectangle around detected people.
- **Confidence percentage:** Displays the model's confidence score for each detection.
- **Easy exit:** Press `Q` to close the camera application.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV (`cv2`) | Webcam access, image processing, and displaying the camera feed |
| YOLO11 | AI-based person detection |
| Ultralytics | Loading and running the YOLO model |
| OS | Creating folders and managing file paths |
| Time | Managing the photo capture interval |
| Datetime | Adding date and time to captured photos |

## 4. Requirements

Before running the project, make sure you have:

- Python installed on your computer.
- A working webcam.
- An internet connection for the initial YOLO model download, if the model file is not already available.
- The required Python libraries installed.

## 5. Installation

### Step 1: Install the required libraries

Open Command Prompt or the VS Code terminal and run:

```bash
pip install opencv-python ultralytics
```

If you use Python 3.12 on Windows, you can also run:

```bash
py -3.12 -m pip install opencv-python ultralytics
```

### Step 2: Create the project file

Create a Python file named:

`ai_camera.py`

Copy your AI Camera Python code into this file and save it.

### Step 3: Run the project

Open the terminal in your project folder and execute:

```bash
py -3.12 ai_camera.py
```

Alternatively, if Python is configured as the default version:

```bash
python ai_camera.py
```

The first run may take some time because the YOLO11 model (`yolo11n.pt`) may need to be downloaded.

## 6. How the Project Works

1. The application creates the `AI_Camera_Photos` folder on the Desktop if it does not already exist.
2. It loads the YOLO11 nano model using `yolo11n.pt`.
3. It opens the computer's default webcam.
4. The camera continuously captures video frames.
5. The AI model checks each frame for people.
6. When a person is detected, a green rectangle and confidence percentage appear around the person.
7. If at least five seconds have passed since the last successful photo capture, the application saves a new photo.
8. The saved photo includes the capture date and time.
9. Pressing `Q` stops the application and releases the webcam.

## 7. Where Are the Photos Saved?

Photos are automatically saved in this folder:

```text
Desktop/
└── AI_Camera_Photos/
    ├── person_2026-10-27_11-30-00.jpg
    ├── person_2026-10-27_11-30-05.jpg
    └── person_2026-10-27_11-30-10.jpg
```

*Note: The filenames above are examples. Actual filenames depend on when photos are captured.*

Each photo has a unique timestamp-based filename, provided two captures do not occur within the same second.

## 8. Important Code Details

### YOLO model

```python
model = YOLO("yolo11n.pt")
```

Loads the YOLO11 nano model, a lightweight model suitable for many real-time computer vision applications.

### Detecting people

```python
results = model(frame, classes=[0], verbose=False)
```

Runs detection on the current camera frame. In the standard COCO-trained YOLO model, class ID `0` represents a person.

### Photo capture interval

```python
cooldown = 5
```

Sets a minimum five-second interval between successful captures while a person is detected.

### Saving photos

```python
cv2.imwrite(filepath, frame)
```

Saves the current processed camera frame as a JPEG image.

### Exiting the application

```python
if cv2.waitKey(1) & 0xFF == ord("q"):
    break
```

Stops the live camera loop when the user presses `Q`.

## 9. Applications and Use Cases

This project demonstrates concepts used in:

- Office and workplace monitoring systems.
- Visitor detection at entrances.
- Basic security camera prototypes.
- Smart building and IoT projects.
- Computer vision learning and demonstrations.
- Automated image collection for research and testing.

**Important:** This project detects people, but it does not identify their names, verify employee identity, or determine whether someone is authorized to enter. Production security systems require additional safeguards and appropriate access-control technology.

## 10. Limitations

- A working webcam is required.
- Detection accuracy depends on lighting, camera quality, distance, and the model.
- The application may occasionally miss people or detect objects incorrectly.
- The default camera index `0` may need to be changed if multiple cameras are connected.
- The application saves the full camera frame, not just a cropped image of the detected person.
- The application does not automatically delete old photos, so storage usage can increase over time.

## 11. Privacy and Responsible Use

Use this project only in locations where you have permission to operate a camera. Inform people when appropriate, protect captured images, restrict access to the photo folder, and follow applicable privacy laws and workplace policies.

## 12. Future Improvements

Possible enhancements include:

- A CustomTkinter graphical user interface.
- Start and stop camera buttons.
- A photo gallery showing saved images.
- A counter for detected people.
- Configurable photo capture intervals.
- Email or desktop notifications when a person is detected.
- Saving detection records in Excel or a database.
- Person tracking and entry/exit counting.

## 13. Author

**Project Name:** AI Camera – Person Detection and Automatic Photo Capture

**Language:** Python

**Project Type:** Artificial Intelligence / Computer Vision

**Purpose:** To demonstrate real-time person detection and automatic timestamped photo capture using a webcam.

---

*This project is intended for learning and prototyping AI-based computer vision applications.*
