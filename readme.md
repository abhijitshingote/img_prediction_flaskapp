Flask frontend for a ML model that predicts dog vs cat from an image. Model uses resnet and transfer learning.

Deploy steps
1. git clone https://github.com/abhijitshingote/img_prediction_flaskapp.git
2. cd img_prediction_flaskapp
3. docker build -t img-recog-flask-app .
4. docker run --name running-flask-app -it -p 5001:5000 img-recog-flask-app
5. Browser - http://127.0.0.1:5001/