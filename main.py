__author__ = 'PocketJacks74'

from urllib2 import Request, urlopen
from PyPDF2 import PdfFileWriter, PdfFileReader
from StringIO import StringIO
import pandas as pd
from bs4 import BeautifulSoup
import math
import re

df_date = pd.read_csv('FOMC_Dates_modified.csv')
url = "http://www.federalreserve.gov"
df_date['NLP']=0
#pattern_list=['<P>(.*)</P>','<P>(.*)','<p>(.*)</p>','<p>(.*)']

for i, filename in enumerate(df_date.url):
        if pd.isnull(filename):
                print str(i) + 'th record is not availale'
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
        else:
                if filename[:4] == 'http':
                        remoteFile = BeautifulSoup(urlopen(Request(filename)).read())
                else:
                        remoteFile = BeautifulSoup(urlopen(Request(url + filename)).read())
                #print filename
                pagelist = []
                m=remoteFile.find_all('p')
                for m_sub in m:
                        pagelist = pagelist + m_sub.get_text().split()
                df_date['NLP'].iloc[i] = pagelist
                #print pagelist






