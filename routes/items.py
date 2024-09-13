from flask import Blueprint, render_template, request, redirect, url_for
from database.db import db
from models import Item

items_bp = Blueprint('items', __name__)


@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        new_item = Item(name=name, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('catalog.catalog'))
    return render_template('add_item.html')
