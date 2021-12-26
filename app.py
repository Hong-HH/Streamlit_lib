import streamlit as st
from streamlit_folium import folium_static
import folium
import json


def main() :
    st.title('테스트 페이지 입니다.')
    

    lib = ['folium', 'observable']
    select_lib = st.sidebar.selectbox('라이브러리를 선택해주세요', lib )

    if select_lib == 'folium' :
        st.subheader('folium')
        choice_eg = st.sidebar.radio('선택해주세요', ['예시', '예시2'])
        if choice_eg == '예시' :
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

        elif choice_eg == '예시2' :
            geo_path = 'data/korea.geojson'
            geo_str = json.load(open(geo_path, encoding='utf-8'))

    
    elif select_lib == 'observable' :
        pass


if __name__ == '__main__' :
    main()