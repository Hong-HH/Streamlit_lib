import streamlit as st
import numpy as np
import pandas as pd

def run_form_app() :
    eg = ['설명복붙',  '테스트']
    choice_eg = st.sidebar.radio('선택해주세요', eg)
    if choice_eg == '설명복붙' :
        with st.form("my_form"):
            st.write("Inside the form")
            slider_val = st.slider("Form slider")
            checkbox_val = st.checkbox("Form checkbox")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("slider", slider_val, "checkbox", checkbox_val)

        st.write("Outside the form")
    elif choice_eg == '테스트' :
        with st.form("my_form"):
            st.write("설문조사 페이지 입니다")
            slider_val = st.slider("자습시간(분)을 입력해주세요", min_value=0 , max_value=240)
            checkbox_val = st.checkbox("이번주 과제를 제출 하셨으면 체크해주세요")

            if checkbox_val :
                project = '제출'
            else :
                project = '미제출'

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("입력하신 자습시간은 : {} 분 입니다. 과제는 {} 하셨군요".format(slider_val, project))