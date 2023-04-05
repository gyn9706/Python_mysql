#cmd창 : pip install pymysql -- 파이썬에서 db(mysql)쓰기 위한 드라이버 설치
import pymysql 

conn,cur=None,None
data1,data2,data3,data4="","","",""
row=None #객체이기 때문에 아무것도 없다는 초기값을 줌

conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='new_schema',charset='utf8')
cur=conn.cursor() #만들어둔 쿼리문을 db쪽에 연결하는데 사용하는 객체

cur.execute("select * from customer") #쿼리문 보내서 new_schema 데이터 불러옴

print("사용자ID    사용자이름           주소              전화번호") # 타이틀
print("------------------------------------------------------------")

while(True):
    row=cur.fetchone() #fetchone하나씩 fetchall 모두
    if row==None:
        break
    #data1=row[0]
    #data2=row[1]
    #data3=row[2]
    #data4=row[3]

    data1,data2,data3,data4=row

    print("%s %15s %15s %15s" % (data1,data2,data3,data4))
conn.close()