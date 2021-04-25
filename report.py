from docxtpl import DocxTemplate, InlineImage
import yaml
import sys
from docx import Document
import executor
import img_gen
from pascal import exe
import platform
import os
import cairosvg

doc = DocxTemplate("templ.docx")

#Получение данных из конфига
conf = yaml.full_load((open(sys.argv[1], encoding='utf-8')).read())
k = 0
t = 0
for n, i in enumerate(conf.get('tasks')):
    
    
    if os.path.exists('img/'+str(i.get('num'))) or os.path.exists('img/'+str(i.get('num'))):
        print('Директория '+str(i.get('num'))+' уже создана. Если хотите обновить данные, то переместите или удалите её и запустите программу заново.')
        
    else:
        open(i.get('file')[:-3]+'.pas', 'w').write(exe(i.get('file')))
        code = exe(i.get('file'))

        if platform.system() == "Windows":
            os.mkdir('img\\'+str(i.get('num')))
            my_img = open('img\\'+str(i.get('num'))+'\\'+str(i.get('num'))+'_code.svg', 'w').write(img_gen.code_img(code))
            path = "img\\"+str(i.get('num'))+"\\"+str(i.get('num'))+"_code.svg"
        elif platform.system() == "Linux":
            os.mkdir('img/'+str(i.get('num')))
            my_img = open('img/'+str(i.get('num'))+'/'+str(i.get('num'))+'_code.svg', 'w').write(img_gen.code_img(code))
            path = 'img/'+str(i.get('num'))+'/'+str(i.get('num'))+'_code.svg'
        path_png = path[0:-4]+'.png'
        print(path_png)
        k=0

        cairosvg.svg2png(url=path, write_to=path_png)
        conf['tasks'][n] |= {'code': InlineImage(doc, path_png)}   

        for j in i.get('data'): 
            executor.execute(i.get('file'), j)
            k += 1
            print(k)
            executor.execute(i.get('file'), j)
            if platform.system() == "Windows":
            	my_img = open('img\\'+str(i.get('num'))+'\\'+str(i.get('num'))+'_start'+str(k)+'.svg', 'w').write(executor.execute(i.get('file'), j))
            elif platform.system() == "Linux":
            	my_img = open('img/'+str(i.get('num'))+'/'+str(i.get('num'))+'_start'+str(k)+'.svg', 'w').write(executor.execute(i.get('file'), j))

doc.render(conf)
doc.save("Отчёт "+str(conf.get('work_num'))+".docx")
