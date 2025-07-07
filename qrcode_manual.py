#Importing QR Code library and its class config library
import qrcode
import qrcode.constants

#Declaring custom exception class to validate URL input
class HttpError(Exception):
    pass

#Custom function to validate URL input (https:// or www. or http://)
def validate_website(url):
    #Validating first case scenario: https/http + www
    if(url.split(".")[0] == "https://www" or url.split(".")[0] == "www" or url.split(".")[0] == "http://www"):
        pass
    #Second scenario: https/http
    elif(url.split("//")[0] == "https:" or url.split("//")[0] == "http:"):
        pass
    #Raising exception
    else:
        raise HttpError(url,"Website invalid")

if __name__ == "__main__":
    #Initializing QR Code class with its attributes
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 16,
        border = 4,
    )

    while True:
        #Listening URL from user input
        try:
            url = input('Type in the website to be converted to QR Code: ')

            #Validating URL to make sure it is a valid URL
            validate_website(url)
        except HttpError as e:
            message =  print('Website invalid, your input must include https or www')
        else:
            #Creating object QR Code
            qr.add_data(url)
            qr.make(fit=True)

            #Creating an image from the QR Code, showing and saving it
            img = qr.make_image(fill_color="black", back_color="white")
            img.show()
            img.save("manual_qrcode.png")
            break
    