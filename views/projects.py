"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:28 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template, request

from models.projects.image_classification import all_datasets, classes_and_image
from models.projects.image_search import upload
from models.neural_network.pre_trained import Inception
from views import app, back


@app.route('/projects/')
@back.anchor
def projects():
    return render_template('projects/index.html')


@app.route('/projects/image-classification/', methods=['GET', 'POST'])
@back.anchor
def image_classification():
    data = dict()
    # Retrieve all available image datasets
    data['datasets'] = all_datasets(full_path=False)
    data['datasets_full'] = all_datasets(full_path=True)
    # Options for next dataset upload
    # Verify uploaded dataset [At least 2 classes]
    # Process selection on the UI for the requested dataset
    # Room for training and testing a new dataset
    # Retrieve dataset classes and one random image for each class
    data['class_n_image'] = classes_and_image(dataset_dir=data['datasets_full'][0])
    # Write a JavaScript snippet to show training progress
    # And testing in case of  delay
    return render_template('projects/image-classification.html', data=data)


@app.route('/projects/generative-models/')
@back.anchor
def generative_models():
    return render_template('projects/generative-models.html')


@app.route('/projects/image-search/', methods=['GET', 'POST'])
@back.anchor
def image_search():
    if request.method == 'POST':
        image = None
        if 'upload-file' not in request.form:
            image = {'file': request.files['upload-file'], 'type': 'upload'}
        elif 'camera-file' not in request.form:
            image = {'file': request.files['camera-file'], 'type': 'upload'}
        elif request.form['image-url']:
            image = {'file': request.form['image-url'], 'type': 'url'}
        path = upload(image)
        if path and type(path) == str:
            # Start searching...
            print('Loading pre-trained inception model...')
            model = Inception(weights='imagenet')
            results = model.predict(path)
            print('Image prediction', results)

        else:
            print('Error with the upload')
    return render_template('projects/image-search.html')


@app.route('/projects/ai-articles/')
@back.anchor
def ai_articles():
    return render_template('projects/ai-articles.html')


@app.route('/projects/auto-encoding/')
@back.anchor
def auto_encoding():
    return render_template('projects/auto-encoding.html')


@app.route('/projects/reinforcement-learning/')
@back.anchor
def reinforcement_learning():
    return render_template('projects/reinforcement-learning.html')
