__author__ = 'PocketJacks74'

from urllib2 import Request, urlopen
from PyPDF2 import PdfFileWriter, PdfFileReader
from StringIO import StringIO
import pandas as pd
import math

df_date = pd.read_csv('FOMC_Dates.csv')
url = "http://www.federalreserve.gov"
df_date['NLP']=0
for i, filename in enumerate(df_date.url):
        if filename=='nan':
                pass
        elif filename[-3:] == 'pdf':
                remoteFile = urlopen(Request(url + filename)).read()
                memoryFile = StringIO(remoteFile)
                pdfFile = PdfFileReader(memoryFile)
                pagelist = []
                for pageNum in xrange(pdfFile.getNumPages()):
                        currentPage = pdfFile.getPage(pageNum)
                        myText = currentPage.extractText()
                        thispage = myText.split()
                        pagelist = pagelist + thispage
                df_date['NLP'].iloc[i] = pagelist



