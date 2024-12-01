import base64
import librosa
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

#pour le service svm
def preprocess_wav(wav_base64):
    # Convertir le base64 en fichier audio wav
    wav_data = base64.b64decode(wav_base64)
    with open("temp.wav", "wb") as f:
        f.write(wav_data)

    # Charger le fichier wav et extraire des features (MFCCs par exemple)
    y, sr = librosa.load("temp.wav", sr=None)

    # 1. Zero Crossing Rate
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y=y))

    # 2. Spectral Centroid
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

    # 3. Spectral Rolloff
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))

    # 4. MFCCs (20 coefficients MFCC)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfccs_mean = np.mean(mfccs.T, axis=0)

    # Combiner tous les features en un seul vecteur
    features = np.hstack([
        zero_crossing_rate,
        spectral_centroid,
        rolloff,
        mfccs_mean 
    ])

    return features

