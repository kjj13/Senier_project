# file name : app.py
# pwd : /myflask/app.py
# 추가해야함

from flask import Flask, render_template, request, redirect , url_for,session, abort, flash

from flask_mail import Mail, Message
	
from email.message import EmailMessage
#from module import dbmodules

import smtplib
import pymysql

app = Flask(__name__)

# 세션 사용하기위한 설정값
app.secret_key = b'jjj!111/'

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rlawndwo123@gamil.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# db = pymysql.connect(host='18.212.183.253',
#                      port=3306,
#                      user='jjoong',
#                      passwd='',
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
                    passwd='',
                    db='pi',
                    charset='utf8')

    cursor = db.cursor()
    
    sql     = "SELECT * FROM cctv WHERE cctv_check = 1;"
    cursor.execute(sql)
    row= cursor.fetchall()
    db.close()

        #db_class.close()
    if row:
        return render_template('first.html', resultData = row)
        #return render_template('imgg.html')
    else:
        #return "false"
        return render_template('first.html',resultData= 'None')

@app.route("/please", methods=['GET'])
def please():
    db = pymysql.connect(host='18.212.183.253',
                    port=3306,
                    user='jjoong',
                    passwd='',
                    db='pi',
                    charset='utf8')

    cursor = db.cursor()
    
    sql     = "SELECT * FROM cctv WHERE cctv_check = 1;"
    cursor.execute(sql)
    row= cursor.fetchall()

    sel_sql = "SELECT * FROM cctv;"
    cursor.execute(sel_sql)
    sel = cursor.fetchall()

    check_sql = "SELECT mem_id ,cctv_name, cctv_check, url FROM cctv WHERE cctv_check = %s ORDER BY mem_id;"

    cursor.execute(check_sql, 0)
    Manager0_Data = cursor.fetchall()

    #허용한 cctv정보들
    cursor.execute(check_sql, 1)
    Manager1_Data = cursor.fetchall()

    #CCTV 정보가 하나라도 있을 경우
    if sel:
        #권한이 있는 CCTV가 있을 경우
        

        if row:
            #return render_template('index.html', resultData = row)
            #로그인이 된 경우
            if session['logflag']:
                mem_id = session['userid']

                c_sql = "SELECT cctv_name, latitude, longitude FROM cctv WHERE mem_id = %s;"
                cursor.execute(c_sql, mem_id)
                Data = cursor.fetchall()

                db.close()
                #관리자로 로그인 한 경우
                if session['userid'] == 'admin':
                  
                    return render_template('final.html', session_data = session['userid'], resultData = row, resultData0 = Manager0_Data, resultData1 = Manager1_Data)
                #일반 구매자로 로그인 한 경우
                else:
                    return render_template('final.html', session_data = session['userid'], resultData = row, cctv_Data = Data)
                    # mem_id = session['userid']

                    # c_sql = "SELECT cctv_name, latitude, longitude FROM cctv WHERE mem_id = %s;"
                    # cursor.execute(c_sql,mem_id)
                    # Data = cursor.fetchall()
                    # db.close()

                    #구매자가 등록한 CCTV가 있는 경우
                    #if Data:
                        #return str(Data)
                        #return render_template('final.html', resultData = row, cctv_Data = Data)
                    #구매자가 등록한 CCTV가 없는 경우
                    #else:
                        #return "등록한 cctv가 없습니다."
                        #return render_template('final.html', resultData = row, cctv_Data = 'None')
                    # Data = request.args.get('Data')
                    
                    #return render_template('final.html', resultData = row, cctv_Data = Data)
            #로그인이 안된 경우
            else:
                #return "로그인 실패"
                # return render_template('final.html', resultData = row)
                return redirect(url_for('index'))
            #return str(row)

        #권한이 있는 CCTV가 없는 경우
        else:
            #return "false"
            #로그인이 된 경우
            if session['logflag']:
                mem_id = session['userid']

                c_sql = "SELECT cctv_name, latitude, longitude FROM cctv WHERE mem_id = %s;"
                cursor.execute(c_sql, mem_id)
                Data = cursor.fetchall()

                db.close()
                #관리자로 로그인 한 경우
                if session['userid'] == 'admin':
                    return render_template('final.html', session_data = session['userid'], resultData = 'None', resultData0 = Manager0_Data, resultData1 = Manager1_Data)
                #일반 구매자로 로그인 한 경우
                else:
                    return render_template('final.html', session_data = session['userid'], resultData = 'None', cctv_Data = Data)
            #로그인이 안된 경우
            else:
                return redirect(url_for('index'))

    #정말 CCTV 정보가 하나도 없을 경우
    else:
        if session['logflag']:
            mem_id = session['userid']

            c_sql = "SELECT cctv_name, latitude, longitude FROM cctv WHERE mem_id = %s;"
            cursor.execute(c_sql, mem_id)
            Data = cursor.fetchall()

            db.close()
            #관리자로 로그인 한 경우
            if session['userid'] == 'admin':
                return render_template('final.html', session_data = session['userid'], resultData='None', resultData0=Manager0_Data, resultData1=Manager1_Data)
            #일반 구매자로 로그인 한 경우
            else:
                return render_template('final.html',session_data = session['userid'], resultData='None', cctv_Data=Data)
        #로그인이 안된 경우
        else:
            return redirect(url_for('index'))


# login 화면
@app.route("/login")
def login():
    return render_template('login.html')

# logout하면 메인페이지(로그인 전 화면)로 이동
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
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    id = request.form["id"]
    pw = request.form["pw"]


    sql     = "SELECT id, pw \
                FROM info where id=%s and pw=%s;"
    cursor.execute(sql,(id,pw))
    row= cursor.fetchall()
    db.close()
    
    #로그인 성공시
    if row:
        session['userid'] = id        #세션값 설정 -> 로그인 된 상태와 안된 상태 화면 다르게 하기위해서
        session['logflag'] = True   
        #auth값으로 일반 사용자 / 관리자 / 구매자 나누기 위해? 
        #근데 세션값으로 다 나눌수 있을꺼같은데..
       
        return redirect(url_for('please'))
    #로그인 실패시
    else :
        return redirect(url_for('login'))


#자신의 cctv 정보를 수정하는 페이지로 이동
@app.route("/cctv_modify_Form", methods=['POST'])
def cctv_modify_Form():
    mem_id = session['userid']
    cctv_name = request.form["cctv_name"]
    #추가
    #arr = [cctv_name, ..] #추가

    return render_template("cctv_modify_Form.html",Data = cctv_name)

#자신의 cctv 정보를 수정
@app.route("/cctv_modify", methods=['POST'])
def cctv_modify():
    mem_id = session['userid']
    latitude = request.form["latitude"]
    longitude = request.form["longitude"]
    cctv_name = request.form["cctv_name"]

    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    modify_sql = "UPDATE cctv SET latitude = %s, longitude = %s WHERE mem_id = %s and cctv_name = %s;"
    
    cursor.execute(modify_sql,(latitude,longitude,mem_id,cctv_name))
    db.commit()
    db.close()

    #return redirect(url_for('cctv_Management'))
    return redirect(url_for('please'))

#자신의 cctv 정보를 삭제
@app.route("/delete_cctv", methods=['POST'])
def delete_cctv():
    mem_id = session['userid']
    cctv_name = request.form["cctv_name"]

    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    delete_sql = "DELETE FROM cctv WHERE mem_id = %s and cctv_name = %s;"

    cursor.execute(delete_sql,(mem_id,cctv_name))

    db.commit()
    db.close()

    #return "삭제"
    return redirect(url_for('please'))

#-----------------여기까지 회원용 cctv 관리------------

#---------------여기부터 관리자용 cctv 관리-------------------
#회원들이 등록한 cctv 정보 다 보여주기 - 관리자용 cctv 관리
# @app.route("/Manager_cctv_Management")
# def Manager_cctv_Management():
#     mem_id = session['userid']

#     db = pymysql.connect(host='18.212.183.253',
#                      port=3306,
#                      user='jjoong',
#                      passwd='',
#                      db='pi',
#                      charset='utf8')

#     cursor = db.cursor()

#     #아직 허용안한 cctv정보들
#     check_sql = "SELECT mem_id ,cctv_name, cctv_check, url FROM cctv WHERE cctv_check = %s ORDER BY mem_id;"   
#     #check_sql = "SELECT mem_id ,cctv_name, cctv_check, url FROM cctv WHERE cctv_check = %s;"  
#     cursor.execute(check_sql,0)
#     row0 = cursor.fetchall()

#     #허용한 cctv정보들
#     cursor.execute(check_sql,1)
#     row1 = cursor.fetchall()
#     db.close()

#     #return str(row0)
#     return redirect(url_for('please'), Manager0_Data = row0 , Manager1_Data = row1)
#     #return render_template('Manager_cctv_management.html',resultData0 = row0, resultData1 = row1)

#cctv 권한주기 -> cctv_check =1 로 만들기
@app.route("/Authorization", methods=['POST'])
def Authorization():
    mem_id = request.form["mem_id"]
    cctv_name = request.form["cctv_name"]
    cctv_check = request.form["cctv_check"]

    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    auth_sql = "UPDATE cctv SET cctv_check = %s WHERE mem_id = %s and cctv_name = %s;"

    if cctv_check == '0':
        cursor.execute(auth_sql,(1,mem_id,cctv_name))
    elif cctv_check == '1':
        cursor.execute(auth_sql,(0,mem_id,cctv_name))

    db.commit()
    db.close()

    #return cctv_check
    #return redirect(url_for('Manager_cctv_Management'))
    return redirect(url_for('please'))

#---------------여기까지 관리자용 cctv 관리-------------------


#cctv 정보 Insert
@app.route("/cctv_insert", methods=['POST'])
def cctv_insert():
    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    if request.method == 'POST':
        unique_num = request.form["unique_num"]        #고유번호
        cctv_name = request.form["cctv_name"]          #cctv 이름
        latitude = request.form["latitude"]            #위도
        longitude = request.form["longitude"]          #경도
        #url = request.form["url"]                     #동영상 경로

        sql = "SELECT * FROM cctv WHERE unique_num = %s;"   # 고유번호가 같은게 있나 확인

        cursor.execute(sql,unique_num)
        row = cursor.fetchall()

        #고유번호가 맞았을 경우
        if row:
            mem_id = session['userid']

            #update_sql = "update cctv set cctv_check = %s where unique_num= %s;"
            cctv_update_sql = "UPDATE cctv SET cctv_name = %s, latitude = %s, longitude = %s, mem_id = %s WHERE unique_num = %s;"

            cursor.execute(cctv_update_sql,(cctv_name,latitude,longitude,mem_id,unique_num))
            db.commit()
            db.close()

            #flash('등록성공!')
            #return "축하해"
            #flash('등록성공!')
            return redirect(url_for('please'))
        #고유번호가 틀렸을 경우
        else:
            #flash('다시입력!')
            return "고유번호가 틀렸습니다."
            # return render_template('cctv_register_Form.html')
    else:
        return "GET방식으로 들어옴"
        # return render_template('cctv_register_Form.html')



# 회원가입 화면
@app.route("/SignUp") 
def SignUp():
    return render_template('SignUp.html')

# 회원가입 Insert
@app.route('/member_insert',  methods=['POST'])
def member_insert():
    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    if request.method == 'POST':
        userid = request.form["id"]
        pw = request.form["pw"]
        mail = request.form["mail"]

        #print(userid,pw,mail)

        #db_class= dbmodules.Database()
    
        sql = "INSERT INTO info(id,pw,mail) \
                    VALUES(%s,%s,%s);"

        cursor.execute(sql,(userid, pw , mail))
        db.commit()
        db.close()

        return redirect(url_for('login'))
        #return render_template('insert.html')
 
    #return render_template('insert.html')
    #return render_template('index.html')
    return "insert"

# ID 중복체크
@app.route('/ID_check',  methods=['POST'])
def ID_check():
    db = pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='',
                     db='pi',
                     charset='utf8')

    cursor = db.cursor()

    if request.method == 'POST':
        userid = request.form["id"]

        ID_check_sql = "SELECT * FROM info WHERE id = %s;"

        cursor.execute(ID_check_sql,userid)
        ID_check = cursor.fetchall()

        if ID_check:
            return render_template('SignUp.html',check = 'x')
        else:
            #return str(userid)
            return render_template('SignUp.html',check = 'o', userid = userid)
    else:
        return "GET ERROR"

#로그인 상태에서 이메일 보내기
@app.route('/data',  methods=['POST','GET'])
def data():
    if request.method == 'POST':
        smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

        # 서버 연결을 설정하는 단계
        smtp_gmail.ehlo()

        # 연결을 암호화
        smtp_gmail.starttls()

        #로그인
        smtp_gmail.login('rlawndwo123@gmail.com', '')

        msg=EmailMessage()
    
        # 제목 입력
        msg['Subject']= request.form['email_title']
        
        # 내용 입력
        email_content = request.form['email_content']
        msg.set_content(email_content)
        
        # 보내는 사람
        msg['From']='rlawndwo123@gmail.com'
        
        # 받는 사람
        msg['To']= request.form['email_receiver']
        
        smtp_gmail.send_message(msg)

        return redirect(url_for('please'))
    else:
        return "GET ERROR"


#로그인 안한 상태에서 이메일 보내기
@app.route('/data1',  methods=['POST','GET'])
def data1():
    
    if request.method == 'POST':
        smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

        # 서버 연결을 설정하는 단계
        smtp_gmail.ehlo()

        # 연결을 암호화
        smtp_gmail.starttls()

        #로그인
        smtp_gmail.login('rlawndwo123@gmail.com', '')

        msg=EmailMessage()
    
        # 제목 입력
        msg['Subject']= request.form['email_title']
        
        # 내용 입력
        email_content = request.form['email_content']
        msg.set_content(email_content)
        
        # 보내는 사람
        msg['From']='rlawndwo123@gmail.com'
        
        # 받는 사람
        msg['To']= request.form['email_receiver']
        
        smtp_gmail.send_message(msg)

        return redirect(url_for('index'))
    else:
        return "GET ERROR"
