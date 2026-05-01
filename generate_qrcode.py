#!/usr/bin/env python3
"""
Generate a QR code for 'Vodafone Agentic Commerce' text.
This script creates a QR code image and saves it as 'vodafone_qrcode.png'.
"""

import qrcode

def generate_qrcode(text, output_filename):
    """
    Generate a QR code image from the given text.
    
    Args:
        text (str): The text to encode in the QR code
        output_filename (str): The filename to save the QR code image to
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(output_filename)
    print(f"✓ QR code generated successfully: {output_filename}")

if __name__ == "__main__":
    # Generate QR code for 'Vodafone Agentic Commerce'
    text = "Vodafone Agentic Commerce"
    output_file = "vodafone_qrcode.png"
    
    generate_qrcode(text, output_file)
