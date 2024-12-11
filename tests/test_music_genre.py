import requests
import base64

def test_music_genre():
    base_url = "http://127.0.0.1:5000"  

    url_svm = f"{base_url}/svm/classify_svm"  
    url_vgg = f"{base_url}/vgg19/classify_vgg19"   

    with open("hiphop.00003.wav", "rb") as audio_file:
        wav_data = base64.b64encode(audio_file.read()).decode("utf-8")

    data = {"wav_music": wav_data}

    response_svm = requests.post(url_svm, json=data) 
    print(response_svm.text) 
    assert response_svm.status_code == 200, f"Error in SVM service: {response_svm.text}"
    assert 'genre' in response_svm.json(), "No genre found in response from SVM service"
    print(f"SVM Predicted Genre: {response_svm.json()['genre']}")

    response_vgg = requests.post(url_vgg, json=data)
    print(response_vgg.text)
    assert response_vgg.status_code == 200, f"Error in VGG service: {response_vgg.text}"
    assert 'genre' in response_vgg.json(), "No genre found in response from VGG service"
    print(f"VGG Predicted Genre: {response_vgg.json()['genre']}")