import requests

def test_music_genre():
    url_svm = "http://svm_service/classify_svm"  
    url_vgg = "http://vgg19/classify_vgg19"  

    music_file = {"file": open("../data/genres_originales/blues/blues.00000.wav", "rb")}

    # Test du service SVM
    response_svm = requests.post(url_svm, files=music_file)
    assert response_svm.status_code == 200, f"Error in SVM service: {response_svm.text}"
    assert 'genre' in response_svm.json(), "No genre found in response from SVM service"
    print(f"SVM Predicted Genre: {response_svm.json()['genre']}")

    # Test du service VGG
    response_vgg = requests.post(url_vgg, files=music_file)
    assert response_vgg.status_code == 200, f"Error in VGG service: {response_vgg.text}"
    assert 'genre' in response_vgg.json(), "No genre found in response from VGG service"
    print(f"VGG Predicted Genre: {response_vgg.json()['genre']}")

    music_file.close()
