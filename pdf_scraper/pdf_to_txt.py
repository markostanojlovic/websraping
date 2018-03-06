# python3 
# requirements : 
# sudo pip3 install pdfminer2
# sudo pip3 install chardet

import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys

def print_usage():
    print("""
        Usage: python3 pdf_to_txt.py arg1 [arg2]

        arg1 - path to the pdf file 
        arg2 - output txt file path 
        """)

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

try:
    text = convert_pdf_to_txt(sys.argv[1])
except (FileNotFoundError, IndexError):
    err_msg = '*** ERROR: File not found! ***\n'
    print_usage()
    sys.exit(err_msg)

try: 
    output_file_name = sys.argv[2]
except IndexError:
    output_file_name = sys.argv[1]+'.txt'

output_file = open(output_file_name, "w")
output_file.write(text)
output_file.close()

