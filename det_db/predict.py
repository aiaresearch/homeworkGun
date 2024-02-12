import cv2
import numpy as np

net = cv2.dnn.readNetFromONNX("model-quant.onnx")

im = cv2.imread("c.jpg")
in_shape = (128, 128)

# Resize to input shape
ratio = min(in_shape[1] / im.shape[1], in_shape[0] / im.shape[0])
nw = int(im.shape[1] * ratio)
nh = int(im.shape[0] * ratio)
im = cv2.resize(im, (nw, nh))
# Pad to input shape
top = (in_shape[0] - nh) // 2
bottom = in_shape[0] - nh - top
left = (in_shape[1] - nw) // 2
right = in_shape[1] - nw - left
im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

blob = cv2.dnn.blobFromImage(im, scalefactor=1./255., mean=[0.485, 0.456, 0.406], swapRB=True)

net.setInput(blob)
out = net.forward()
bmap = out[0, 0, :, :]
bmap = bmap > bmap.mean()
print(bmap.max())

# Create bounding boxes from output bit map
def get_boxes(map):
    boxes = []
    contours, _ = cv2.findContours((map * 255).astype(np.uint8), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        boxes.append(box)
    return boxes

boxes = get_boxes(bmap)

# Draw bounding boxes
for box in boxes:
    cv2.drawContours(im, [box], 0, (0, 255, 0), 2)

# Display
cv2.imshow("Input", im)
cv2.imshow("Output", out[0, 0, :, :])

cv2.imshow("Input", im)
cv2.imshow("Output", out[0, 0, :, :])

cv2.waitKey(0)