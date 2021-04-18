from docxtpl import DocxTemplate
import yaml
import sys

doc = DocxTemplate("templ2.docx")

conf = yaml.load((open(sys.argv[1])).read())
i = conf.get('i')
work_name = conf.get('work_name')
task = conf.get('task')

context = { 'i' : i, 'name_work' : work_name, 'task': task}

doc.render(context)
doc.save("templ-final2.docx")