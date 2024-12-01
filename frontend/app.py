import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template
from svm_service.svm_service import svm_service
from vgg_service.vgg19_service import vgg19_service


main_app = Flask(__name__)

# Enregistrer les services comme blueprints
main_app.register_blueprint(svm_service, url_prefix='/svm')
main_app.register_blueprint(vgg19_service, url_prefix='/vgg19')

# Route pour servir la page HTML
@main_app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    main_app.run(host='0.0.0.0', port=5000)
