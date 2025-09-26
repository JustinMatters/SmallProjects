import base64
import qrcode

""" 
This script is designed to allow you to create a valid QR code
to create a TOTP code for Google Authenticator for offline ID
verification 
(eg to provide verification to avoid voice cloning phone scams)
All the people sharing the TOTP code should be able to verify 
codes with each other to confirm identities
"""

issuer = 'issuer' # must be URL safe
user = 'user' # must be URL safe

valid = False
while valid == False:
    secret = input('secret (needs to be base32 encodable): ')
    if len(secret) < 12 or len(secret) > 30:
        print('please use a string between 12 and 30 characters')
    else:
        try:
            secret_encode = secret.encode()
            print(secret_encode)
            b32_secret = base64.b32encode(secret_encode)
            print(b32_secret.decode())
            valid = True
        except:
            print('secret needs to be base32 encodable.')



totp_string = f'otpauth://totp/{issuer}:{user}?secret={b32_secret.decode()}&issuer={issuer}'
print(totp_string)

qr_code_maker = qrcode.QRCode(
    version=1, 
    box_size=10, 
    border=5, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qr_code_maker.add_data(totp_string)
qr_code_maker.make(fit=True)
img = qr_code_maker.make_image(fill_color="black", back_color="white")
img.show()
# you may not want to save for security reasons
# img.save("qrcode.png")

