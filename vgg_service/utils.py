import base64
import librosa
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array
import os
from PIL import Image

#pour le service vgg19
def preprocess_wav_vgg19(wav_base64):
    # Convertir le base64 en fichier audio wav
    wav_data = base64.b64decode(wav_base64)
    wav_path = "temp.wav"
    with open(wav_path, "wb") as f:
        f.write(wav_data)

    # Charger l'audio et générer un spectrogramme
    y, sr = librosa.load(wav_path, sr=None)

    # Créer le spectrogramme
    spectrogram_path = "temp_spectrogram.png"
    plt.figure(figsize=(10, 4))
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.savefig(spectrogram_path)
    plt.close()

    # Charger le spectrogramme et le convertir en tableau de pixels
    spectrogram_img = Image.open(spectrogram_path).convert('RGB') 
    spectrogram_img = spectrogram_img.resize((224, 224))
    spectrogram_img = img_to_array(spectrogram_img) 
    spectrogram_img = np.expand_dims(spectrogram_img, axis=0)  

    # Supprimer les fichiers temporaires
    os.remove(wav_path)
    os.remove(spectrogram_path)

    return spectrogram_img