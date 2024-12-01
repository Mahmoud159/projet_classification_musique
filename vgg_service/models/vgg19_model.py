import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG19
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

import os

# Récupérer le chemin absolu du répertoire courant
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin vers images_original
train_data_dir = os.path.join(base_dir, 'images_original')


# Paramètres pour le prétraitement des images
# Taille d'entrée standard pour VGG19
img_height, img_width = 224, 224  
batch_size = 32 

# Générateur d'images pour le chargement des données
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# Charger les images d'entraînement
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# Charger les images de validation
validation_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Charger VGG19 pré-entraîné sur ImageNet
base_model = VGG19(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))

# Congeler les couches du modèle de base
for layer in base_model.layers:
    layer.trainable = False

# Ajouter des couches Fully-Connected pour la classification
x = base_model.output
x = Flatten()(x) 
x = Dense(256, activation='relu')(x) 
x = Dropout(0.5)(x) 
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(train_generator.num_classes, activation='softmax')(x) 

# Créer le modèle final
model = Model(inputs=base_model.input, outputs=predictions)

# Compiler le modèle
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Entraînement du modèle
history = model.fit(
    train_generator,
    epochs=25,  # Ajustez selon les performances
    validation_data=validation_generator
)

# Tracer la courbe de précision
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(loc='upper left')
plt.show()

# Tracer la courbe de perte
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper left')
plt.show()

model.save('models/vgg19_music_genre_classification.h5')