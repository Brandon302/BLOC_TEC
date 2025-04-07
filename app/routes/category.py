from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.category import Category

# Definimos el blueprint
categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

# Listar categorías
@categories_bp.route('/')
def listar_categories():
    categories = Category.query.all()
    return render_template('categorys/listar_categorys.html', categories=categories)


if __name__ == '__main__':
    categories_bp.run(debug=True)
