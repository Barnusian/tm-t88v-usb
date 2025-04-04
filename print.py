import usb.core
import usb.util

def send_raster_image_to_printer(image_path):
    # Find the Epson TM-T88V printer (Vendor ID: 0x04b8, Product ID: 0x0e15)
    printer = usb.core.find(idVendor=0x04b8, idProduct=0x0e15)

    if printer is None:
        raise ValueError("Printer not found. Please ensure the printer is connected and turned on.")

    # Set the active configuration
    printer.set_configuration()

    # Open the image file in binary mode
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()

    # Send the raster image data to the printer
    printer.write(1, img_data)

# Example usage
image_path = 'path_to_your_greyscale_raster_image.bmp'
send_raster_image_to_printer(image_path)
