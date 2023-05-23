import sqlite3


con = sqlite3.connect("mtuci.db")
cur = con.cursor()

def table(con, cur):
    cur.execute("CREATE TABLE IF NOT EXISTS subject ( id serial PRIMARY KEY, name varchar (128) NOT NULL );")
    cur.execute("CREATE TABLE IF NOT EXISTS subject_type ( id serial PRIMARY KEY, name varchar(128) NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS class ( id serial PRIMARY KEY, subject int NOT NULL REFERENCES subject(id), subject_type int NOT NULL REFERENCES subject_type(id) );")
    cur.execute("CREATE TABLE IF NOT EXISTS time ( id serial PRIMARY KEY, start_time varchar(64) NOT NULL );")
    cur.execute("CREATE TABLE IF NOT EXISTS teacher ( id serial PRIMARY KEY, full_name varchar(256) NOT NULL );")
    cur.execute("CREATE TABLE IF NOT EXISTS teacher_subject ( id serial PRIMARY KEY, teacher int NOT NULL REFERENCES teacher(id), class int NOT NULL REFERENCES class(id) );")
    cur.execute("CREATE TABLE IF NOT EXISTS timetable ( id serial PRIMARY KEY, week int NOT NULL, day int NOT NULL, class int NOT NULL REFERENCES class(id), class_time int NOT NULL REFERENCES time(id), room_number varchar(64) NOT NULL );")
    con.commit()

def day_go(day, week, cur):
    full_day = ''
    con = sqlite3.connect("mtuci.db")
    cur = con.cursor()    
    for i in range(1,6):
        cur.execute("SELECT * FROM timetable WHERE day='{day}' and week='{week}' and class_time='{i}'".\
                    format(day=day, week=week, i=i))
        records_para = list(cur.fetchall())
        
        if not records_para:
            n_para = '\n<Нет пары>'
            name_para = ''
            type_para = ''
            teacher = ''
            kab = ''
        else:
            n_para = ''
            cur.execute("SELECT * FROM class WHERE id='{id}'".\
                        format(id=int(records_para[0][3])))
            records_class = list(cur.fetchall())
            cur.execute("SELECT * FROM subject WHERE id='{id}'".\
                        format(id=int(records_class[0][1])))
            records = list(cur.fetchall())
            name_para = '\n' + str(records[0][1])
            
            cur.execute("SELECT * FROM subject_type WHERE id='{id}'".\
                        format(id=int(records_class[0][2]))) 
            records = list(cur.fetchall())
            type_para = '\n' + str(records[0][1])

            cur.execute("SELECT * FROM teacher_subject WHERE class='{classs}'".\
                        format(classs=int(records_class[0][0]))) 
            records_teacher = list(cur.fetchall())
            
            cur.execute("SELECT * FROM teacher WHERE id='{id}'".\
                        format(id=int(records_teacher[0][1]))) 
            records = list(cur.fetchall())
            teacher = '\n' + str(records[0][1])
            
            kab = 'в ' + str(records_para[0][5])
            
            
        cur.execute("SELECT * FROM time WHERE id='{i}'".\
                    format(i=i))
        records = list(cur.fetchall())
        time = records[0][1]
        
        
        para = f'{i}. {time} {n_para} {name_para} {teacher} {type_para} {kab}'
        full_day = f'{full_day} {para} \n \n'
    
    full_day = str(full_day[:-4])
    con.commit()
    return(full_day)
