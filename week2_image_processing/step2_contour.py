import cv2

# 이미지 읽기
img = cv2.imread("apple_side_A.png")

# 그레이스케일
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 블러
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 이진화
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

# 윤곽선 찾기
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선 그리기
cv2.drawContours(img, contours, -1, (0,255,0), 2)

# 결과 출력
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()