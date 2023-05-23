import requests
from flask import Flask, render_template, request, redirect
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


con = psycopg2.connect(database="jew",
                       user="postgres",
                       password="08112001io",
                       host="127.0.0.1",
                       port="5432")
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()


app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def loginindex():
    return render_template('login.html') 


@app.route('/login/', methods=['POST'])
def login():
    if request.form.get("login"):
        username = request.form.get('username')
        password = request.form.get('password')
    
        if not username:
            return ("Вы не ввели логин")
        if not password:
            return ("Вы не ввели пароль")

    
        cur.execute("SELECT * FROM jew_user WHERE username='{username}' AND password='{password}'".\
                    format(username=username, password=password))
    
        records = cur.fetchall()
    
        if not records:
            con.commit()
            return ('Пароль и логин введены неверно, либо же такого аккаунта не существует')
        else:
            cur.execute("SELECT * FROM jewellery")
            jew_name = cur.fetchall()
            jew_namee = ''
            s = 0
            while s < len(jew_name):
                jewn = jew_name[s][1]
                jew_namee = jew_namee + str(jewn) + ', '
                s += 1
            return render_template('account.html', name=records[0][1], discount=records[0][4], jew_name=jew_namee[0:-2]) 
    elif request.form.get("registration"):
        return redirect("/reg/")


@app.route('/reg/', methods=['GET'])
def regindex():
    return render_template('reg.html') 


@app.route('/reg/', methods=['POST'])
def reg():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    
    if not username:
        return ("Вы не ввели логин")
    if not password:
        return ("Вы не ввели пароль")
    
    
    cur.execute("SELECT * FROM jew_user WHERE username in('{username}')".\
                format(username=username))
    
    records = str(cur.fetchall())
    
    if records == '[]':
        cur.execute("INSERT INTO jew_user (name, username, password) VALUES ('{name}', '{username}', '{password}')".\
                    format(name=name, username=username, password=password))
        con.commit()
        return ('Поздравляю с успешной регистрацией')
    else:
        con.commit()
        return('Аккаунт с таким логином уже существует')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)