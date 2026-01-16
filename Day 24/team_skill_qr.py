import qrcode

# -------------------------------
# TEAM SKILL MAP DATA (SPECIAL FORMAT)
# -------------------------------
team_skill_map = (
    "TEAM SKILL MAP – PROJECT GROUP\n\n"
    "[Requirement Analysis Node]\n"
    "• Ritikesh → Requirement Analyst\n"
    "• Expert in understanding and mapping project requirements\n\n"
    "[Design Node]\n"
    "• Abhishek → Visual Architect\n"
    "• Expert in creating flow charts\n\n"
    "[Content Node]\n"
    "• Lokesh → Content Strategist\n"
    "• Expert in creating content\n\n"
    "[Crisis Node]\n"
    "• Sudha → Situation Manager\n"
    "• Expert in handling situations\n\n"
    "[Knowledge Node]\n"
    "• Yamini → Concept Explainer\n"
    "• Expert in explanation\n\n"
    "[Technical Node]\n"
    "• Pavithra → Code Engineer\n"
    "• Expert in writing code"
)


# -------------------------------
# QR CODE GENERATION
# -------------------------------
qr = qrcode.QRCode(                                              #This object will store settings + data for the QR code.
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4
)

qr.add_data(team_skill_map)
qr.make(fit=True)

# -------------------------------
# SAVE QR CODE AS IMAGE
# -------------------------------
img = qr.make_image(fill_color="black", back_color="white")
img.save("team_skill_map.png")

print("QR Code generated successfully!")
print("Saved as: team_skill_map.png")
