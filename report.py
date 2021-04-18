from docxtpl import DocxTemplate
import yaml
import sys

doc = DocxTemplate("templ.docx")

conf = yaml.load((open(sys.argv[1])).read())

i = conf.get('i')
work_name = conf.get('work_name')
task = conf.get('task')
autor_name = conf.get('autor_name')
group = conf.get('group')
var_num = conf.get('var_num')

context = {'autor_name': autor_name, 'group': group, 'var_num': var_num, 'i' : i, 'work_name' : work_name, 'task': task}

doc.render(context)
doc.save("templ-final.docx")