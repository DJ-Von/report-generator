from docxtpl import DocxTemplate, InlineImage
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
for n, i in enumerate(conf.get('tasks')):
    code = exe(i.get('file'))
    open(i.get('file')[:-3]+'.pas', 'w').write(code)
    print(f'code = ', code)
    open('img_buffer.svg', 'w').write(img_gen.code_img(code))
    cairosvg.svg2png(url='img_buffer.svg', write_to=f'{i.get("file")[:-3]}.png')
    conf['tasks'][n] |= {'code': InlineImage(doc, f'{i.get("file")[:-3]}.png')}
    for j in i.get('data'): 
        executor.execute(i.get('file'), j)

doc.render(conf)
doc.save("templ-final.docx")
