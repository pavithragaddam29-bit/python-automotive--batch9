import qrcode

form_url ="https://docs.google.com/forms/d/e/1FAIpQLSdf-RlgXNNO4lU9bXaz58U3lXwISR9lWJyrxgH4F3p8v58IWQ/viewform?usp=dialog"

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4
)

qr.add_data(form_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("student_form_qr.png")

print("QR created successfully")
print("Scan QR to fill the form")
