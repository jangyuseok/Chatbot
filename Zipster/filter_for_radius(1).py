import requests
import time

url_call = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'

headers = {"Authorization": "KakaoAK 9a1835d570021a39b3df8de1042d71bc"}
# input_file_name = 'D:\\frontend_workspace\\1_html_workspace\Crawlling\\naver_land_Yongsan_2y_220205_143812.txt'

output_file_main_name = 'test_radius_500_jongro_'+time.strftime('%Y%m%d_%H%M%S')+'.txt'
output_file_main = open(output_file_main_name, 'w', encoding = "utf-8")
output_file_main.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format('위도','경도','URL_NUM','주소','법정동','문화생활','판매시설','음식점'))
output_file_main.close()


# def fget_list():
#     input_file = open(input_file_name, "r", encoding = "utf-8")
#     input_text = input_file.read()
#     lines = input_text.splitlines()
#     lists=[]
    
#     for line in lines[:]:
#         elms = line.strip().split("\t")
#         latitude = elms[0]
#         longtitude = elms[1]
#         url_num = elms[11]
#         lists.append([latitude, longtitude, url_num])
#     return lists[1:]


def fwrite_land_main(latitude, longtitude, url_num, address, address_dong, total_culture, total_market, total_restaurant):
    output_file_main = open(output_file_main_name, "a", encoding="utf-8")
    output_file_main.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(latitude, longtitude, url_num, address, address_dong, total_culture, total_market, total_restaurant))
    return


def count(latitude, longtitude, radius, keywords):
    total=0
    for keyword in keywords:
        url = url_call.format(keyword)
        params = {
            'x' : longtitude, 
            'y' : latitude, 
            'radius' : radius}
        result = requests.get(url, params=params, headers=headers).json()
        count = result.get('meta').get('total_count')
        total += count
    return total


def adr(latitude, longtitude):
    url= 'https://dapi.kakao.com/v2/local/geo/coord2address.json?query={}'
    params={
        'x': longtitude,
        'y': latitude,
        'input_coord' : 'WGS84'
    }
    result = requests.get(url, params=params, headers=headers).json()['documents'][0]
    address = result.get('address').get('address_name')
    address_dong = result.get('address').get('region_3depth_name')
    return address, address_dong


def culture(latitude, longtitude, radius) :
    keywords = ['영화관', '전시장','공연장','공방']
    total = count(latitude, longtitude, radius, keywords)
    return total


def market(latitude, longtitude, radius) :
    keywords = ['시장','백화점','슈퍼']
    total = count(latitude, longtitude, radius, keywords)
    return total


def restaurant(latitude, longtitude, radius) :
    keywords = ['음식점','패스트푸드','술집']
    total = count(latitude, longtitude, radius, keywords)
    return total


def fcrawl_land_main(latitude, longtitude, url_num, radius):
    total_culture = culture(latitude, longtitude, radius)
    total_market = market(latitude, longtitude, radius)
    total_restaurant = restaurant(latitude, longtitude, radius)
    address = adr(latitude, longtitude)[0]
    address_dong = adr(latitude, longtitude)[1]
    fwrite_land_main(latitude, longtitude, url_num, address, address_dong, total_culture, total_market, total_restaurant)
    return 


# def fmain():
#     lists = fget_list()
#     for list in lists[0:]:
#         latitude = list[0]
#         longtitude = list[1]
#         url_num = list[2]
#         radius = 500     #300/400/500
#         fcrawl_land_main(latitude, longtitude, url_num, radius)
#         time.sleep(1)

# fmain()

radius = 500     #300/400/500 37.574499811446984, 126.98672948795792
latitude = 37.574499811446984
longtitude = 126.98672948795792
url_num = ''
total_culture = culture(latitude, longtitude, radius)


