import cv2

# cargar imagen
img = cv2.imread("./Perfil.jpg", 0)

print(type(img))
print(img.shape) # size
print(img.ndim)

# mostrar imagen
cv2.imshow("Perfil", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# si quieres redimensionar la imagen
resized_image = cv2.resize(img, (1000, 500))
cv2.imshow("Redimension", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()