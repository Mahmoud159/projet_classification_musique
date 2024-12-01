import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, validation_curve
import matplotlib.pyplot as plt
import pickle
import os

# Charger les données du fichier CSV (ou Excel)
csv_file_path = os.path.join(os.path.dirname(__file__), 'features_30_sec.csv')

df = pd.read_csv(csv_file_path)

# Sélectionner les features pour l'entraînement
X = df[['zero_crossing_rate_mean', 'spectral_centroid_mean', 'rolloff_mean', 
        'mfcc1_mean', 'mfcc2_mean', 'mfcc3_mean', 'mfcc4_mean', 'mfcc5_mean', 
        'mfcc6_mean', 'mfcc7_mean', 'mfcc8_mean', 'mfcc9_mean', 'mfcc10_mean', 
        'mfcc11_mean', 'mfcc12_mean', 'mfcc13_mean', 'mfcc14_mean', 'mfcc15_mean', 
        'mfcc16_mean', 'mfcc17_mean', 'mfcc18_mean', 'mfcc19_mean', 'mfcc20_mean']]

# Les étiquettes (genres de musique)
y = df['label']  

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle SVM
model_svm = SVC()
model_svm.fit(X_train, y_train)

# Évaluer les performances du modèle
print('Train score :', model_svm.score(X_train, y_train))
print('Test score :', model_svm.score(X_test, y_test))

# Validation croisée pour évaluer le modèle
k_3 = np.arange(1, 31)
tr_score_3, val_score_3 = validation_curve(model_svm, X_train, y_train, param_name='C', param_range=k_3, cv=5)

# Visualiser les résultats de la validation croisée
plt.plot(k_3, val_score_3.mean(axis=1), label='validation')
plt.plot(k_3, tr_score_3.mean(axis=1), label='train')
plt.ylabel('score')
plt.xlabel('C')
plt.legend()
plt.show()

# Enregistrer le modèle entraîné dans un fichier .pkl
with open('models/svm_model.pkl', 'wb') as f:
    pickle.dump(model_svm, f)

print('Modèle SVM sauvegardé avec succès dans models/svm_model.pkl')
