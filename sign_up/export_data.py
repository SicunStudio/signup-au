#-*- coding:utf-8 -*-
from docxtpl import DocxTemplate
import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

applicants = cursor.execute("select * from applicant")
datas = cursor.fetchall()
result = [{"name": data[0], "sex":data[1], "major":data[2], "contact":data[3], "firstWill":data[
    4], "secondWill":data[5], "adjustable":data[6], "selfintroduce":data[7]}for data in datas]
context = {"applicants": result}

tpl = DocxTemplate("signup_tpl.docx")
tpl.render(context)
tpl.save("data.docx")

cursor.close()
conn.close()
