from flask import Flask, request, jsonify, Blueprint
from .utils import preprocess_wav
import pickle
import os

# app = Flask(__name__)

svm_service = Blueprint('svm_service', __name__)

# Charger le modèle SVM pré-entraîné
model_path = os.path.join(os.path.dirname(__file__), 'models', 'svm_model.pkl')
with open(model_path, 'rb') as f:
    svm_model = pickle.load(f)


@svm_service.route('/classify_svm', methods=['POST'])
def classify_svm():
    # Récupérer le fichier base64 depuis la requête POST
    data = request.json['wav_music']
    # Convertir base64 en wav
    features = preprocess_wav(data)  

    # Traitement et prédiction
    prediction = svm_model.predict([features])

    return jsonify({'genre': prediction[0]})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
