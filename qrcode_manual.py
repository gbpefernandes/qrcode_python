import qrcode
import qrcode.constants

class HttpError(Exception):
    pass

def validate_website(url):
    if(url.split(".")[0] == "https://www" or url.split(".")[0] == "www" or url.split(".")[0] == "http://www"):
        pass
    else:
        raise HttpError(url,"Website invalid")

if __name__ == "__main__":
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 16,
        border = 4,
    )

    while True:
        try:
            url = input('Type in the website to be converted to QR Code: ')
            validate_website(url)
        except HttpError as e:
            message =  print('Website invalid, your input must include https or www')
        else:
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            print(type(img))
            img.show()
            break
    