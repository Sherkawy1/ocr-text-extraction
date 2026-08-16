import os
import threading
import cv2
from paddleocr import PaddleOCR

CAMERA_INDEX = 1
OUTPUT_TXT_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "ocr_result.txt")
DEBUG_IMAGE_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "debug_frame.jpg")
MAX_OCR_DIM = 1280

print("Loading model...")
ocr = PaddleOCR(
    use_textline_orientation=True,
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    enable_mkldnn=False,
    lang="en",
)
print("Model loaded successfully!")

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print(f"Failed to open camera index {CAMERA_INDEX}.")
    exit()

for _ in range(15):
    cap.read()

print("\n--- INSTRUCTIONS ---")
print("Press SPACE to capture image and run OCR")
print("Press ESC to exit\n")


def extract_text(ocr_result):
    texts = []
    for res in ocr_result:
        data = res.json if hasattr(res, "json") else res

        if isinstance(data, dict):
            if "rec_texts" in data:
                texts.extend(data["rec_texts"])
            elif "res" in data and isinstance(data["res"], dict) and "rec_texts" in data["res"]:
                texts.extend(data["res"]["rec_texts"])
            elif "rec_text" in data:
                texts.extend(data["rec_text"])
        elif isinstance(data, list):
            for line in data:
                try:
                    texts.append(line[1][0])
                except (IndexError, TypeError):
                    pass

    return texts


state_lock = threading.Lock()
is_processing = False
last_result_text = None


def run_ocr_in_background(frame_to_process):
    global is_processing, last_result_text

    cv2.imwrite(DEBUG_IMAGE_PATH, frame_to_process)

    h, w = frame_to_process.shape[:2]
    if max(h, w) > MAX_OCR_DIM:
        scale = MAX_OCR_DIM / max(h, w)
        frame_for_ocr = cv2.resize(frame_to_process, (int(w * scale), int(h * scale)))
    else:
        frame_for_ocr = frame_to_process

    results = ocr.predict(frame_for_ocr)
    extracted_text = extract_text(results) if results else []
    text = "\n".join(extracted_text)

    with open(OUTPUT_TXT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print("\n===== OCR RESULT =====")
    print(text.strip() if text.strip() else "[No text detected]")
    print("======================")
    print(f"Saved text to: {OUTPUT_TXT_PATH}")
    print(f"Saved captured frame to: {DEBUG_IMAGE_PATH}")
    print("\nPress SPACE again to capture another image, or ESC to exit.\n")

    with state_lock:
        last_result_text = text
        is_processing = False


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to access camera")
        break

    display_frame = frame.copy()

    with state_lock:
        processing_now = is_processing

    if processing_now:
        cv2.putText(
            display_frame, "Processing OCR... please wait",
            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2
        )

    cv2.imshow("Camera - Press SPACE to capture, ESC to exit", display_frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 32 and not processing_now:
        print("Processing OCR in background...")
        with state_lock:
            is_processing = True
        threading.Thread(target=run_ocr_in_background, args=(frame.copy(),), daemon=True).start()

    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()