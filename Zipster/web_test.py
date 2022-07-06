import pandas as pd
import numpy as numpy


df = pd.read_csv('C:\Users\e\Desktop\df_sc_month.csv')

# loaded_model = pickle.load(open('finalized_model.sav','rb'))
# titles = {'건강':0,
#             '카페':1,
#             '문화생활':2,
#             '편의시설':3,
#             '반려동물':4,
#             '대중교통':5,
#             '판매시설':6,
#             '의료시설':7,
#             '공공기관':8,
#             '음식점':9,
#             '오락시설'10
#             }





# c1=titles.get(condition1)
# c2=titles.get(condition2)
# c3=titles.get(condition3)
dong='익선동'
condition1='건강'
condition2='편의시설'
condition3='카페'

def sort(dong, condition1, condition2, condition3):
    df_filter_by_dong = df.loc[(df['법정동']==str(dong))]
                        # df[(df['법정동']==str(dong))]
    df_filter_by_dong['score'] = df_filter_by_dong[condition1]*1.4+df_filter_by_dong[condition2]*1.2+df_filter_by_dong[condition3]
    df_filter_by_dong.sort_values(by='score', ascending=True)
    print(df_filter_by_dong.head())
    return

sort()




