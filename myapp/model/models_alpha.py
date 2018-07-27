from django.db import models
from django.db import connection

# Create your models here.
def patientregModel(pname,pmob,pimg,padd,pemail,ppass):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO patient_profile(name,mobile,image,address,email,password)VALUES('%s','%s','%s','%s','%s','%s')"%(pname,pmob,pimg,padd,pemail,ppass))
    rid=cursor.lastrowid
    connection.close()
    return rid
def docregModel(hname,dname,dimg,dspcl,dcon):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO doctor_profile(hospital_name,name,image,specialization,contact)VALUES('%s','%s','%s','%s','%s')"%(hname,dname,dimg,dspcl,dcon))
    rid=cursor.lastrowid
    connection.close()
    return rid
def hospitalregModel(hname,hadd,hemail,hpass,hsecurity,hans):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO hospital_profile(name,address,email,password,security_ques,answer)VALUES('%s','%s','%s','%s','%s','%s')"%(hname,hadd,hemail,hpass,hsecurity,hans))
    rid=cursor.lastrowid
    connection.close()
    return rid
def p_checkuserModel(email,pass_word):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM patient_profile WHERE email='%s' AND password='%s'"%(email,pass_word))
    rowcount = cursor.rowcount
    connection.close()
    return rowcount
def h_checkuserModel(email,pass_word):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM hospital_profile WHERE email='%s' AND password='%s'"%(email,pass_word))
    rowcount = cursor.rowcount
    connection.close()
    return rowcount
def pf_checkuserModel(email):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM patient_profile WHERE email='%s'"%(email))
    rowcount = cursor.rowcount
    connection.close()
    return rowcount
def p_updatepassModel(p_password,email):
    cursor=connection.cursor()
    cursor.execute("update patient_profile set password='%s' where email='%s'"%(p_password,email))
    connection.close()
def hospital_listModel():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM hospital_profile")
    hlist=cursor.fetchall()
    connection.close()
    return hlist
def doc_listModel():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM doctor_profile")
    dlist=cursor.fetchall()
    connection.close()
    return dlist
def appointmentModel(h_name,d_name,dept,date,time):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO appointments(hospital_name,doctor_name,department,date,time)VALUES('%s','%s','%s','%s','%s')"%(h_name,d_name,dept,date,time))
    rid=cursor.lastrowid
    connection.close()
    return rid
def getAppointmentDetailsModel():
    cursor=connection.cursor()
    cursor.execute("select * from appointments")
    rows_effected=cursor.fetchall()
    connection.close()
    return rows_effected
def df_checkuserModel(name):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM doctor_profile WHERE name='%s'"%(name))
    rowcount = cursor.rowcount
    connection.close()
    return rowcount
def d_updatepassModel(contact,name):
    cursor=connection.cursor()
    cursor.execute("update doctor_profile set contact='%s' where name='%s'"%(contact,name))
    connection.close()
def d_checkuserModel(name,contact):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM doctor_profile WHERE name='%s' AND contact='%s'"%(name,contact))
    rowcount = cursor.rowcount
    connection.close()
    return rowcount
    


    
