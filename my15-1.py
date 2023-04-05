#cmd창 : pip install pymysql -- 파이썬에서 db(mysql)쓰기 위한 드라이버 설치
import pymysql 

conn,cur=None,None
data1,data2,data3,data4="","","",""
sql=""

conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='new_schema',charset='utf8')
cur=conn.cursor() #만들어둔 쿼리문을 db쪽에 연결하는데 사용

while(True):
    data1=input("사용자 ID ==> ") #입력받을땐 문자타입으로 받아짐
    if data1 == "":
        break
    data2=input("사용자 이름 ==> ")
    data3=input("사용자 이메일 ==> ")
    data4=input("사용자 출생연도 ==> ")

    sql="insert into Customer values("+data1+", '"+data2+"', '"+data3+"', '"+data4+"')" #data1은 int타입이여야해서 ''없음
    cur.execute(sql)

conn.commit()
conn.close()