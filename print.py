from escpos.printer import Usb

def send_raster_image_to_printer(image_path):
    # Initialize the printer
    p = Usb(0x04b8, 0x0e15, 0)

    # Print the image
    p.image(image_path)

    # Cut the paper
    p.cut()

# Example usage
image_path = 'path_to_your_greyscale_raster_image.bmp'
send_raster_image_to_printer(image_path)
