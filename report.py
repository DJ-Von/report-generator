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


def g():
    doc = DocxTemplate("templ.docx")
    conf = yaml.full_load((open('conf.yaml')).read())
    for n, i in enumerate(conf.get('tasks')):
        code = exe(i.get('file'))
        open(i.get('file')[:-3]+'.pas', 'w').write(code)
        print(f'code = ', code)
        open('img_buffer.svg', 'w').write(img_gen.code_img(code))
        cairosvg.svg2png(url='img_buffer.svg', write_to=f'{i.get("file")[:-3]}.png')
        
        open(f'{i.get("file")[:-3]}.svg', 'w').write(img_gen.code_img(code))
        
        conf['tasks'][n] |= {'code': InlineImage(doc, f'{i.get("file")[:-3]}.png')}
        doc.replace_pic(f'{i.get("file")[:-3]}.png',f'{i.get("file")[:-3]}.svg')

        conf['tasks'][n] |= {'results': []}
        for nn, j in enumerate(i.get('data')):
            open('img_buffer.svg', 'w').write(img_gen.result_img(executor.execute(i.get('file'), j)))
            cairosvg.svg2png(url='img_buffer.svg', write_to=f'{i.get("file")[:-3]}_start{nn}.png')
            
            open(f'{i.get("file")[:-3]}_start{nn}.svg', 'w').write(img_gen.result_img(executor.execute(i.get('file'), j)))    
            conf['tasks'][n]['results'].append(InlineImage(doc, f'{i.get("file")[:-3]}_start{nn}.png'))

            doc.replace_pic(f'{i.get("file")[:-3]}_start{nn}.png',f'{i.get("file")[:-3]}_start{nn}.svg')

    doc.render(conf)
    doc.save("templ-final.docx")
