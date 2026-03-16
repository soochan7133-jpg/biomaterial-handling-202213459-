import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread("apple_side_A.png")

# 전처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

# 윤곽선 찾기
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 가장 큰 윤곽선 선택
c = max(contours, key=cv2.contourArea)

# 면적
area = cv2.contourArea(c)

# 둘레
perimeter = cv2.arcLength(c, True)

# circularity 계산
circularity = 4 * np.pi * area / (perimeter * perimeter)

print("Area:", area)
print("Perimeter:", perimeter)
print("Circularity:", circularity)

# 윤곽선 표시
cv2.drawContours(img, [c], -1, (0,255,0), 2)

cv2.imshow("Shape Analysis", img)

cv2.waitKey(0)
cv2.destroyAllWindows()