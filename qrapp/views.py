import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
import base64

def home(request):
    qr_image_data = None  # Initialize variable to hold the QR code image
    download_data = None  # Initialize variable for Base64 encoded data for download
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)

            # Convert image to Base64 for rendering and downloading
            qr_image_data = base64.b64encode(buffer.getvalue()).decode()
            download_data = qr_image_data

    return render(request, "home.html", {"qr_image_data": qr_image_data, "download_data": download_data})