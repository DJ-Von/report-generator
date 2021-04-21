from docxtpl import DocxTemplate
import yaml
import sys
from docx import Document
import executor
import img_gen
from pascal import exe
import executor
import cairosvg
from docx.shared import Inches

doc = DocxTemplate("templ.docx")

#Получение данных из конфига
conf = yaml.load((open(sys.argv[1])).read())
for i in conf.get('tasks'):
    open(i.get('file')[:-3]+'.pas', 'w').write(exe(i.get('file')))
    
    code = exe(i.get('file'))
    open('img_buffer.svg', 'w').write(img_gen.code_img(code))
    p = doc.add_paragraph()
    r = p.add_run()
    cairosvg.svg2png(url='img_buffer.svg', write_to='img.png')
    #r.add_picture('img.png')

    for j in i.get('data'): 
        executor.execute(i.get('file'), j)

doc.render(conf)
doc.save("templ-final.docx")