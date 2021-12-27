from pyarrow import NullType
import streamlit as st
import mysql.connector
from mysql.connector.errors import Error
from datetime import datetime

from mysql_connection import get_connection


def run_mini_add_app() :
    st.text('로그인을 해주세요')
    name = st.text_input('닉네임을 적어주세요 (1~12글자)')
    pw = st.text_input('비밀번호를 적어주세요 (4~20글자)')
    rogin_b = st.button('로그인')
    # open_b = st.button('옷장열기')
    login = False
    input_all =False
    if rogin_b :
        try : 
            connection = get_connection()
            
            query = '''select * from mini_user
                    where nick_name = %s and password = %s;'''

            record = (name, pw)

            
            cursor = connection.cursor()


            cursor.execute(query, record)

            # select 문은 아래 내용이 필요하다.
            # 커서로 부터 실행한 결과 전부를 받아와라.
            record_list = cursor.fetchall()
            
            # 컬럼의 이름이 키 값으로 온다.
            if len(record_list[0][id]) > 0 :
                login = True
                st.text('로그인 성공!')
                u_id = record_list[0][id]
                
            else :
                st.text('로그인 실패... 아이디랑 비밀번호를 확인해주세요.')
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print('MySQL connection is closed')
                else :
                    print('connection does not exist') 
                
        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
        except Error as e :
            # 뒤의 e는 에러를 찍어라 error를 e로 저장했으니까!
            print('Error while connecting to MySQL', e)
        # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        
        
    #if open_b :
        #if login is True:
            
    season = st.selectbox('계절을 선택해주세요', ['봄/가을', '여름', '겨울', '사계절'])
    type = st.text_input('타입을 적어주세요(외투, 하의, 상의 등)')
    type_detail = st.text_input('더 자세한 타입을 적어주세요(코트, 티셔츠 등)')
    color = st.text_input('색상을 적어주세요')
    last_worn = st.date_input('마지막으로 입은 날짜를 선택해주세요')

    submit = st.button('입력하기')
    if (season) and (type) and (type_detail) and (color) and (last_worn) :
        input_all = True
    if (submit) and (input_all):
        print('시간없다'  )

    
    try :
        query = '''insert into mini_clothes
                    (user_id, season, type, type_detail, color, last_worn)
                    values(%s, %s, %s, %s, %s,%s);'''
        # 셀렉트 문은 파라미터의 param 쓰자.
        record = (u_id, season, type, type_detail, color, last_worn )

        cursor = connection.cursor()

        cursor.execute(query, record)

        # select 문은 아래 내용이 필요하다.
        # 커서로 부터 실행한 결과 전부를 받아와라.
        connection.commit()

    except Error as e:
        print('Error', e)
    # finally는 필수는 아니다.
    finally :
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
    
        #else :
        #   st.text('로그인을 해주세요')
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        finally : 
            print('finally')
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist') 
