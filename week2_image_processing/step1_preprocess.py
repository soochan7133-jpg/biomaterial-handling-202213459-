import cv2

# 이미지 읽기
img = cv2.imread("apple_side_A.png")

# 그레이스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 블러 처리 (노이즈 제거)
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 결과 출력
cv2.imshow("Gray Image", gray)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()