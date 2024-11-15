import cv2
import glob

# leer las imágenes con glob, cargarlas con cv2
images = [cv2.imread(file) for file in glob.glob("./images/*.jpg")]
count = 1

# redimensionarlas y guardarlas en un nuevo folder
for img in images:
    resized = cv2.resize(img, (100, 100))
    
    # mostrar la imagen
    cv2.imshow("Hey", resized)
    
    # cerrar la ventana al presionar una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # guardar la nueva imagen
    cv2.imwrite(f"./resources/new{count}.jpg", resized)
    count += 1