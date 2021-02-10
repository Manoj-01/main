from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL
from twilio.rest import Client

app=Flask(__name__)
#MySQL connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="postgres"
app.config["MYSQL_DB"]="main"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

#Loading Home page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("workdecor.html",datas=res)

#New User
@app.route("/addusers",methods=['GET','POST'])
def addusers():
    if request.method=='POST':
        name=request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        address = request.form['address']
        city = request.form['city']
        phone_number = request.form['phone_number']
        availability = request.form['availability']
        last_donation = request.form['last_donation']
        degree=request.form['degree']
        major=request.form['major']
        academic_year=request.form['academic_year']
        con=mysql.connection.cursor()
        sql="INSERT INTO `main`.`users` (`NAME`, `AGE`, `BLOOD_GROUP`, `GENDER`, `HEIGHT`, `WEIGHT`, `ADDRESS`, `CITY`, `PHONE_NUMBER`, `AVAILABILITY` ,`LAST_DONATION` ,`DEGREE`, `MAJOR` ,`ACADEMIC_YEAR`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        con.execute(sql,[name,age,blood_group,gender,height,weight,address,city,phone_number,availability,last_donation,degree,major,academic_year])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("addusers.html")

#Update User
@app.route("/editusers/<string:id>",methods=['GET','POST'])
def editusers(id):
    con = mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        address = request.form['address']
        city = request.form['city']
        phone_number = request.form['phone_number']
        availability = request.form['availability']
        last_donation = request.form['last_donation']
        degree = request.form['degree']
        major = request.form['major']
        academic_year = request.form['academic_year']
        sql="update main.users set NAME=%s,AGE=%s,BLOOD_GROUP=%s,GENDER=%s,HEIGHT=%s,WEIGHT=%s,ADDRESS=%s,CITY=%s,PHONE_NUMBER=%s,AVAILABILITY=%s,LAST_DONATION=%s,DEGREE=%s,MAJOR=%s,ACADEMIC_YEAR=%s where ID=%s";
        con.execute(sql,[name,age,blood_group,gender,height,weight,address,city,phone_number,availability,last_donation,degree,major,academic_year,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    con=mysql.connection.cursor()
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editusers.html",datas=res)

#Delete User
@app.route("/deleteusers/<string:id>",methods=['GET','POST'])
def deleteusers(id):
    con=mysql.connection.cursor()
    sql="DELETE FROM users WHERE ID=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))

#Send SMS
@app.route("/sendsms/<string:send_sms>",methods=['GET','POST'])
def sendsms(send_sms):
    con = mysql.connection.cursor()
    sql = "SELECT PHONE_NUMBER=%s FROM users;"
    con.execute(sql,[send_sms])
    mysql.connection.commit()
    con.close()
    print(code())
    return render_template("dummy.html")



#SMS code
def code():
    account_sid ='AC5bfb4aee56ba55e525e0d31ab5762ed2'
    auth_token ='8a0e7f078a0483ceca7b29b84e11819a'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="Well done!!!",
                from_='+15028379552',
                to='+918248607955'
                 )
    print(message.sid)


if (__name__=='__main__'):
    app.run(debug=True)
