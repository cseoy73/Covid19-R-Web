import urllib.request
import datetime
import json
from config import *

#코로나19 시,도 발생현황

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            print("[%s] Url Request Success " %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None



def getdata(pageno, numofrows, yyyymmdd, eeeemmdd):
    endPoint = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    #&pageNo=1&numOfRows=10&startCreateDt=20200410&endCreateDt=20200410"
 
    param = "?_type=json&serviceKey="+service_key
   
    param += "&pageNo=" + pageno
    
    param += "&numOfRows=" + numofrows
    
    param += "&startCreateDt=" + yyyymmdd
  
    param += "&endCreateDt=" + eeeemmdd

    url = endPoint + param
 


    retData = get_request_url(url)
    if(retData == None):
        return None
      
    else :
        return json.loads(retData)
 





jsonResult=[]



pageno = '10'
numofrows = '10'


nStartYear = 2020

for year in range(nStartYear,  nStartYear+1):
    for month in range(6,7):
        for day in range(1,2):
            yyyymmdd = "{0}{1:0>2}{2:0>2}".format(str(year), str(month),str(day))
            eeeemmdd = "{0}{1:0>2}{2:0>2}".format(str(year), str(month),str(day))
            
            jsonData = getdata(pageno, numofrows, yyyymmdd, eeeemmdd)
            if( jsonData['response']['header']['resultMsg'] =='NORMAL SERVICE.'):
                
                
                for i in range(1,19):
                    area = jsonData['response']['body']['items']['item'][i]['gubun']
                    incDec = jsonData['response']['body']['items']['item'][i]['incDec']
                    
                    
                    print('지역=', area , ":",  '날짜=', yyyymmdd,":",'신규 확진자 수=',incDec)
                    jsonResult.append({'date': yyyymmdd,'area': area, 'incDec':incDec})

                
               
                

                #저장하는 방법
with open('covid2.json','w',encoding='utf8') as outfile:
    retJson = json.dumps(jsonResult, indent= 4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)
    # json 파일이든 csv 파일도 가능
    # 파일 생성됨 해외방문객 정보 어쩌고.json 파일로 
