import cv2

image = cv2.imread('image.jpeg')

height, width = image.shape[:2]
print(f'original image size: {width}x{height}')

new_height = int(height * (300 / 96))
new_width = int(width * (300 /96))

resized_image = cv2.resize(image, (new_width, new_height))

print(f'resized image size: {new_width}x{new_height}')

# cv2.imwrite('resized_image.jpeg', resized_image)

gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('gray_image.jpeg', gray_image)

denoised_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

cv2.imwrite('denoised_image.jpeg', denoised_image)

# _, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.imwrite('binary_image.jpeg', binary_image)