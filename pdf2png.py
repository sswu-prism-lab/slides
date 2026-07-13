import pymupdf

PDF_PATH = "C:/Users/dwigh/slides/images/general/"

for i in range(12, 13):
    FILENAME = PDF_PATH + "fig" + str(i) + ".pdf"
    OUTPUT_PATH = PDF_PATH + "fig" + str(i) + ".png"
    doc = pymupdf.open(FILENAME)[0]
    pix = doc.get_pixmap(dpi=500)
    pix.save(OUTPUT_PATH)