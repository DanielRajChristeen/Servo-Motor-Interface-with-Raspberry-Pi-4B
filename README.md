# **Servo Motor Interface with Raspberry Pi 4B**

A simple, high-impact project demonstrating how to control a **standard servo motor** using the **Raspberry Pi 4B** through direct GPIO-based PWM — no external driver board required.

This repo is perfect for beginners exploring embedded motion control, as well as makers prototyping robotics and automation systems.

---

## 🚀 **Project Overview**

This project uses the Raspberry Pi’s hardware PWM capability to rotate a servo motor across a range of angles. The implementation handles:

* GPIO setup
* 50 Hz PWM signal generation
* Angle-to-duty-cycle mapping
* Smooth forward and reverse servo sweeps
* Safe cleanup on program exit

The Pi directly drives the signal, while the servo power can come from an external 5V source for stability.

---

## 🧠 **How It Works**

### ✔ Core Algorithm

The script follows a simple but robust sequence:

1. Configure GPIO and set **GPIO18** as a PWM output pin.
2. Initialize **50 Hz PWM**, the standard control signal frequency for hobby servos.
3. Convert each target angle to a duty cycle using a linear formula:

   ```
   duty = 2 + (angle / 18)
   ```
4. Apply the duty cycle and allow the servo to reach the position.
5. Reset the duty cycle to eliminate jitter.
6. Sweep from **0° → ~180°** in steps, then back down.
7. Gracefully stop PWM and clean GPIO on exit.

### ✔ Important Values (Why They Matter)

| Parameter            | Value           | Purpose                             |
| -------------------- | --------------- | ----------------------------------- |
| **PWM Frequency**    | 50 Hz           | Standard refresh rate for RC servos |
| **GPIO Pin**         | GPIO18          | Supports stable hardware PWM        |
| **Duty Cycle Range** | ~2%–12%         | Maps to servo’s 0°–180° range       |
| **Delay (1 sec)**    | `time.sleep(1)` | Servo settling time                 |
| **Sweep Steps**      | 20° increments  | Smooth movement + test coverage     |
| **Micro-delay**      | 0.001 sec       | Prevents rapid loop execution       |

The code used in this project is provided in `Servo_interface.py` in this repository. 

---

## 🛠 **Hardware Requirements**

* Raspberry Pi 4B
* SG90 / MG995 / similar hobby servo
* Jumper wires
* Stable 5V supply for servo (recommended)
* Common ground between Pi and servo

**Connection Map:**

| Servo Wire             | Connects To                    |
| ---------------------- | ------------------------------ |
| Brown/Black (GND)      | Raspberry Pi GND               |
| Red (5V)               | External 5V or Pi 5V (if safe) |
| Orange/Yellow (Signal) | GPIO18                         |

---

## 📂 **Repository Structure**

```
📁 Servo-RPi-Interface
│
├── Servo_interface.py      # Main source code
├── README.md               # Documentation (this file)
└── LICENSE                 # MIT License
```

---

## ▶️ **How to Run**

1. Enable GPIO & install RPi.GPIO (if not installed):

   ```bash
   sudo apt-get install python3-rpi.gpio
   ```
2. Clone the repo:

   ```bash
   git clone <your-repo-url>
   cd Servo-RPi-Interface
   ```
3. Run the script:

   ```bash
   python3 Servo_interface.py
   ```

You should see the servo sweeping smoothly between angles.

---

## 📚 **What You Learn**

* PWM signal control on Raspberry Pi
* Mapping angles to duty cycles
* Interfacing actuators without external drivers
* Managing timing & motion accuracy
* Writing safe cleanup routines in GPIO projects

This serves as a foundation for robotics applications like pan-tilt rigs, robotic arms, automation modules, and smart IoT devices.

---

## 📄 **License**

MIT License — free to use, modify, and build upon.

---
