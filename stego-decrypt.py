import cv2
import os
import string

password="1234"
imgd = cv2.imread("encryptedImage.png")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    #for i in range(len(msg)):
    for i in range(5):
        print("img[n, m, z]=",imgd[n, m, z])
        print("c[img[n, m, z]]=",c[imgd[n, m, z]])
        message = message + c[imgd[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")