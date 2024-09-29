import qrcode as qr

text = input("Enter Text or Link To Conert into QR Code : ")


img = qr.make(text)
img.save("QR.png")