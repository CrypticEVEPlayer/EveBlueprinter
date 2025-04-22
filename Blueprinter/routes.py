from flask import render_template, url_for, flash, redirect, request
from Blueprinter import app, db
from Blueprinter.models import t_industryActivityMaterials, InvTypes


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/bpo/<int:typeid>", methods=['GET', 'POST'])
def bpo(typeid):
    materials = db.session.query(t_industryActivityMaterials).filter_by(typeID = typeid).all()
    print(len(materials))
    if len(materials) == 0:
        flash('Blueprint not found', 'danger')
        return render_template('home.html')
    items = []
    blueprint = InvTypes.query.get(typeid)
    for material in materials:
        print(material)
        invtype = InvTypes.query.get(material.materialTypeID)
        print(invtype)
        item = {'id': material.materialTypeID,
                'qty': material.quantity,
                'name': invtype.typeName}
        print(item)
        items.append(item)
    
    return render_template('home.html', items=items, name=blueprint.typeName)
