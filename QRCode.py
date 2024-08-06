import qrcode
from PIL import Image
import qrcode.constants

# Alternate way and easier one

# img = qr.make("https://www.instagram.com/kunj.cr2/")
# img.save("ig@kunj.cr2.png")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://www.instagram.com/kunj.cr2/")
qr.make(fit=True)

img = qr.make_image()
img.save("ig@kunj.cr2.png")