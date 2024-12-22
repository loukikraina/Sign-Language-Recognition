# Sign Language Recognition App 🤟

## Overview
A desktop application built with PyQt5 that recognizes American Sign Language (ASL) gestures in real-time using computer vision and deep learning.

## Tech Stack
- Python 3.x
- PyQt5
- OpenCV (cv2)
- Keras
- NumPy

## Dependencies Installation
```bash
pip install opencv-python PyQt5 keras numpy
```

## Project Structure
```
project/
├── asl_model/          # Trained model directory
├── data/
│   └── asl_images/     # Reference ASL images
│       ├── A.jpg
│       ├── B.jpg
│       └── ...
└── gui3.py             # Main application file
```

## Modes of Operation

### 1. Learn Mode 📚
- Real-time ASL sign practice
- Shows target letter for practice
- Instant feedback on gesture accuracy
- Displays recognition confidence

### 2. Recognition Mode 👁️
- Basic sign-to-text conversion
- Shows recognized letter
- Displays confidence percentage
- Continuous recognition

### 3. Keyboard Mode ⌨️
- Continuous sign detection
- Sentence building capability
- Backspace support
- Real-time text display

## Features

### Core Functionality
- Real-time video processing
- ASL gesture recognition
- 24 letter support (A-Y, excluding J and Z)
- 90% confidence threshold
- Sentence building capability

### UI Elements
- Modern button design
- Hover animations
- Live video feed
- Recognition feedback
- Probability display
- Sentence visualization

## Controls

### Keyboard Shortcuts
- `Backspace`: Delete last character
- `A-Z`: Change target letter in Learn mode
- `Back Button`: Return to main menu

### Recognition Area
- 200x200 pixel central frame
- Real-time boundary display
- Visual recognition zone marker

## Technical Implementation

### Image Processing
1. Grayscale conversion
2. Histogram equalization
3. Image normalization
4. 28x28 resize for model input

### Threading
- QThread implementation
- Non-blocking video processing
- Smooth UI responsiveness
- Real-time frame updates

### Recognition Process
1. Frame capture
2. Image preprocessing
3. Model prediction
4. Confidence check
5. Result display

## Best Practices

### For Optimal Recognition
- Ensure good lighting
- Keep hands within marked area
- Hold gestures steady
- Maintain consistent distance
- Use plain background

### For Best Performance
- Regular camera checks
- Clear recognition area
- Update model as needed
- Monitor system resources

## Running the Application

Start the application:
```bash
python gui3.py
```

## System Requirements
- Working webcam
- Python 3.x environment
- Sufficient lighting
- Stable background
- Adequate processing power

## Notes
- Recognition accuracy depends on lighting conditions
- Model performs best with clear hand gestures
- Regular calibration may improve results
- Performance varies with system capabilities
