__author__ = 'PocketJacks74'

from urllib2 import Request, urlopen
from PyPDF2 import PdfFileWriter, PdfFileReader
from StringIO import StringIO

url = "http://www.federalreserve.gov/monetarypolicy/files/fomcmoa19800109.pdf"
writer = PdfFileWriter()

remoteFile = urlopen(Request(url)).read()
memoryFile = StringIO(remoteFile)
pdfFile = PdfFileReader(memoryFile)

# initialize page list

pagelist = []
for pageNum in xrange(pdfFile.getNumPages()):
        currentPage = pdfFile.getPage(pageNum)
        myText = currentPage.extractText()
        thispage = myText.split()
        pagelist = pagelist + thispage

print len(pagelist)
