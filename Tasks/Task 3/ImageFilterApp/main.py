import cv2

img = cv2.imread("REBEL.jpg")

if img is None:
    print("Image not found!")
    exit()

print("Choose Filter:")
print("1 - Grayscale")
print("2 - Blur")
print("3 - Cartoon")

choice = input("Enter choice: ")

if choice == "1":
    output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.jpg", output)
    cv2.imshow("Grayscale", output)

elif choice == "2":
    output = cv2.GaussianBlur(img, (15,15), 0)
    cv2.imwrite("blur.jpg", output)
    cv2.imshow("Blur", output)

elif choice == "3":

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray_blur = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(
        gray_blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    color = cv2.bilateralFilter(img, 9, 250, 250)

    output = cv2.bitwise_and(color, color, mask=edges)

    cv2.imwrite("cartoon.jpg", output)
    cv2.imshow("Cartoon", output)

else:
    print("Invalid choice!")

cv2.waitKey(0)
cv2.destroyAllWindows()