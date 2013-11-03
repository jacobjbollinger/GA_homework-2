import pyPdf

def get_text(path):
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    content = ""
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + "\n"  # Extract text from page and add to content
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content
    