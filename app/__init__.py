import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL desde .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar modelos
from app.models.post import Post
from app.models.category import Category

# Importar Blueprints
from app.routes.post import posts_bp
from app.routes.category import category_bp

# Registrar Blueprints
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(category_bp, url_prefix='/categories')

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')
