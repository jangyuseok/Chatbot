import sys
import numpy as np
import requests
import pandas as pd
import joblib
import pickle
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestRegressor




df_month = pd.read_csv('df_sc_month.csv')
df_jongro_month = pd.read_csv('df_jongro_month_sc.csv')
df_2y = pd.read_csv('df_sc_2y.csv')
df_jongro_2y = pd.read_csv('df_jongro_2y_sc.csv')
model_jongro_month = joblib.load('modeling_test_rf (1).pkl')
model_jongro_2y = joblib.load('modeling_jongro_2020_2y_3.pkl')


#월세, 구, 필터링
def sort_month(gu, price, rentPrice, condition1, condition2, condition3):
    df_filter = df_month.loc[(df_month['지역구']==str(gu)) & (df_month['보증금']<=int(price)) & (df_month['임대료']<=int(rentPrice))] #구, 보증금, 임대료 필터링   
    df_filter['score'] = df_filter[condition1]*1.4+df_filter[condition2]*1.2+df_filter[condition3] #선호환경 가중치
    df_dscending = df_filter.sort_values(by=['score'], ascending=False)[:15] 
    return df_dscending


#종로구 월세, 필터링, 예측
def sort_jongro_month(price, rentPrice, condition1, condition2, condition3):
    df_filter = df_jongro_month.loc[(df_jongro_month['보증금']<=int(price)) & (df_jongro_month['임대료']<=int(rentPrice))] #보증금, 임대료 필터링   
    df_filter['score'] = df_filter[condition1+'_sc']*1.4+df_filter[condition2+'_sc']*1.2+df_filter[condition3+'_sc'] #선호환경 가중치
    df_dscending = df_filter.sort_values(by=['score'], ascending=False)[:15] 
    input_data = df_dscending[['임대면적','보증금','위도','경도','문화생활','판매시설','음식점']]
    df_dscending['예측값'] = model_jongro_month.predict(input_data)
    return df_dscending


# #전세, 구, 필터링
def sort_2y(gu, price, condition1, condition2, condition3):
    df_filter = df_2y.loc[(df_2y['지역구']==str(gu)) & (df_2y['보증금']<=int(price))] #구, 보증금, 임대료 필터링   
    df_filter['score'] = df_filter[condition1]*1.4+df_filter[condition2]*1.2+df_filter[condition3] #선호환경 가중치
    df_dscending = df_filter.sort_values(by=['score'], ascending=False)[:15] 
    return df_dscending


# #종로구 전세, 필터링, 예측
def sort_jongro_2y(price, condition1, condition2, condition3):
    df_filter = df_jongro_2y.loc[(df_jongro_2y['보증금']<=int(price))] #보증금, 임대료 필터링   
    df_filter['score'] = df_filter[condition1]*1.4+df_filter[condition2]*1.2+df_filter[condition3] #선호환경 가중치
    df_dscending = df_filter.sort_values(by=['score'], ascending=False)[:15] 
    input_data = df_dscending[['임대면적', '위도','경도','건강','카페','문화생활','편의시설','반려동물','대중교통','판매시설','의료시설','공공기관','음식점','오락시설']]
    df_dscending['예측값'] = model_jongro_2y.predict(input_data)
    return df_dscending

