import urllib.request
import datetime
import json
from config import *
service_key="3nDFWMx%2Fbj0C6u3pEHVsj6Tf52bsiyyeWfdZ0V%2FpAbG7QDY6YacCEadI1KKNowc%2BlsD7a7feD1QxgNWHk2QRgA%3D%3D"
#공공데이터 홈페이지에 일반 인증키(utf-8)


def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            print("[%s] Url Request Success " %datetime.datetime.now())
            return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


# ?_type=json&serviceKey=&pageNo=1&numOfRows=10&spclAdmTyCd=99
def getdata(pageno, numofrows, kinds):
    endPoint = "http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList"
   
 
    param = "?_type=json&serviceKey="+service_key
   
    param += "&pageNo=" + pageno
    #1
    param += "&numOfRows=" + numofrows
    #10
    param += "&spclAdmTyCd=" + kinds
    #99
    #A0=국민안심병원, 97=코로나검사실시기간, 99=코로나 선별진료소 운영기관
    url = endPoint + param
    print(url)
    retData = get_request_url(url)
    print(retData)
    if(retData == None):
        return None
      
    else :
        return json.loads(retData)
 

jsonResult=[]



pageno = '1'
numofrows = '10'
kinds = '99'

jsonData = getdata(pageno, numofrows, kinds)
print(jsonData)



if( jsonData['response']['header']['resultCode'] =='00'):
    for item in jsonData['response']['body']['items']['item']:
        date = item['adtFrDd']
        #날짜
        area = item['sidoNm']
        #시도
        name = item['yadmNm']
        #병원 이름
        print('지역=', area , ":",  '날짜=', date,":",'name=',name)
        jsonResult.append({'date': date,'area': area, 'name':name})
    

         
# # with open('hospital.json','w',encoding='utf8') as outfile:
# #     retJson = json.dumps(jsonResult, indent= 4, sort_keys=True, ensure_ascii=False)
# #     outfile.write(retJson)
   
