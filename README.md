# Face Following Robot

A Raspberry Pi based autonomous robot capable of detecting and following a person's face using OpenCV, a servo-mounted camera, and a differential drive chassis.

---

# Features

- Face detection using OpenCV Haar Cascade
- Camera tracking using a servo motor
- Differential drive robot using two DC motors
- Automatic distance estimation based on face size
- Autonomous left/right steering
- GitHub friendly project structure
- Modular object-oriented architecture

---

# Hardware

Required components:

- Raspberry Pi 4
- Raspberry Pi Camera Module
- 2x DC Motors
- L293D Motor Driver
- Servo Motor (SG90 or similar)
- Battery Pack
- Robot Chassis
- microSD Card
- Jumper Wires

---

# Software

- Raspberry Pi OS
- Python 3
- OpenCV
- gpiozero
- NumPy

---

# Project Structure

```
face-following-robot/

├── camera/
│   └── camera.py
│
├── vision/
│   ├── face_detector.py
│   └── tracker.py
│
├── hardware/
│   ├── servo.py
│   └── motors.py
│
├── controller/
│   └── robot_controller.py
│
├── config/
│   └── gpio_config.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/DavidelPuricel/Tracking_CameraRobot.git

cd Tracking_CameraRobot
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the project

Simply execute:

```bash
python main.py
```

---

# How it works

1. The camera continuously captures frames.

2. OpenCV detects the largest face.

3. The face position is compared to the center of the image.

4. The servo rotates the camera to keep the face centered.

5. If the servo rotates too far left or right, the robot turns in the same direction.

6. The apparent size of the face is used to estimate distance.

7. The robot moves forward, backward or stops to maintain an appropriate distance.

---

# Robot Behaviour

| Face Position | Robot Action |
|--------------|--------------|
| Left | Turn Left |
| Right | Turn Right |
| Center & Far | Move Forward |
| Center & Close | Move Backward |
| Center & Correct Distance | Stop |
| No Face | Stop |

---

# GPIO Configuration

| Device | GPIO |
|---------|------|
| Servo | GPIO17 |
| Left Enable | GPIO18 |
| Left IN1 | GPIO23 |
| Left IN2 | GPIO24 |
| Right Enable | GPIO19 |
| Right IN1 | GPIO27 |
| Right IN2 | GPIO22 |

Modify `config/gpio_config.py` if different pins are used.

---

# Dependencies

```
opencv-python
numpy
gpiozero
lgpio
```

---

# Future Improvements

- MediaPipe Face Detection
- PID Servo Controller
- Smooth Differential Steering
- Face Recognition
- Object Avoidance
- Mobile App Control
- Live Video Streaming
- Battery Monitoring

---

# Authors

Developed as a university robotics practice project.

Author:
**David Vulcu**

GitHub:
https://github.com/DavidelPuricel

---

# License

This project is intended for educational purposes.