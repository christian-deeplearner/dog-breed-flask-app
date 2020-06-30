from flask import Flask, request, render_template
app = Flask(__name__)

from commons import get_model
from inference import get_dog_breed_name

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('file not uploaded')
            return
        file = request.files['file']
        image = file.read()
        dog_breed = get_dog_breed_name(image_bytes=image)
        print(dog_breed)
        return render_template('results.html', breed=dog_breed)