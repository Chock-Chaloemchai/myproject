from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
# import pymysql

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="10.183.255.101",
  user="root",
  password="Nera123456",
  database="neralocaldb"
)
# print(mydb)

#เชื่อมต่อ databast localhost
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root", 
#     password="", 
#     database="chickenfarm"
#     )

#ดึงข้อมูลทั้งหมดของตาราง tbl_user มาเก็บไว้ในตัวแปรเป็นแบบ list
# @app.route("/data")
# def data():
#         cursor = mydb.cursor()
#         sql = ("select * from tbl_user")
#         cursor.execute(sql)
#         data = cursor.fetchall()    
#         return render_template('data.html',data=data)

@app.route("/data_101")
def data_101():
        cursor = mydb.cursor()
        sql = ("select * from member")
        cursor.execute(sql)
        data = cursor.fetchall()    
        return render_template('data_101.html',data=data)

@app.route("/")
def index():
    username = "AdminChock"
    return render_template('index.html',username = username)

@app.route("/register_member")
def register_member():
    return render_template('register_member.html')

# เพิ่มข้อมูลลง มาเก็บไว้ที่ตัวแปร
@app.route("/signup_model")
def signup_model():
    model_name = request.args.get('model_name')
    remark =  request.args.get('remark')
    return render_template('thank.html',data={"model_name":model_name,"remark":remark})

@app.route("/test_add_user")
def test_add_user():
    return render_template('test_add_user.html')

# เพิ่มข้อมูลลง Database localhost
# @app.route("/add_user", methods=['POST'])
# def add_user():
#     if request.method == "POST":
#         fname = request.form['fname']
#         lname = request.form['lname']
#         username = request.form['username']

#         cursor = mydb.cursor()
#         sql = ("insert into `tbl_user` (`firstname`, `lastname`, `username`) values (%s, %s, %s)")
#         cursor.execute(sql,(fname,lname,username))
#         mydb.commit()

#     return redirect(url_for('data'))

# เพิ่มข้อมูลลง Server101
@app.route("/add_user_model", methods=['POST'])
def add_user_model():
    if request.method == "POST":
        model = request.form['model_name']
        
        cursor = mydb.cursor()
        sql = ("CALL AddA02Account(%s, 'gosoftka123', %s, 'Male', 'Thailand', 'th-TH', 1, 'newbot');")
        cursor.execute(sql,(model,model))
        mydb.commit()

    return redirect(url_for('data_101'))

@app.route("/show_member")
def show_member():
    list_username = ["AdminChock","AdminPin","AdminJohn"]
    #ส่งค่าไปแสดงที่หน้าเว็บ
    member = 10
    #ส่งค่าแบบ Dictionary ไปแสดงที่หน้าเว็บ
    data = {"name":"Chaloemchai","age":20,"salary":4200}
    return render_template('show_member.html', data=member,mydata=data, list_username=list_username)

# @app.route("/pin")
# def hello():
#     return "<h1>Hello, Pinnnn!</h1>"

# @app.route("/member/<name>/<age>")
# def member(name,age):
#     return "<h1>Hello, {} age : {} </h1> " .format(name,age)



if __name__ == "__main__":
    app.run(debug=True)

