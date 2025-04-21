from flask import render_template, url_for, flash, redirect, request
from Blueprinter import app, db
from Blueprinter.models import t_industryActivityMaterials, InvTypes
import sqlite3
import pandas as pd

@app.route("/")
@app.route("/home")
def home():
    #invtype = InvTypes.query.get_or_404(997)
    typeids_to_filter = [997]
    materials = db.session.query(t_industryActivityMaterials).filter_by(typeID = 997).all()
    test = InvTypes.query.get(997)
    print(test)
    print(len(materials))
    items = []
    for material in materials:
        print(material)
        invtype = InvTypes.query.get(material.materialTypeID)
        print(invtype)
        item = {'id': material.materialTypeID,
                'qty': material.quantity,
                'name': invtype.typeName}
        print(item)
        items.append(item)
    
    return render_template('home.html', items=items)


@app.route("/test")
def test():
    #invtype = InvTypes.query.get_or_404(997)
    cnx = sqlite3.connect('instance/sqlite-latest.sqlite')
    materials = pd.read_sql_query('SELECT * from industryActivityMaterials WHERE typeID = 997 AND activityID = 1', cnx)
    items = []
    for index, row in materials.iterrows():
        invtype = pd.read_sql_query(f"SELECT * from InvTypes WHERE typeID = {row['materialTypeID']}", cnx)
        item = {'id': row['materialTypeID'],
                'qty': row['quantity'],
                'name': invtype.loc[0]['typeName']}
        items.append(item)
    
    return render_template('home.html', items=items)
