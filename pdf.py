import PyPDF2

template = PyPDF2.PdfReader(open('dummy.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

with open('watermarked_output.pdf', 'wb') as file:
    for i in range(len(template.pages)):
        page = template.pages[i]
        watermark_page = watermark.pages[i % len(watermark.pages)]
        page.merge_page(watermark_page)
        output.add_page(page)

    output.write(file)
