import mysql.connector
from mysql.connector.errors import Error
from datetime import datetime

from mysql_connection import get_connection


def run_mini_add_app() :
    st.text('로그인을 해주세요')
    name = st.text_input('닉네임을 적어주세요 (1~12글자)')
    pw = st.text_input('비밀번호를 적어주세요 (4~20글자)')
    rogin_b = st.button('로그인')
    open_b = st.button('옷장열기')
    rogin = False
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
                st.text('로그인 성공!')
                rogin = True
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
        
        
    if open_b :
        if rogin :
            try :
                query = '''select *
                            from mini_user
                            left join mini_clothes
                                on mini_user.id = mini_clothes.user_id
                            where mini_user.nick_name = %s;'''
                # 셀렉트 문은 파라미터의 param 쓰자.
                record = (name, )

                cursor = connection.cursor(dictionary = True)

                cursor.execute(query, record)

                # select 문은 아래 내용이 필요하다.
                # 커서로 부터 실행한 결과 전부를 받아와라.
                record_list = cursor.fetchall()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        finally : 
            print('finally')
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist') 
