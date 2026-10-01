import numpy as np
import cv2
# Vision Artificia Act 10 NC 0032
# Lee la imagen en escala de grises
img = cv2.imread("jojos parte 5.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("jojos 0032", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea
print("La linea 0032")
import numpy as np
import cv2

# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("Linea", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

# Abre la ventana con la imagen
cv2.imshow("El circulo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Giorno... volví a la vida. Mi alma estaba destinada a morir lentamente, pero revivió gracias a ti.", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

# Abre la ventana con la imagen
cv2.imshow("El texto", img)
cv2.waitKey(0)
cv2.destroyAllWindows()