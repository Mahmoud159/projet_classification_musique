// Fonction pour classifier l'audio avec SVM
function classifySVM() {
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');

    // Vérifier si un fichier est sélectionné
    if (fileInput.files.length === 0) {
        resultDiv.innerHTML = "Veuillez sélectionner un fichier audio.";
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    // Lire le fichier en tant que data URL (base64)
    reader.onload = function (event) {
        const wavData = event.target.result.split(',')[1]; 
        fetch('/svm/classify_svm', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ wav_music: wavData }), 
        })
        .then(response => response.json())
        .then(data => {
            // Afficher le genre prédit
            resultDiv.innerHTML = "Genre prédit avec SVM: " + data.genre;
        })
        .catch(error => {
            console.error('Erreur lors de la classification SVM:', error);
            resultDiv.innerHTML = "Erreur lors de la classification.";
        });
    };

    // Lire le fichier audio
    reader.readAsDataURL(file);
}

// Fonction pour classifier l'audio avec VGG19 (à adapter selon votre implémentation)
function classifyVGG19() {
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');

    // Vérifier si un fichier est sélectionné
    if (fileInput.files.length === 0) {
        resultDiv.innerHTML = "Veuillez sélectionner un fichier audio.";
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    // Lire le fichier en tant que data URL (base64)
    reader.onload = function (event) {
        const wavData = event.target.result.split(',')[1]; 
        fetch('/vgg19/classify_vgg19', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ wav_music: wavData }), 
        })
        .then(response => response.json())
        .then(data => {
            // Afficher le genre prédit
            resultDiv.innerHTML = "Genre prédit avec VGG19: " + data.genre;
        })
        .catch(error => {
            console.error('Erreur lors de la classification VGG19:', error);
            resultDiv.innerHTML = "Erreur lors de la classification.";
        });
    };

    // Lire le fichier audio
    reader.readAsDataURL(file);
}
