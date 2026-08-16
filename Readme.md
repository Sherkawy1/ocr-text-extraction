\# Real-Time Live Camera OCR System



A real-time Optical Character Recognition (OCR) desktop application built with Python, \*\*OpenCV\*\*, and \*\*PaddleOCR\*\*\[cite: 1]. The system captures live video frames from a camera feed, resizes the image for optimal performance, and performs multi-threaded OCR processing without freezing the live preview interface\[cite: 1]. Extracted text is saved automatically to a file\[cite: 1].



\---



\## Key Features



\- \*\*Live Camera Feed:\*\* Real-time camera streaming with interactive keyboard controls using OpenCV\[cite: 1].

\- \*\*Non-Blocking Multi-Threading:\*\* OCR inference runs in a background thread using Python's `threading` module, ensuring the live camera view remains responsive\[cite: 1].

\- \*\*Deep Learning OCR Engine:\*\* Powered by \*\*PaddleOCR\*\* for accurate text detection and recognition\[cite: 1].

\- \*\*Image Rescaling Optimization:\*\* Automatically scales down high-resolution frames before running OCR to reduce memory usage and speed up processing\[cite: 1].

\- \*\*Automatic Output Export:\*\* Saves the recognized text to `ocr\_result.txt` on the Desktop and captures a debug image (`debug\_frame.jpg`) for verification\[cite: 1].



\---



\## Tech Stack \& Libraries



\- \*\*Language:\*\* Python 3.x

\- \*\*Computer Vision:\*\* `opencv-python`\[cite: 1]

\- \*\*OCR Engine:\*\* `paddleocr`\[cite: 1]

\- \*\*Concurrency:\*\* `threading` (Standard Library)\[cite: 1]

\- \*\*OS \& Filesystem:\*\* `os` (Standard Library)\[cite: 1]



\---



\## Installation \& Setup



\### 1. Prerequisites

Ensure you have Python installed. It is recommended to use a virtual environment:



```bash

python -m venv venv

\# On Windows

venv\\Scripts\\activate

\# On Linux/macOS

source venv/bin/activate



```



\### 2. Install Dependencies



Install the required packages using `pip`:



```bash

pip install opencv-python paddleocr



```



\*Note: If you plan to run PaddleOCR on GPU, make sure to install `paddlepaddle-gpu`. Otherwise, CPU-based `paddlepaddle` will work as well.\*



\---



\## How to Run



1\. Connect your webcam or external camera.

2\. If using an external camera, update the `CAMERA\_INDEX` variable in `Ocr-Project.py` if needed (default is `1`):





```python

CAMERA\_INDEX = 1



```





3\. Run the script:

```bash

python Ocr-Project.py



```







\---



\## Usage Controls



| Key | Action |

| --- | --- |

| \*\*SPACEBAR\*\* | Capture current frame and run background OCR



&#x20;|

| \*\*ESC\*\* | Exit application and close camera feed



&#x20;|



\---



\## Output Files



When you press \*\*SPACE\*\*, the application outputs:



1\. \*\*`ocr\_result.txt`\*\* (Desktop): Contains all recognized lines of text extracted from the captured image.





2\. \*\*`debug\_frame.jpg`\*\* (Desktop): The exact frame captured for reference/debugging.







\---



\## Code Architecture



```

├── Ocr-Project.py            # Main application script

├── README.md                 # Project documentation

└── Outputs (Generated)

&#x20;   ├── \~/Desktop/ocr\_result.txt

&#x20;   └── \~/Desktop/debug\_frame.jpg



```



\---



\## Author



\* \*\*Ahmed Sherkawy\*\* - \*Computer Science \& AI Student\*



