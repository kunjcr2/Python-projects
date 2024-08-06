import qrcode
from PIL import Image
import qrcode.constants

# Alternate way and easier one

# img = qr.make("URL goes here")
# img.save("name of the image goes here")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("URL goes here")
qr.make(fit=True)

img = qr.make_image()
img.save("name of the image goes here")
