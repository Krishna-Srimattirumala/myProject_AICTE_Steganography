Problem Statement: In present internet world with increased cyber threats, it is very difficult to send secret codes. Current project addresses this issue of sending secret messages by hiding them in images or pictures.
Technology  used: Operating System: Windows 11 
                  Programming Language: Python ver 3.12.8
                  Python libraries: cv2, string, os
                  IDE: Visual Source Code
                  Git/GitHub as repository of the code 

Current project is divided into 2 python programs one for encryption ( stego-encrypt.py )and other for decryption (stego-encrypt.py), to send secret message by hiding it in an image.
Data sent offline by Sender to Receiver
        Password or key : 1234
        Length of the secret message: 5
        
Documentation of stego-encrypt.py:

The stego-encrypt.py file is a Python script that performs steganography by embedding a secret message into an image.

Imports:
cv2: OpenCV library for image processing.
os: Library for interacting with the operating system.
string: Library for string operations (though not used in this script).

Reading the Image:
The script reads an image named Screenshot2025-02-08.png using OpenCV's cv2.imread function. You need to replace "Screenshot2025-02-08.png" with the correct path to your image.

User Inputs:
The user is prompted to enter a secret message (msg) and a passcode (password).

Character Encoding:
Two dictionaries, d and c, are created to map characters to their ASCII values and vice versa. This is done for all characters with ASCII values from 0 to 254.

Embedding the Message:
The script iterates over each character in the secret message.
It encodes each character into the image by modifying the pixel values. Specifically, it changes the pixel values at positions (n, m, z) where n, m, and z are indices that are incremented in each iteration.
The pixel values are modified using the ASCII values of the characters from the secret message.

Saving the Encrypted Image:
The modified image is saved as encryptedImage.png.
The script then opens the encrypted image using the default image viewer on Windows with the os.system("start encryptedImage.png") command.


Documentation of stego-decrypt.py:

The stego-decrypt.py file is a Python script that performs the decryption part of steganography by extracting a hidden message from an image. 

Imports:
cv2: OpenCV library for image processing.
os: Library for interacting with the operating system.
string: Library for string operations (though not used in this script).

Predefined Password:
The script sets a predefined password (password = "1234") which will be used to authenticate the decryption process. This would be shared offline by the sender to receiver.

Reading the Encrypted Image:
The script reads an image named encryptedImage.png using OpenCV's cv2.imread function. This image is expected to contain the hidden message.

Character Encoding:
Two dictionaries, d and c, are created to map characters to their ASCII values and vice versa. This is done for all characters with ASCII values from 0 to 254.

Initializing Variables:
The variable message is initialized as an empty string to store the decrypted message.
The variables n, m, and z are initialized to 0. These will be used as indices to traverse the image pixels.

User Input for Passcode:
The user is prompted to enter a passcode for decryption (pas).

Authentication and Decryption:
The script checks if the entered passcode matches the predefined password.
If the passcode is correct, the script proceeds to extract the hidden message from the image:
It iterates over the pixels of the image, retrieving the ASCII values stored in the pixel values at positions (n, m, z).
These ASCII values are converted back to characters using the c dictionary and appended to the message string.
The indices n, m, and z are incremented in each iteration to move to the next pixel. This is done in a for loop for the length of the secret message ( shared offline by the Sender to receiver). Here it is 5.
The decrypted message is then printed.

Unauthorized Access:
If the entered passcode does not match the predefined password, the script prints "YOU ARE NOT auth" indicating that the user is not authorized to decrypt the message.
