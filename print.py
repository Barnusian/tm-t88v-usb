from escpos.printer import Usb

# Define USB Vendor ID and Product IDs for both models
vendor_id = 0x04b8  # Epson's Vendor ID
t88v = 0x0e15       # TM-T88V Product ID
t88iv = 0x0202      # TM-T88IV Product ID

# Select the printer model you are using
printer = Usb(vendor_id, t88v)  # Change to t88iv if using TM-T88IV

# Print some text
printer.text("Hello from the Epson TM-T88V!\n")

# Print a raster image
printer.image("your_image.png")

# Cut the receipt
printer.cut()