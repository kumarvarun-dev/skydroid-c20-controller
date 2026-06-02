# Skydroid C20 Ground Station

A Python-based Ground Control Station (GCS) for the Skydroid C20 camera system. This application provides:

* Live RTSP video streaming
* Gimbal control
* Camera control (photo/video)
* Zoom control
* Command logging
* Simple Tkinter-based user interface

---

## Features

### Live Video Feed

* Connects to the C20 RTSP stream
* Displays real-time video inside the application
* Automatic frame updates

### Gimbal Control

* Pan Left
* Pan Right
* Tilt Up
* Tilt Down
* Stop Movement
* Center Gimbal

### Camera Functions

* Capture Photo
* Start Recording
* Stop Recording

### Zoom Functions

* Zoom In
* Zoom Out

### Command Logging

* Displays all transmitted UDP commands
* Useful for debugging and protocol analysis

---

## System Architecture

```text
+-----------------------+
|  Tkinter GUI          |
+-----------+-----------+
            |
            v
+-----------------------+
|  UDP Command Sender   |
|  Port: 9002           |
+-----------+-----------+
            |
            v
+-----------------------+
|  Skydroid C20 Camera  |
+-----------+-----------+
            |
            v
+-----------------------+
| RTSP Video Stream     |
| Port: 554             |
+-----------+-----------+
            |
            v
+-----------------------+
| OpenCV Video Display  |
+-----------------------+
```

---

## Requirements

### Python Version

```bash
Python 3.8+
```

### Dependencies

Install required packages:

```bash
pip install opencv-python pillow
```

or

```bash
pip install -r requirements.txt
```

Example `requirements.txt`

```text
opencv-python
Pillow
```

---

## Camera Configuration

Update the following parameters if your camera IP differs:

```python
CAMERA_IP = "192.168.144.108"
UDP_PORT = 9002

RTSP_URL = "rtsp://192.168.144.108:554/stream=1"
```

---

## Running the Application

```bash
python main.py
```

---

## Available Commands

### Gimbal Control

| Action | Command        |
| ------ | -------------- |
| Up     | `#TPUG2wPTZ01` |
| Down   | `#TPUG2wPTZ02` |
| Left   | `#TPUG2wPTZ03` |
| Right  | `#TPUG2wPTZ04` |
| Stop   | `#TPUG2wPTZ00` |
| Center | `#TPUG2wPTZ09` |

---

### Camera Control

| Action          | Command        |
| --------------- | -------------- |
| Take Photo      | `#TPUD2wCAP01` |
| Start Recording | `#TPUD2wREC01` |
| Stop Recording  | `#TPUD2wREC00` |

---

### Zoom Control

| Action   | Command        |
| -------- | -------------- |
| Zoom In  | `#TPUD2wDZM0A` |
| Zoom Out | `#TPUD2wDZM0B` |

---

## Project Structure

```text
project/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## User Interface

```text
+---------------------------------------------------------+
|                                                         |
|                RTSP Video Display                       |
|                                                         |
+-----------------------------------+---------------------+
                                    |
                                    | Gimbal Controls
                                    | Camera Controls
                                    | Zoom Controls
                                    |
                                    | Command Log
                                    |
                                    +---------------------+
```

---

## Future Improvements

* Keyboard control support
* Joystick integration
* Automatic camera discovery
* Video recording on PC
* Snapshot saving on PC
* Telemetry display
* Multi-camera support

---



