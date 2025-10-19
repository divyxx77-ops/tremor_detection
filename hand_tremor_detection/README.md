🖐️ Hand Tremor Detection using MediaPipe & OpenCV
📖 Overview

This real-time hand tremor detection system uses MediaPipe and OpenCV to track fingertip movements through a webcam. By analyzing subtle variations in the fingertip’s position, it calculates and displays the tremor intensity on-screen, providing an instant visual assessment of hand stability.


⚙️ How It Works

Captures live video using the system’s webcam.

Detects and tracks the index fingertip (landmark 8) using MediaPipe’s hand-tracking model.

Calculates the displacement and standard deviation of fingertip movement to estimate tremor intensity.


Displays the tremor level in real-time with color indicators:

🟢 Below 1.0 → Steady hand

🟡 1.0 – 3.0 → Mild tremor

🔴 Above 3.0 → Noticeable/Severe tremor


🧠 Interpretation

A low tremor level indicates stable hand movement, while a high tremor value reflects increased instability.
This can help in assessing motor control, fatigue, or potential neurological tremors during motion analysis.


💻 Requirements

Install the following Python packages before running the code:

pip install opencv-python mediapipe numpy scipy matplotlib


🚀 Usage

Run the Python script:

python tremor_detection.py



Allow webcam access when prompted.

Move your hand in front of the camera and observe the tremor level in real-time.

Press ‘q’ to exit the program.


📸 Output Example

The webcam window shows:

Detected hand landmarks

Real-time tremor level displayed at the top

Color feedback based on tremor intensity


🧩 Future Improvements

Add data logging for long-term tremor tracking

Plot live frequency graphs (FFT-based analysis)

Support for multi-hand tracking and comparative tremor study


👩‍💻 Author

Developed by A V K Divyalakshmi
Integrating Biotechnology with Computer Vision for health and motor analysis applications.
