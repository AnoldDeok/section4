import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#다운로드 url
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
savename = "D:/PythonData/section4/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)
    print("다운로드 완료")

#BeautifulSoup 파싱
xml = open(savename,'r',encoding="utf-8").read()
soup = BeautifulSoup(xml,"html.parser")

#지역확인
info = {}
for location in soup.find_all("location"):
    loc = location.find("city").string
    weather = location.find_all("tmn")
    if not (loc in info): #지역명 중복처리
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
#print(info)
#print(info.keys())

#각 지역별 날씨 텍스트 쓰기
with open('D:/PythonData/section4/forecast.txt','wt') as f:
    for loc in sorted(info.keys()):
        print("+",loc)
        f.write(str(loc)+"\n")
        for n in info[loc]:
            print("-",n)
            f.write('\t'+str(n)+'\n')
