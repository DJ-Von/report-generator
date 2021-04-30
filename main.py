import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from report import g


UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    links = ''
    if request.method == 'POST':
        autor = request.form.get('autor')
        work_num = request.form.get('work_num')
        work_name = request.form.get('work_name')
        conf = f"""
---
autor: {autor}
work_name: |-
  {work_name}
work_num: {work_num}
tasks:"""

        counter = int(request.form.get('counter')) 
        for i in range(counter):
            task = request.form.get(str(i+1)+'task')
            num = request.form.get(str(i+1)+'num')
            data = request.form.get(str(i+1)+'data')
            file_name = request.form.get(str(i+1)+'file_name')
            starts = request.form.get(str(i+1)+'starts')
            print('Задача: '+str(i+1))
            print(task)
            
            conf += f"""
  - about: |-
      {task}
    num: {num}
    data:
{data}
    file: {file_name}
    starts: {starts}
"""
            

        conf += f"..."
        
        f = open('conf.yaml', 'w').write(conf)
        uploaded_files = request.files.getlist("file[]")
        filenames = []
        for file in uploaded_files:
            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
                filename = secure_filename(file.filename)
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Save the filename into a list, we'll use it later
                filenames.append(filename)
                links += '''<a href="'''+url_for('uploaded_file', filename=filename[:-3]+'.pas')+'''"  download>Скачать '''+filename[:-3]+'.pas'+'''</a><br>'''
        links += '''<a href="/templ-final.docx" download>Скачать отчёт</a>'''
        g()
        return '''<p>'''+links+'''</p><br>
                  <a href = "/">На главную</a>  
        '''
                
    return render_template('index.html')

app.run()
