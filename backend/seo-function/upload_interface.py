from flask import Flask, request, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'backend/seo-function'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return '✅ File uploaded successfully!'
    return '''
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)