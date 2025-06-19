```markdown
# Gesture-Based Brightness Adjuster

A **contact-free** way to control your laptop or desktop screen brightness: simply pinch with your thumb and index finger in front of the webcam and watch the brightness adapt in real time.  
The project is written in **Python** and relies on **OpenCV** and **MediaPipe** for robust hand-tracking, plus [`screen_brightness_control`](https://pypi.org/project/screen-brightness-control/) for actually changing the back-light.

<img src="docs/demo.gif" width="640" alt="demo gif showing pinch-to-dim gesture">

> **Why?**  
> In hospitals, clean rooms, kiosks, or any shared workstation, touching function keys is inconvenient or unhygienic.  
> A camera-based approach offers an intuitive, zero-contact alternative.

---

## ✨ Features

| Gesture | Action | Notes |
|---------|--------|-------|
| Thumb–index pinch/expand | **Continuously** map pinch distance → brightness (0 % – 100 %) | Range is calibrated in code (`[30 px … 220 px]` by default) |
| Pinky curled | **“Commit”** the current brightness value | Prevents accidental changes when your hand is just passing by |
| FPS overlay | Real-time frame-rate to check performance | |

Future ideas (see **Roadmap** below):
* Multi-user support & user-specific calibration
* Ambient-light fusion for smarter auto-brightness
* Mac OS / Linux back-end adapters (currently Windows-only via *screen_brightness_control*)

---

## 🗂️ Repository layout

```

ESP32-NODEJS-SERVER/   ← your other project (irrelevant here)
handtrack.py           ← reusable HandDetector class (OpenCV + MediaPipe)
brightnesscontrol.py   ← main entry point; runs the webcam loop
requirements.txt       ← pinned dependency versions
.gitignore             ← keeps `__pycache__`, `.env`, etc. out of Git
README.md              ← you are here

````

### `handtrack.py`

* Wraps MediaPipe Hands into a convenient `HandDetector` class.
* Exposes:
  * `handDetect(img)` → annotate image & populate `self.results`
  * `positionLocate(img, hand=0)` → list of **[id, x, y]** landmarks
  * (extra helpers for distances, finger-state, etc.—extend as needed)

### `brightnesscontrol.py`

1. Opens the default webcam (`cv2.VideoCapture(0)`).
2. Detects one hand, reads landmarks 4 (thumb tip) and 8 (index tip).
3. Computes Euclidean distance → interpolates to brightness value.
4. Checks if pinky (landmark 20) is curled; if yes → calls  
   `sbc.set_brightness(value)`.
5. Draws all UI overlays (landmarks, lines, FPS) and shows the live feed.

---

## 🛠  Requirements

| Package | Tested version | Install command |
|---------|----------------|-----------------|
| Python  | 3.9+           | – |
| OpenCV  | `opencv-python==4.10.*` | `pip install opencv-python` |
| MediaPipe | `mediapipe==0.10.*` | `pip install mediapipe` |
| NumPy   | `numpy>=1.23`  | `pip install numpy` |
| Screen Brightness | `screen-brightness-control==0.14.*` | `pip install screen_brightness_control` |

> ⚠️  `screen_brightness_control` currently supports Windows & some Linux/X11 setups.  
> On macOS you’ll need a different backend (see *Roadmap*).

---

## 🚀 Quick start

```bash
git clone https://github.com/<your-user>/gesture-brightness.git
cd gesture-brightness
python -m venv venv
venv\Scripts\activate         # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python brightnesscontrol.py
````

Hold your hand \~40 cm from the webcam:

* **Pinch** thumb & index.
  *Closer* ⇒ dimmer, *wider* ⇒ brighter.
* **Curl pinky** to “lock-in” the new brightness value.

Press **`q`** (or close the window) to exit.

---

## 🧩 Configuration

Open `brightnesscontrol.py` and tweak:

| Variable                           | Purpose                                             |
| ---------------------------------- | --------------------------------------------------- |
| `Widthcam`, `Heightcam`            | capture resolution                                  |
| `detectionCon`, `trackCon`         | MediaPipe confidence thresholds                     |
| `[30, 220]`                        | pixel distance range mapped to 0 %–100 % brightness |
| `min_brightness`, `max_brightness` | clamp output range (if desired)                     |

---

## 🗺  Roadmap

* [ ] **Mac OS & Wayland** brightness backend
  (`brightnessctl`, `ddcutil`, or AppleScript wrapper)
* [ ] **Multiple gestures** (volume, media control, window snapping)
* [ ] **Per-user calibration** saved in a small YAML/JSON profile
* [ ] **Ambient-light sensor fusion** for context-aware brightness

Pull requests and suggestions welcome!

---

## 📝 License

MIT © 2025 Your Name
See [LICENSE](LICENSE) for details.

```

> **Tip:** drop a short **demo GIF** in `docs/demo.gif` (or change the link) so visitors immediately see the project in action.
```
