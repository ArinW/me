import qrcode

img = qrcode.make("https://arinw.github.io/me/")
img.save("arin_qr.png")
