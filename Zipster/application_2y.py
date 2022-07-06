from flask import Flask, request, jsonify
import sys
import numpy as np
import requests
import pandas as pd

application = Flask(__name__)

#전세, 구, 필터링
df = pd.read_csv('df_sc_month.csv')

def sort(gu, price, condition1, condition2, condition3):
    df_filter = df.loc[(df['지역구']==str(gu)) & (df['보증금']<=int(price))] #구, 보증금, 임대료 필터링   
    df_filter['score'] = df_filter[condition1]*1.4+df_filter[condition2]*1.2+df_filter[condition3] #선호환경 가중치
    df_dscending = df_filter.sort_values(by=['score'], ascending=False)[:15] 
    return df_dscending
 


@application.route("/")
@application.route('/home')
def home():
    return "''<h3>반갑습니다!</h3>''"

@application.route('/landrec_', methods = ['POST'])
def Landrec():
    
    content = request.get_json()
    gu = content["action"]["params"]["gu"]
    price = content["action"]["params"]["price"]
    condition1 = content["action"]["params"]["condition1"]
    condition2 = content["action"]["params"]["condition2"]
    condition3 = content["action"]["params"]["condition3"]

    answer = sort(gu, price, condition1, condition2, condition3)
    price = answer['보증금'].values
    dong = answer['법정동'].values
    area = answer['임대면적'].values
    url = answer['URL'].values
    #  url = df_dscending['URL'].values[0]
    # dong = df_dscending['법정동'].values[0]
    #분석이 정교해지려면 

    dataSend = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "carousel": {
              "type": "listCard",
              "items": [
            {            
                  "header": {
                    "title": "당신만을 위한 추천: 상위 5개 매물(Link)"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[0]),
                      "description": str(dong[0]) + "에 위치한 넓이 " + str(area[0]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[0])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[1]) + ", 월세 ",
                      "description": str(dong[1]) + "에 위치한 넓이 " + str(area[1]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[1])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[2]) + ", 월세 ",
                      "description": str(dong[2]) + "에 위치한 넓이 " + str(area[2]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[2])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[3]) + ", 월세 ",
                      "description": str(dong[3]) + "에 위치한 넓이 " + str(area[3]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[3])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[4]) + ", 월세 ",
                      "description": str(dong[4]) + "에 위치한 넓이 " + str(area[4]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[4])
                      }
                    }
                  ],
                  "buttons": [
                    {
                      "label": "네이버 부동산으로 이동",
                      "action": "webLink",
                      "webLinkUrl": "https://m.land.naver.com/"
                    }
                  ]
                },
          {            
                  "header": {
                    "title": "당신만을 위한 추천: 상위 10개 매물(Link)"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[5]) + ", 월세 ",
                      "description": str(dong[5]) + "에 위치한 넓이 " + str(area[5]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[5])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[6]) + ", 월세 ",
                      "description": str(dong[6]) + "에 위치한 넓이 " + str(area[6]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[6])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[7]) + ", 월세 ",
                      "description": str(dong[7]) + "에 위치한 넓이 " + str(area[7]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[7])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[8]) + ", 월세 ",
                      "description": str(dong[8]) + "에 위치한 넓이 " + str(area[8]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[8])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[9]) + ", 월세 ",
                      "description": str(dong[9]) + "에 위치한 넓이 " + str(area[9]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[9])
                      }
                    }
                  ],
                },
              {            
                  "header": {
                    "title": "당신만을 위한 추천: 상위 15개 매물(Link)"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[10]) + ", 월세 ",
                      "description": str(dong[10]) + "에 위치한 넓이 " + str(area[10]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[10])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[11]) + ", 월세 ",
                      "description": str(dong[11]) + "에 위치한 넓이 " + str(area[11]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[11])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[12]) + ", 월세 ",
                      "description": str(dong[12]) + "에 위치한 넓이 " + str(area[12]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[12])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[13]) + ", 월세 ",
                      "description": str(dong[13]) + "에 위치한 넓이 " + str(area[13]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[13])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[14]) + ", 월세 ",
                      "description": str(dong[14]) + "에 위치한 넓이 " + str(area[14]) + "m² 매물입니다. Click🔍",
                      "link": {
                        "web": str(url[14])
                      }
                    }
                  ]
                }
              ]    
            }
          }   
        ]
      }
    }
    return jsonify(dataSend)



if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)