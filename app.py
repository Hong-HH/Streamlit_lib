import streamlit as st
from folium_app import run_folium_app
from form_app import run_form_app
from mini_app import run_mini_app
from streamlit_folium import folium_static
import folium
import json
from branca.colormap import linear
import pandas as pd
import numpy as np


def main() :
    st.title('테스트 페이지 입니다.')
    

    lib = ['folium', 'observable', '설문조사', '미니멀리스트']
    select_lib = st.sidebar.selectbox('라이브러리나 주제를 선택해주세요', lib )

    if select_lib == 'folium' :
        st.subheader('folium')
        choice_eg = st.sidebar.radio('선택해주세요', ['예시복붙', '실험1', '실험2'])
        if choice_eg == '예시복붙' :
            with st.echo():
                # center on Liberty Bell
                m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

                # add marker for Liberty Bell
                tooltip = "Liberty Bell"
                folium.Marker(
                    [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
                ).add_to(m)

                # call to render Folium map in Streamlit
                folium_static(m)

        elif choice_eg == '실험1' :
            geo_path = 'data/korea_re_1.json'
            geo_str = json.load(open(geo_path, encoding='utf-8'))
        
            # center on Liberty Bell
            m = folium.Map(location=[36.8, 127.5], zoom_start=7)

            # 일단 지도 더함
            folium.GeoJson(geo_str).add_to(m)

            # 데이터 가져오기
            df = pd.read_csv('data/df_sido.csv')
            

            # 컬러맵 
            colormap = linear.YlGn_09.scale(df.counts.min(), df.counts.max())
            print(colormap(5.0))

            #choropleth
            folium.GeoJson(
                geo_str,
                name="car_accident",
                style_function=lambda feature: {
                    
                    "fillColor": colormap(df[feature['properties']['NAME']]),
                    "color": "black",
                    "weight": 1,
                    "dashArray": "5, 5",
                    "fillOpacity": 0.9,
                },
            ).add_to(m)

            folium.LayerControl().add_to(m)

            #call to render Folium map in Streamlit
            folium_static(m)

        elif choice_eg == '실험2' :
            run_folium_app()

    
    elif select_lib == '설문조사' :
        run_form_app()

    elif select_lib == '미니멀리스트' :
        run_mini_app()
            






    
    elif select_lib == 'observable' :
        pass


if __name__ == '__main__' :
    main()