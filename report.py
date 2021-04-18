from docxtpl import DocxTemplate
import yaml
import sys
from docx import Document
import executor

doc = DocxTemplate("templ.docx")

#Получение данных из конфига
conf = yaml.load((open(sys.argv[1])).read())

i = conf.get('i')
work_name = conf.get('work_name')
task = conf.get('task')
autor_name = conf.get('autor_name')
group = conf.get('group')
var_num = conf.get('var_num')
img = conf.get('img')

#Запись данных из конфига
context = {'autor_name': autor_name, 'group': group, 'var_num': var_num, 'i' : i, 'work_name' : work_name, 'task': task}

doc.replace_pic('car.jpg', img)

doc.render(context)
doc.save("templ-final.docx")

#Генерация изображения кода программы
html = executor.code_gen(conf.get('file'))

print(html)
q = open('1.svg', 'w')
q.write(html)
q.close()