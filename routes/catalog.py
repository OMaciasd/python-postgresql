# routes/catalog.py
from flask import Blueprint, render_template, request, redirect, url_for
from database.db import db
from models import Item

catalog_bp = Blueprint('catalog', __name__)


@catalog_bp.route('/catalog')
def catalog():
    items = Item.query.all()
    return render_template('catalog.html', items=items)


@catalog_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        new_item = Item(name=name, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('catalog.catalog'))
    return render_template('add_item.html')
