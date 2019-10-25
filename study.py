from selenium import webdriver
from bs4 import BeautifulSoup

#크롬 드라이버 주소 C:\Users\Mark\Desktop\GitHub\driver
driver = webdriver.Chrome("C:/Users/Mark/Desktop/GitHub/driver/chromedriver.exe")
driver.get("http://www.gevolution.co.kr/rank/ios")
soup = BeautifulSoup(driver.page_source, "lxml")

i = 1
rawdata = []
# for data in soup.findAll(name="div", attrs={"class":"grp"}):
#     stripdata = data.text.strip()
#     rawdata = stripdata.split('\n')
#
#     print(str(i)+'위  : '+rawdata[0])
#     print(rawdata[1]+'\n')
#
#
#     #print(str(i)+"위 : "+data.text.strip())
#     i += 1
#     if i == 5:
#         break

j=1
k=1
for data in soup.findAll(name="div", attrs={"class":"grp"}):
    stripdata = data.text.strip()
    rawdata = stripdata.split('\n')

    if j == 1:
        print(str(k) + '위  : ' + rawdata[0])
        print(rawdata[1] + '\n')
        j += 1
        k += 1
    elif j % (3*k-2) == 0:
        print(str(k) + '위  : ' + rawdata[0])
        print(rawdata[1] + '\n')
        j += 1
        k += 1
    else:
        j += 1

    if k == 6:
        break
#4 7 10 13 16
