# make function - for creating  qrcode 
# save function - converts qrcode into image formate 
import qrcode 
from PIL import Image # PIL is a module in python library called pillow


qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=5)
# QRcode is a class in qrcode library having above parameters.
# version - an integer meant to control size of QR code - smallest is version 1 21*21 matrix
# error_correction : has low,medium,high levels which controls error correction used in QRcode like overlapping of borders,etc
# box-size : controls no. of many pixels each box of qrcode has

qr.add_data("https://www.google.com/")
qr.make(fit=True) # ensures entire dimension of qrcode is utilized even when our data can fir in smaller boxes
img=qr.make_image(fill_color="pink",black_color="red")
img.save("Google_Qrcode.png")