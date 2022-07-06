import requests
import json
import time

# url = "https://m.land.naver.com/cluster/ajax/articleList?itemId=&mapKey=&lgeo=&showR0=&rletTpCd=APT%3AOPST%3AVL%3AJWJT%3ADDDGG%3AOR&tradTpCd=B2&z=13&lat=37.585677&lon=126.9774064&btm=37.5170174&lft=126.9110593&top=37.6542734&rgt=127.0437535&wprcMax=20000&tag=NOLOAN&totCnt=471&cortarNo=1111000000&sort=rank&page=1"
# #현재 조건 서울시 종로구 월세 아파트 오피스텔 빌라 전원주택 단독 다가구 원룸 보증금 2억이하 융자금 없는 
# payload={}
# headers = {
#   'Accept': 'application/json, text/javascript, */*; q=0.01',
#   'Accept-Encoding': 'gzip, deflate, br',
#   'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#   'Cache-Control': 'no-cache',
#   'Connection': 'keep-alive',
#   'Cookie': 'NNB=3XA4MUUX6XTWC; nx_ssl=2; _ga=GA1.2.1671714194.1643178208; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; SHOW_FIN_BADGE=Y; MM_NEW=1; NFS=2; landHomeFlashUseYn=Y; realestate.beta.lastclick.cortar=1111000000; HT=HM; BMR=s=1643531106868&r=https%3A%2F%2Fm.blog.naver.com%2Fvwjdalsgkv%2F222370775182%3Ffbclid%3DIwAR0gTPKKqNxeb7LN45X9c342bPfF0MJbiIB1Lq6D3JT__WfBYPotub-LUco&r2=https%3A%2F%2Fwww.google.com%2F; JSESSIONID=7D232CBF9C33EF106024C52CC8D1842D; REALESTATE=1643532801987; wcs_bt=44058a670db444:1643532855; REALESTATE=1643528692942',
#   'Host': 'm.land.naver.com',
#   'Pragma': 'no-cache',
#   'Referer': 'https://m.land.naver.com/',
#   'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'Sec-Fetch-Dest': 'empty',
#   'Sec-Fetch-Mode': 'cors',
#   'Sec-Fetch-Site': 'same-origin',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#   'X-Requested-With': 'XMLHttpRequest'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

# response = requests.request("GET", url, headers=headers, data=payload)
# elements = json.loads(response.text)['body']

# for element in elements:
#     articleNo = element['atclNo']
#     print(articleNo)
#     url = 'https://m.land.naver.com/article/info/'+ articleNo #해당 매물 url
#     print(url)
# ------------------------------------------------------------------------------------------------------------
def fmake_file():
  output_file_name = 'naver_land_guro_2y_' + time.strftime("%y%m%d_%H%M%S") + '.txt'
  output_file = open(output_file_name, "w", encoding="utf-8")
  output_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format('위도','경도','주소','층_raw','임대건물코드','임대건물명','임대면적','전월세구분코드','전월세구분','보증금','임대료', 'URL_NUM'))
  output_file.close()
  return output_file_name


def fwrite_land(i, lat, lng, adr, flrInfo, rletTpNmCode, rletTpNm, spc1, tradTpNmCode, tradTpNm, prc, rentPrc, atclNo, output_file_name):
  output_file = open(output_file_name, "a", encoding="utf-8")
  output_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(lat, lng, adr, flrInfo, rletTpNmCode, rletTpNm , spc1, tradTpNmCode , tradTpNm, prc, rentPrc, atclNo))
  output_file.close()
  return


def fcrawl_land(i, output_file_name):
  time.sleep(1)
  url = "https://m.land.naver.com/cluster/ajax/articleList?itemId=&mapKey=&lgeo=&showR0=&rletTpCd=APT%3AOPST%3AVL%3AJWJT%3ADDDGG%3AOR&tradTpCd=B1&z=12&lat=37.49551&lon=126.887532&btm=37.3710593&lft=126.7759521&top=37.6197537&rgt=126.9991119&wprcMax=20000&totCnt=873&cortarNo=1153000000&sort=rank&page="+str(i)
  # url = "https://m.land.naver.com/cluster/ajax/articleList?itemId=&mapKey=&lgeo=&showR0=&rletTpCd=APT%3AOPST%3AVL%3AJWJT%3ADDDGG%3AOR&tradTpCd=B1%3AB2&z=12&lat=37.5874&lon=127.020729&btm=37.4697786&lft=126.8971328&top=37.7048359&rgt=127.1443252&wprcMax=20000&totCnt=2441&cortarNo=1129000000&sort=rank&page="+str(i)
  payload={}
  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'NNB=3XA4MUUX6XTWC; nx_ssl=2; _ga=GA1.2.1671714194.1643178208; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; SHOW_FIN_BADGE=Y; MM_NEW=1; NFS=2; landHomeFlashUseYn=Y; realestate.beta.lastclick.cortar=1111000000; HT=HM; BMR=s=1643531106868&r=https%3A%2F%2Fm.blog.naver.com%2Fvwjdalsgkv%2F222370775182%3Ffbclid%3DIwAR0gTPKKqNxeb7LN45X9c342bPfF0MJbiIB1Lq6D3JT__WfBYPotub-LUco&r2=https%3A%2F%2Fwww.google.com%2F; JSESSIONID=7D232CBF9C33EF106024C52CC8D1842D; REALESTATE=1643532801987; wcs_bt=44058a670db444:1643532855; REALESTATE=1643528692942',
    'Host': 'm.land.naver.com',
    'Pragma': 'no-cache',
    'Referer': 'https://m.land.naver.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  elements = json.loads(response.text)['body']

  results = []
  for element in elements:
    lat = element['lat']
    lng = element['lng']
    adr =''
    try:
      flrInfo = element['flrInfo']
    except:
      flrInfo = ''
    rletTpNmCode ='' 
    rletTpNm = element['rletTpNm']
    spc1 = element['spc1']
    tradTpNmCode =''
    tradTpNm = element['tradTpNm']
    prc = element['prc']
    rentPrc = element['rentPrc']
    atclNo = element['atclNo']


    # news_title_clean = news_title.replace("\n", "").replace("\t", "").replace("\r", "").strip()
    results.append([i, lat, lng, adr, flrInfo, rletTpNmCode, rletTpNm, spc1, tradTpNmCode, tradTpNm, prc, rentPrc, atclNo])
    fwrite_land(i, lat, lng, adr, flrInfo, rletTpNmCode, rletTpNm, spc1, tradTpNmCode, tradTpNm, prc, rentPrc, atclNo, output_file_name)
  return results


def fmain():
  output_file_name = fmake_file()
  for i in range(1,46):
    results = fcrawl_land(i, output_file_name)
   
    time.sleep(6)

fmain()