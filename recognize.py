import cnocr
import os
import cap

# image_dir = r"E:\homeworkGun\tests\images"

# Initialize the OCR model
ocr = cnocr.CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det')

results = []

# start recognition
# 先读一张图片，然后识别，后面要改成按下扳机拍照识别
while True:
    frame = cap.capImage()
    for line in ocr.ocr(frame, det=True):
        print('recognized text: ', line['text'])
        results.append(line['text'])
    break