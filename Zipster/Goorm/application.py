from flask import Flask, request, jsonify
import sys
import numpy as np
import requests
import pandas as pd
from combineLand import*

application = Flask(__name__)


@application.route("/")

@application.route('/landrec_month', methods = ['POST'])
def Landrec_month():
    
    content = request.get_json()
    gu = content["action"]["params"]["gu"]
    price = content["action"]["params"]["price"]
    rentPrice = content["action"]["params"]["rentPrice"]
    condition1 = content["action"]["params"]["condition1"]
    condition2 = content["action"]["params"]["condition2"]
    condition3 = content["action"]["params"]["condition3"]

    answer = sort_month(gu, price, rentPrice, condition1, condition2, condition3)
    price = answer['보증금'].values
    rentPrice = answer['임대료'].values
    dong = answer['법정동'].values
    area = answer['임대면적'].values
    url = answer['URL'].values


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
                    "title": "당신만을 위한 추천: 상위 5개 매물"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[0]) + ", 월세 " + str(rentPrice[0]),
                      "description": str(dong[0]) + "에 위치한 넓이 " + str(area[0]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[0])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[1]) + ", 월세 " + str(rentPrice[1]),
                      "description": str(dong[1]) + "에 위치한 넓이 " + str(area[1]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[1])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[2]) + ", 월세 " + str(rentPrice[2]),
                      "description": str(dong[2]) + "에 위치한 넓이 " + str(area[2]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[2])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[3]) + ", 월세 " + str(rentPrice[3]),
                      "description": str(dong[3]) + "에 위치한 넓이 " + str(area[3]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[3])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[4]) + ", 월세 " + str(rentPrice[4]),
                      "description": str(dong[4]) + "에 위치한 넓이 " + str(area[4]) + "m² 매물 Click🔍",
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
                      "title": "🏠 보증금 " + str(price[5]) + ", 월세 " + str(rentPrice[5]),
                      "description": str(dong[5]) + "에 위치한 넓이 " + str(area[5]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[5])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[6]) + ", 월세 " + str(rentPrice[6]),
                      "description": str(dong[5]) + "에 위치한 넓이 " + str(area[6]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[6])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[7]) + ", 월세 " + str(rentPrice[7]),
                      "description": str(dong[7]) + "에 위치한 넓이 " + str(area[7]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[7])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[8]) + ", 월세 " + str(rentPrice[8]),
                      "description": str(dong[8]) + "에 위치한 넓이 " + str(area[8]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[8])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[9]) + ", 월세 " + str(rentPrice[9]),
                      "description": str(dong[9]) + "에 위치한 넓이 " + str(area[9]) + "m² 매물 Click🔍",
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
                      "title": "🏠 보증금 " + str(price[10]) + ", 월세 " + str(rentPrice[10]),
                      "description": str(dong[10]) + "에 위치한 넓이 " + str(area[10]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[10])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[11]) + ", 월세 " + str(rentPrice[11]),
                      "description": str(dong[11]) + "에 위치한 넓이 " + str(area[11]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[11])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[12]) + ", 월세 " + str(rentPrice[12]),
                      "description": str(dong[12]) + "에 위치한 넓이 " + str(area[12]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[12])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[13]) + ", 월세 " + str(rentPrice[13]),
                      "description": str(dong[13]) + "에 위치한 넓이 " + str(area[13]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[13])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[14]) + ", 월세 " + str(rentPrice[14]),
                      "description": str(dong[14]) + "에 위치한 넓이 " + str(area[14]) + "m² 매물 Click🔍",
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


@application.route('/landrec_2y', methods = ['POST'])
def Landrec_2y():
    
    content = request.get_json()
    gu = content["action"]["params"]["gu"]
    price = content["action"]["params"]["price"]
    condition1 = content["action"]["params"]["condition1"]
    condition2 = content["action"]["params"]["condition2"]
    condition3 = content["action"]["params"]["condition3"]

    answer = sort_2y(gu, price, condition1, condition2, condition3)
    price = answer['보증금'].values
    dong = answer['법정동'].values
    area = answer['임대면적'].values
    url = answer['URL'].values


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
                    "title": "당신만을 위한 추천: 상위 5개 매물"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[0]),
                      "description": str(dong[0]) + "에 위치한 넓이 " + str(area[0]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[14])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[1]), 
                      "description": str(dong[1]) + "에 위치한 넓이 " + str(area[1]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[1])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[2]),
                      "description": str(dong[2]) + "에 위치한 넓이 " + str(area[2]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[2])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[3]), 
                      "description": str(dong[3]) + "에 위치한 넓이 " + str(area[3]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[3])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[4]), 
                      "description": str(dong[4]) + "에 위치한 넓이 " + str(area[4]) + "m² 매물 Click🔍",
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
                      "title": "🏠 보증금 " + str(price[5]), 
                      "description": str(dong[5]) + "에 위치한 넓이 " + str(area[5]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[5])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[6]), 
                      "description": str(dong[5]) + "에 위치한 넓이 " + str(area[6]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[6])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[7]), 
                      "description": str(dong[7]) + "에 위치한 넓이 " + str(area[7]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[7])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[8]), 
                      "description": str(dong[8]) + "에 위치한 넓이 " + str(area[8]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[8])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[9]), 
                      "description": str(dong[9]) + "에 위치한 넓이 " + str(area[9]) + "m² 매물 Click🔍",
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
                      "title": "🏠 보증금 " + str(price[10]), 
                      "description": str(dong[10]) + "에 위치한 넓이 " + str(area[10]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[10])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[11]), 
                      "description": str(dong[11]) + "에 위치한 넓이 " + str(area[11]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[11])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[12]), 
                      "description": str(dong[12]) + "에 위치한 넓이 " + str(area[12]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[12])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[13]), 
                      "description": str(dong[13]) + "에 위치한 넓이 " + str(area[13]) + "m² 매물 Click🔍",
                      "link": {
                        "web": str(url[13])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[14]), 
                      "description": str(dong[14]) + "에 위치한 넓이 " + str(area[14]) + "m² 매물 Click🔍",
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


@application.route('/landrec_jongro_month', methods = ['POST'])
def Landrec_jongro_month():
    
    content = request.get_json()
    price = content["action"]["params"]["price"]
    rentPrice = content["action"]["params"]["rentPrice"]
    condition1 = content["action"]["params"]["condition1"]
    condition2 = content["action"]["params"]["condition2"]
    condition3 = content["action"]["params"]["condition3"]

    answer = sort_jongro_month(price, rentPrice, condition1, condition2, condition3)
    price = answer['보증금'].values
    rentPrice = answer['임대료'].values
    dong = answer['법정동'].values
    area = answer['임대면적'].values
    urlNum = answer['URL_NUM'].values
    predict = answer['예측값'].values


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
                    "title": "당신만을 위한 추천: 상위 5개 매물"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[0]) + ", 월세 " + str(rentPrice[0]) + " Click🔍" ,
                      "description": str(dong[0]) + ", 면적: " + str(area[0]) + "m², 예측 월세: " + str(int(predict[0])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[0])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[1]) + ", 월세 " + str(rentPrice[1]) + " Click🔍" ,
                      "description": str(dong[1]) + ", 면적: " + str(area[1]) + "m², 예측 월세: " + str(int(predict[1])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[1])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[2]) + ", 월세 " + str(rentPrice[2]) + " Click🔍" ,
                      "description": str(dong[2]) + ", 면적: " + str(area[2]) + "m², 예측 월세: " + str(int(predict[2])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[2])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[3]) + ", 월세 " + str(rentPrice[3]) + " Click🔍" ,
                      "description": str(dong[3]) + ", 면적: " + str(area[3]) + "m², 예측 월세: " + str(int(predict[3])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[3])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[4]) + ", 월세 " + str(rentPrice[4]) + " Click🔍" ,
                      "description": str(dong[4]) + ", 면적: " + str(area[4]) + "m², 예측 월세: " + str(int(predict[4])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[4])
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
                      "title": "🏠 보증금 " + str(price[5]) + ", 월세 " + str(rentPrice[5]) + " Click🔍" ,
                      "description": str(dong[5]) + ", 면적: " + str(area[5]) + "m², 예측 월세: " + str(int(predict[5])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[5])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[6]) + ", 월세 " + str(rentPrice[6]) + " Click🔍" ,
                      "description": str(dong[6]) + ", 면적: " + str(area[6]) + "m², 예측 월세: " + str(int(predict[6])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[6])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[7]) + ", 월세 " + str(rentPrice[7]) + " Click🔍" ,
                      "description": str(dong[7]) + ", 면적: " + str(area[7]) + "m², 예측 월세: " + str(int(predict[7])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[7])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[8]) + ", 월세 " + str(rentPrice[8]) + " Click🔍" ,
                      "description": str(dong[8]) + ", 면적: " + str(area[8]) + "m², 예측 월세: " + str(int(predict[8])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[8])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[9]) + ", 월세 " + str(rentPrice[9]) + " Click🔍" ,
                      "description": str(dong[9]) + ", 면적: " + str(area[9]) + "m², 예측 월세: " + str(int(predict[9])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[9])
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
                      "title": "🏠 보증금 " + str(price[10]) + ", 월세 " + str(rentPrice[10]) + " Click🔍" ,
                      "description": str(dong[10]) + ", 면적: " + str(area[10]) + "m², 예측 월세: " + str(int(predict[10])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[10])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[11]) + ", 월세 " + str(rentPrice[11]) + " Click🔍" ,
                      "description": str(dong[11]) + ", 면적: " + str(area[11]) + "m², 예측 월세: " + str(int(predict[11])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[11])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[12]) + ", 월세 " + str(rentPrice[12]) + " Click🔍" ,
                      "description": str(dong[12]) + ", 면적: " + str(area[12]) + "m², 예측 월세: " + str(int(predict[12])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[12])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[13]) + ", 월세 " + str(rentPrice[13]) + " Click🔍" ,
                      "description": str(dong[13]) + ", 면적: " + str(area[13]) + "m², 예측 월세: " + str(int(predict[13])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[13])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[14]) + ", 월세 " + str(rentPrice[14]) + " Click🔍" ,
                      "description": str(dong[14]) + ", 면적: " + str(area[14]) + "m², 예측 월세: " + str(int(predict[14])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[14])
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


@application.route('/landrec_jongro_2y', methods = ['POST'])
def Landrec_jongro_2y():
    
    content = request.get_json()
    price = content["action"]["params"]["price"]
    condition1 = content["action"]["params"]["condition1"]
    condition2 = content["action"]["params"]["condition2"]
    condition3 = content["action"]["params"]["condition3"]

    answer = sort_jongro_2y(price, condition1, condition2, condition3)
    price = answer['보증금'].values
    dong = answer['법정동'].values
    area = answer['임대면적'].values
    urlNum = answer['URL_NUM'].values
    predict = answer['예측값'].values


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
                    "title": "당신만을 위한 추천: 상위 5개 매물"
                  },
                  "items": [
                    {
                      "title": "🏠 보증금 " + str(price[0]) + " Click🔍" ,
                      "description": str(dong[0]) + ", 면적: " + str(area[0]) + "m², 예측 보증금: " + str(int(predict[0])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[0])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[1]) + " Click🔍" ,
                      "description": str(dong[1]) + ", 면적: " + str(area[1]) + "m², 예측 보증금: " + str(int(predict[1])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[1])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[2]) + " Click🔍" ,
                      "description": str(dong[2]) + ", 면적: " + str(area[2]) + "m², 예측 보증금: " + str(int(predict[2])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[2])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[3]) + " Click🔍" ,
                      "description": str(dong[3]) + ", 면적: " + str(area[3]) + "m², 예측 보증금: " + str(int(predict[3])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[3])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[4]) + " Click🔍" ,
                      "description": str(dong[4]) + ", 면적: " + str(area[4]) + "m², 예측 보증금: " + str(int(predict[4])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[4])
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
                      "title": "🏠 보증금 " + str(price[5]) + " Click🔍" ,
                      "description": str(dong[5]) + ", 면적: " + str(area[5]) + "m², 예측 보증금: " + str(int(predict[5])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[5])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[6]) +  "Click🔍" ,
                      "description": str(dong[6]) + ", 면적: " + str(area[6]) + "m², 예측 보증금: " + str(int(predict[6])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[6])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[7]) + " Click🔍" ,
                      "description": str(dong[7]) + ", 면적: " + str(area[7]) + "m², 예측 보증금: " + str(int(predict[7])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[7])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[8]) + " Click🔍" ,
                      "description": str(dong[8]) + ", 면적: " + str(area[8]) + "m², 예측 보증금: " + str(int(predict[8])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[8])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[9]) + " Click🔍" ,
                      "description": str(dong[9]) + ", 면적: " + str(area[9]) + "m², 예측 보증금: " + str(int(predict[9])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[9])
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
                      "title": "🏠 보증금 " + str(price[10]) + " Click🔍" ,
                      "description": str(dong[10]) + ", 면적: " + str(area[10]) + "m², 예측 보증금: " + str(int(predict[10])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[10])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[11]) + " Click🔍" ,
                      "description": str(dong[11]) + ", 면적: " + str(area[11]) + "m², 예측 보증금: " + str(int(predict[11])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[11])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[12]) + " Click🔍" ,
                      "description": str(dong[12]) + ", 면적: " + str(area[12]) + "m², 예측 보증금:" + str(int(predict[12])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[12])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[13]) + " Click🔍" ,
                      "description": str(dong[13]) + ", 면적: " + str(area[13]) + "m², 예측 보증금: " + str(int(predict[13])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[13])
                      }
                    },
                    {
                      "title": "🏠 보증금 " + str(price[14]) + " Click🔍" ,
                      "description": str(dong[14]) + ", 면적: " + str(area[14]) + "m², 예측 보증금: " + str(int(predict[14])),
                      "link": {
                        "web": 'https://m.land.naver.com/article/info/' + str(urlNum[14])
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