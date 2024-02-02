import cnocr
import os

image_dir = r"E:\homeworkGun\tests\images"


ocr = cnocr.CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det')

for file in os.listdir(image_dir):
    if file.endswith(".jpg") or file.endswith(".png"):
        for line in ocr.ocr(os.path.join(image_dir, file), det=True):
            print(line['text'])