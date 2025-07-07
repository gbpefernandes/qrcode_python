import qrcode
import re
import os
from urllib.parse import urlparse
from PIL import Image

def is_valid_url(url):
    # Basic URL validation
    parsed = urlparse(url)
    return all([parsed.scheme in ("http", "https"), parsed.netloc])

def main():
    while True:
        url = input("Enter a URL: ").strip()
        if is_valid_url(url):
            break
        print("Invalid URL. Please enter a valid URL (starting with http:// or https://).")

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Show the image
    img.show()

    # Save the image in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = "lowcode_qrcode.png"
    save_path = os.path.join(script_dir, filename)
    img.save(save_path)
    print(f"QR code saved as {save_path}")

if __name__ == "__main__":
    main()