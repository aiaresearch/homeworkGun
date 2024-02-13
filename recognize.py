from cnocr import CnOcr


# image_dir = r"E:\homeworkGun\tests\images"

# Initialize the OCR model
ocr = CnOcr(rec_model_name='number-densenet_lite_136-fc', det_model_name='en_PP-OCRv3_det', cand_alphabet='0123456789')

# start recognition
# 先读一张图片，然后识别，后面要改成按下扳机拍照识别
def recognize(img):
    results = []
    for line in ocr.ocr(img, det=True):
        print('recognized text: ', line['text'])
        results.append(line['text'])
    return results