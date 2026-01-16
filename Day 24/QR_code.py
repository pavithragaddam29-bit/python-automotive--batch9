import qrcode

# Exact data to be encoded in the QR code
qr_data = (
    "Automotive Testing Batch-9\n\n"
    "Group 1\n"
    "Co-ordinator Name: Ritikesh\n"
    "Team Members: Abhishek, Lokesh, Sudha, Yamini, Pavithra"
)

# Create QR code
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4
)

qr.add_data(qr_data)
qr.make(fit=True)

# Generate QR image
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image
qr_img.save("Automotive_Testing_Batch_9_Group_1.png")

print("QR Code generated successfully.")
