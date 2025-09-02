import easyocr
import cv2
from matplotlib import pyplot as plt

reader = easyocr.Reader(['ja'])

# image = cv2.imread('denoised_image.jpeg')

image = cv2.imread('image.jpeg')


result = reader.readtext(image)

for (bbox, text, prob) in result:
    print(f'Text: {text}, Confidence: {prob:.2f}')
    top_left = tuple(map(int, bbox[0]))
    bottom_right = tuple(map(int, bbox[2]))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
