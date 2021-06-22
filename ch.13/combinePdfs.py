#! python 3
#combinePdfs.py - Combines all the PDFs in the current working directory into
# a single pdf

import PyPDF2, os

#get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#TODO: Loop thorugh all the PDF files.
    for pageNum in range(1, pdfReader.numPages):
              pageObj = pdfReader.getPage(pageNum)
              pdfWriter.addPage(pageObj)

#TODO: Loop thorugh all the pages (except the first) and add them


#TODO: Save the resulting PDF to a file.

              
