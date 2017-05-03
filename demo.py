import cv2

image = cv2.imread("wallet.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
num = str(int(gray_image[0][0]))
print ("number: " + num)
color_list = []
new_image = gray_image[:]
print(type(gray_image[0][0]))
for i in range(100):
    for j in range(len(gray_image[i])):
        if abs(int(num) - int(gray_image[i][j])) >= 30:
            print(gray_image[i][j])
            color_list.append(image[i][i])
        else:
            new_image[i][j] = 0
print(color_list[0])
#cv2.imshow("Over the Clouds", image)
#cv2.imshow("Over the Clouds - gray", gray_image)
x = cv2.Canny(image,50, 150)
cv2.imshow("edges", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
