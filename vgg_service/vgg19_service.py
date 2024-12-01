from flask import Flask, request, jsonify,Blueprint
from .utils import preprocess_wav_vgg19
from tensorflow.keras.models import load_model
import numpy as np
import os

# app = Flask(__name__)
vgg19_service = Blueprint('vgg19_service', __name__)


# Charger le modèle VGG19 pré-entraîné
model_path = os.path.join(os.path.dirname(__file__), 'models', 'vgg19_music_genre_classification.h5')
vgg19_model = load_model(model_path)

# Mapping des indices aux genres
class_indices = {
    0: 'blues',
    1: 'classical',
    2: 'country',
    3: 'disco',
    4: 'hiphop',
    5: 'jazz',
    6: 'metal',
    7: 'pop',
    8: 'reggae',
    9: 'rock'
}

@vgg19_service.route('/classify_vgg19', methods=['POST'])
def classify_vgg19():
    data = request.json['wav_music']

    # Prétraiter le fichier audio pour obtenir un spectrogramme
    spectrogram_img = preprocess_wav_vgg19(data)

    # Traitement et prédiction (spectrogramme pour VGG19)
    prediction = vgg19_model.predict([spectrogram_img])

    # Prendre la classe avec la probabilité la plus élevée
    predicted_class_index = np.argmax(prediction, axis=1)

    # Retourner le genre musical correspondant à l'indice prédit
    predicted_genre = class_indices[predicted_class_index[0]]

    return jsonify({'genre': predicted_genre})

# if __name__ == '__main__':
#     vgg19_service.run(host='0.0.0.0', port=5001)
