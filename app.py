from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


mymodel=tf.keras.models.load_model(
    'mymodel_cats_dogs.h5')
def check_pred(img_path):


    # print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    # plt.imshow(img)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.resnet50.preprocess_input(x)
    preds = mymodel.predict(x)

    # class_dict={value:key for key,value in training_datagen_flow_object.class_indices.items()}
    class_dict={0:'cat',1:'dog'}
    return 'Predicted:'+ class_dict[np.argmax(preds)]
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():

    img=request.files['file1']
    img.save('static/file.jpg')
    prediction=check_pred('static/file.jpg')
    print(prediction)
    return render_template('result.html',data=prediction)


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')