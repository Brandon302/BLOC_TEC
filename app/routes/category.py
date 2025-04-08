from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Category

category_bp = Blueprint('category', __name__)

@category_bp.route('/')
def listar_categorys():
    categories = Category.query.all()
    return render_template('categorys/listar_categorys.html', categories=categories)

@category_bp.route('/category/new', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('category.listar_categorys'))

    return render_template('categorys/create_categorys.html')

@category_bp.route('/category/update/<int:id>', methods=['GET', 'POST'])
def update_category(id):
    category = Category.query.get_or_404(id)

    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('category.listar_categorys'))

    return render_template('categorys/update_categorys.html', category=category)

@category_bp.route('/category/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('category.listar_categorys'))
