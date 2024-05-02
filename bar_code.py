from barcode import EAN13
from barcode.writer import ImageWriter

number = '5901432115697'
generated_barcode = EAN13(number,writer=ImageWriter())
generated_barcode.save("bar-code")
