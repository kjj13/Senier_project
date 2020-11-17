# file name : app.py
# pwd : /myflask/app.py
# 추가해야함

from flask import Flask, render_template, request, redirect , url_for,session, abort

from module import dbmodules

import pymysql

app = Flask(__name__)

# 세션 사용하기위한 설정값
app.secret_key = b'jjj!111/'

# db = pymysql.connect(host='18.212.183.253',
#                      port=3306,
#                      user='jjoong',
#                      passwd='1234',
#                      db='pi',
#                      charset='utf8')

# cursor = db.cursor()

# 메인화면
@app.route("/", methods=['GET'])
def index():
    #return "<h1>Hello</h1>"
    #return render_template('test.html')
    #db_class= dbmodules.Database()

        db = pymysql.connect(host='18.212.183.253',
                        port=3306,
                        user='jjoong',
                        passwd='1234',
                        db='pi',
                        charset='utf8')

        cursor = db.cursor()
    
        sql     = "SELECT * FROM cctv;"
        cursor.execute(sql)
        row= cursor.fetchall()
        db.close()

        #db_class.close()
        if row:
            return render_template('index.html',
                                    result=None,
                                    resultData=row,
                                    resultUPDATE=None)
        else:
            return render_template('in.html',
                                    result=None,
                                    resultData=None,
                                    resultUPDATE=None)



@app.route("/test", methods=['POST'])
def test():
    return 'test'
    #return render_template('info.php')

# login 화면
@app.route("/login")
def login():
    return render_template('login.html')

# logout하면 메인페이지로 이동
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

# Login 확인
@app.route("/check", methods=['POST'])
def check():
    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='1234',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    id = request.form["id"]
    pw = request.form["pw"]

 
    sql     = "SELECT id, pw \
                FROM member where id=%s and pw=%s;"
    cursor.execute(sql,(id,pw))
    row= cursor.fetchall()
    #db.close()
    
    #로그인 성공시
    if row:
        session['userid'] = id        #세션값 설정 -> 로그인 된 상태와 안된 상태 화면 다르게 하기위해서
        session['logflag'] = True   
        #auth값으로 일반 사용자 / 관리자 / 구매자 나누기 위해? 
        #근데 세션값으로 다 나눌수 있을꺼같은데..
        # update_sql = "UPDATE member set auth=1 where id=%s;"

        # cursor.execute(update_sql,id)
        # db.commit()
        # db.close()

        #return render_template('login_test.html')
        return redirect(url_for('index'))
    #로그인 실패시
    else :
        # update_sql = "UPDATE member set auth=0 where id=%s;"

        # cursor.execute(update_sql,id)
        # db.commit()
        # db.close()
        return render_template('login.html')
        #return "아이디 또는 패스워드를 확인 하세요."
        #return redirect(url_for('index'))
        
#카메라 등록 화면
@app.route("/cctv_register_Form")
def cctv_register_Form():
    return render_template('cctv_register_Form.html')

#cctv 테스트
@app.route("/xx", methods=['POST'])
def xx():
    return render_template('xx.html')

@app.route("/xx_test", methods=['POST'])
def xx_test():
    latitude = request.form["Latitude"]
    longitude = request.form["Longitude"]

    x = latitude + longitude

    return x

#카메라 정보 Insert
@app.route("/cctv_insert", methods=['POST'])
def cctv_insert():
    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='1234',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    if request.method == 'POST':
        cctv_id = request.form["cctv_id"]       #고유번호
        latitude = request.form["latitude"]     #위도
        longitude = request.form["longitude"]   #경도
        url = request.form["url"]               #동영상 경로

        sql = "SELECT * FROM cctv WHERE unique_num = %s;"

        cursor.execute(sql,cctv_id)
        row = cursor.fetchall()

        if row:
            mem_id = session['userid']
            cctv_insert_sql = "UPDATE cctv SET latitude = %s, longitude = %s, url = %s, mem_id = %s where id = %s"
            #print(mem_id)

            cursor.execute(cctv_insert_sql,(latitude,longitude,url,mem_id,cctv_id))
            db.commit()
            db.close()

            #return mem_id
            flash('등록성공!')
            return redirect(url_for('index'))
        else:
            flash('다시입력!')
            return render_template('cctv_register_Form.html')
    else:
        return render_template('cctv_register_Form.html')



# 회원가입 화면
@app.route("/SignUp")
def SignUp():
    return render_template('SignUp.html')

# 회원가입 Insert
@app.route('/insert',  methods=['POST'])
def insert():
    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='1234',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    if request.method == 'POST':
        userid = request.form["id"]
        pw = request.form["pw"]
        mail = request.form["mail"]

        #print(userid,pw,mail)

        #db_class= dbmodules.Database()
    
        sql = "INSERT INTO member(id,pw,mail) \
                    VALUES(%s,%s,%s);"

        cursor.execute(sql,(userid, pw , mail))
        db.commit()
        db.close()

        return redirect(url_for('index'))
        #return render_template('insert.html')
 
    return render_template('insert.html')
    #return render_template('index.html')
    #return "insert"

 
# # UPDATE 함수 예제
# @app.route('/update', methods=['GET'])
# def update():
#     db_class= dbmodules.Database()
 
#     sql     = "UPDATE testDB.testTable \
#                 SET test='%s' \
#                 WHERE test='testData'"% ('update_Data')
#     db_class.execute(sql)   
#     db_class.commit()
 
#     sql     = "SELECT idx, test \
#                 FROM testDB.testTable"
#     row     = db_class.executeAll(sql)
 
#     return render_template('/test/test.html',
#                             result=None,
#                             resultData=None,
#                             resultUPDATE=row[0])
