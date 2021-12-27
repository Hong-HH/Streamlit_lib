import streamlit as st
import mysql.connector
from mysql.connector.errors import Error
from datetime import datetime
from mini_open_app import run_mini_add_app

from mysql_connection import get_connection

def run_mini_app() :
    st.subheader('미니멀리스트 도전 : 옷장')
    choice = st.sidebar.selectbox('메뉴를 선택해주세요', ['회원가입', '옷장에 옷 넣기','옷장 정리하기'])
    if choice == '회원가입' :
        name = st.text_input('닉네임을 적어주세요 (1~12글자)')
        u_password = st.text_input('비밀번호를 적어주세요 (4~20글자)')

        if (len(name) > 0) and (len(name) < 13) and (len(u_password) > 3) and (len(u_password) < 21) :
            submit = st.button('회원가입')  
            if submit :

                try : 
                    # 1. DB에 연결
                    connection = get_connection()
                    # 2. 쿼리문 만들기 : mysql workbench 에서 잘 되는것을 확인한 SQL문을 넣어준다.
                    # 이렇게 함수를 쓰면 로컬타임으로 가져온다. 하지만 서버에 저장할때는 UTC로 넣어주어야 한다.
                    current_time = datetime.now()

                    query = '''insert into mini_user
                                (nick_name, password)
                                values
                                (%s, %s);'''
                    # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭 써주자.
                    record = (name,u_password)
                    # 3. 커넥션으로부터 커서를 가져온다.
                    cursor = connection.cursor()

                    # 4. 쿼리문을 커서에 넣어서 실행한다. // 실제로 실행하는 것은 커서가 해준다.
                    # 레코드는 직접입력말고 변수로 넣었을때 실행
                    cursor.execute(query, record)

                    # 5. 커넥션을 커밋한다. => 디비에 영구적으로 반영하라는 뜻.
                    connection.commit()
                    st.write('회원가입이 완료되었습니다.')

                except Error as e:
                    print('Error', e)
                    st.write('다른 아이디로 시도해주세요')
                # finally는 필수는 아니다.
                finally :
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print('MySQL connection is closed')
            else :
                st.text('아이디는 1~12 글자, 비밀번호는 4~20글자로 적어주세요')
    
    elif choice == '옷장에 옷 넣기' :
        run_mini_add_app()

    elif choice == '옷장 정리하기' :
        pass