import streamlit as st
from streamlit_folium import folium_static
import folium

def main() :
    st.title('테스트 페이지 입니다.')
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


if __name__ == '__main__' :
    main()