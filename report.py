from docxtpl import DocxTemplate
import yaml
import sys
from docx import Document
import executor
import img_gen
from pascal import exe
import executor

doc = DocxTemplate("templ.docx")

#Получение данных из конфига
conf = yaml.load((open(sys.argv[1])).read())
for i in conf.get('tasks'):
    open(i.get('file')[:-2]+'.pas', 'w').write(exe(i.get('file')))
#    for j in i.get('data'): 
#        executor.execute(i.get('file'), j)
#open('img_buffer.svg', 'w').write(img_gen.code_img(code))
#doc.replace_pic('car.jpg', 'img_buffer.svg')

doc.render(conf)
doc.save("templ-final.docx")

#Генерация изображения кода программы
#html = executor.code_gen(conf)

