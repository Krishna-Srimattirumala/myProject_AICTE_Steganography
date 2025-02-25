import cv2
import os
import string

img = cv2.imread("Screenshot2025-02-08.png") # Replace with the correct image path#image

msg = input("Enter secret message:")
password = input("Enter a passcode:")

print("Decryptionlength of the secret message:", len(msg))
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
    #print("c(i)=",c[i])

m = 0
n = 0
z = 0

for i in range(len(msg)):
    print("d[msg[i]]=",d[msg[i]])
    img[n, m, z] = d[msg[i]]
    print("img[n, m, z]=",img[n, m, z])
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows

