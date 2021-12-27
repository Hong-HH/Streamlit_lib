import streamlit as st
from streamlit_folium import folium_static
import folium
import json
from branca.colormap import linear
import pandas as pd
import numpy as np

def run_folium_app() :
    geo_path = 'data/korea_re_1.json'
    geo_str = json.load(open(geo_path, encoding='utf-8'))

    # center on Liberty Bell
    pop_Map = folium.Map(location=[36.8, 127.5], zoom_start=7)

    # 일단 지도 더함
    
    # 데이터 가져오기
    df = pd.read_csv('data/df_sido.csv')

    pop_Map.choropleth(geo_data = geo_str,
                        data = df,
                        columns=['Name','counts'],
                        fill_color = 'BuPu',
                        key_on='properties.Name',

                        fill_opacity=0.7,
                        line_opacity=0.3,

                        legend_name = '지역별 교통사고'
                        
                        
                        )
    folium_static(pop_Map)

    

