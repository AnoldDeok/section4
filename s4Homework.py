import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4146125000"
savename = "D:/PythonData/section4/yongin.xml"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)
    print("다운로드 완료")

xml = open(savename,'r',encoding="utf-8").read()
soup = BeautifulSoup(xml,"html.parser")

i=0
list={}
for b in soup.find_all("hour"):
    list[b.string]=[]
    list[b.string].append(soup.find_all("temp")[i].string)
    i=i+1

with open('D:/PythonData/section4/yongin.txt','wt') as f:
    for a in list.keys():
        f.write(a)
        for dd in list[a]:
            f.write("\t"+dd+'\n')
