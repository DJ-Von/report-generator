import os
from flask import Flask, request, redirect, url_for
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
        conf = request.form.get('text')
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
                g()
                links += '''<a href="'''+url_for('uploaded_file', filename=filename[:-3]+'.pas')+'''"  download>Скачать '''+filename[:-3]+'.pas'+'''</a><br>'''
        #links += '''<a href="'''+url_for('uploaded_file', filename='templ-final.docx')+'''"  download>Скачать отчёт</a><br>'''
        links += '''<a href="/templ-final.docx" download>Скачать отчёт</a>'''
        return '''<p>'''+links+'''</p><br>
                  <a href = "/">На главную</a>  
        '''
                
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <style>
        .add {
            cursor: pointer;
        }
        
        .form input {
            display: block;
        }
    </style>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><textarea rows="10" cols="45" name="text"></textarea></p>
      <input type="file" multiple="" name="file[]" class="amount" accept=".py">
     <!--<div class="form">
        
        <div class="add">+</div>
      </div>
      <script type="text/javascript">
        var $add = document.getElementsByClassName('add')[0];
        var $form = document.getElementsByClassName('form')[0];
        $add.addEventListener('click', function(event) {
        var $input = document.createElement('input');
        $input.type = 'file';
        $input.classList.add('amount');
        $form.insertBefore($input, $add);
      });
      </script>-->
      <p><button type=submit>Генерировать отчет</button></p>
      
    </form>
    '''

app.run()
