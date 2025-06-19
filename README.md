# Gesture-Based Brightness Adjuster

A **contact-free** way to control your laptop or desktop screen brightness: simply pinch with your thumb and index finger in front of the webcam and watch the brightness adapt in real time.
The project is written in **Python** and relies on **OpenCV** and **MediaPipe** for robust hand-tracking, plus `screen_brightness_control` for actually changing the back-light.

![demo](docs/demo.gif)

> **Why?**
> In hospitals, clean rooms, kiosks, or any shared workstation, touching function keys is inconvenient or unhygienic.
> A camera-based approach offers an intuitive, zero-contact alternative.

---

## ✨ Features

| Gesture                  | Action                                                     | Notes                                                          |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------- |
| Thumb–index pinch/expand | **Continuously** map pinch distance → brightness (0-100 %) | Range is calibrated in code (`30 px … 220 px` by default)      |
| Pinky curled             | **Commit** the current brightness value                    | Prevents accidental changes while your hand is just passing by |
| FPS overlay              | Real-time frame-rate to check performance                  |                                                                |

*Future ideas (see Roadmap):*
multi-user support, ambient-light fusion, Mac/Linux back-ends, more gestures (volume, media, etc.).

---

## 🗂️ Repository layout

```
handtrack.py            → reusable HandDetector class (OpenCV + MediaPipe)
brightnesscontrol.py    → main entry point; runs the webcam loop
README.md               → you are here
```

### handtrack.py

* Wraps MediaPipe Hands into a convenient `HandDetector` class.
* Exposes

  * `handDetect(img)` → annotate image & fill `self.results`
  * `positionLocate(img, hand=0)` → list of `[id, x, y]` landmarks.

### brightnesscontrol.py

1. Opens the default webcam (`cv2.VideoCapture(0)`).
2. Detects one hand, reads landmarks 4 (thumb tip) and 8 (index tip).
3. Computes Euclidean distance → interpolates to brightness value.
4. Checks if pinky (landmark 20) is curled; if yes → `sbc.set_brightness(value)`.
5. Draws UI overlays and shows the live feed.

---

## 🛠 Requirements

| Package                     | Tested version | Install                                 |
| --------------------------- | -------------- | --------------------------------------- |
| Python                      | 3.9+           | –                                       |
| opencv-python               | 4.10.\*        | `pip install opencv-python`             |
| mediapipe                   | 0.10.\*        | `pip install mediapipe`                 |
| numpy                       | ≥ 1.23         | `pip install numpy`                     |
| screen\_brightness\_control | 0.14.\*        | `pip install screen_brightness_control` |

⚠️ `screen_brightness_control` supports Windows & some X11 setups. macOS will need a different backend (see Roadmap).

---

## 🚀 Quick start

Run inside PyCharm (recommended)
Clone the repository
File ▸ New ▸ Project from Version Control ▸ Git → paste
https://github.com/Unieggy/gesturebased-brightness-controller.git

When PyCharm asks for an interpreter, choose New Virtual Environment
(any Python 3.9 + executable works).

PyCharm will spot missing packages. Click Install requirements or open
Settings ▸ Python Interpreter and add:

opencv-python
mediapipe
numpy
screen_brightness_control

Open brightnesscontrol.py, right-click → Run 'brightnesscontrol'.
A webcam window appears. Pinch to dim/brighten, curl your pinky to lock.

Stop the program with the red ■ button or by closing the video window.

Hold your hand \~40 cm from the webcam:

* **Pinch** thumb & index – closer → dimmer, wider → brighter.
* **Curl pinky** to lock the new brightness.

Press `q` (or close the window) to exit.

---

## 🧩 Configuration

Edit `brightnesscontrol.py`:

| Variable                           | What it does                                      |
| ---------------------------------- | ------------------------------------------------- |
| `Widthcam`, `Heightcam`            | capture resolution                                |
| `detectionCon`, `trackCon`         | MediaPipe confidence thresholds                   |
| `[30, 220]`                        | pixel-distance range mapped to 0-100 % brightness |
| `min_brightness`, `max_brightness` | clamp output range (optional)                     |

---

## 🗺 Roadmap

* [ ] Mac OS & Wayland brightness back-ends (`brightnessctl`, `ddcutil`, AppleScript)
* [ ] Multiple gestures (volume, play/pause, window snapping)
* [ ] Per-user calibration profiles
* [ ] Ambient-light sensor fusion

PRs and ideas are welcome!

---

## 📝 License

MIT © 2025 Your Name
See `LICENSE` for full text.
