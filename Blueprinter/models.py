from Blueprinter import db

class industryActivityMaterials(db.Model):
    __tablename__ = 'industryActivityMaterials'
    typeID = db.Column(db.Integer, primary_key=True)
    activityID = db.Column(db.Integer)
    materialTypeID = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    #def __repr__(self):
    #    return f"industryActivityMaterials('{self.typeID}', '{self.activityID}', '{self.materialTypeID}', '{self.quantity}')"

class InvTypes(db.Model):
    __tablename__ = 'InvTypes'
    typeID = db.Column(db.Integer, primary_key=True)
    groupID = db.Column(db.Integer)
    typeName = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    mass = db.Column(db.Float)
    volume = db.Column(db.Float)
    capacity = db.Column(db.Float)
    portionSize = db.Column(db.Integer)
    raceID = db.Column(db.Integer)
    basePrice = db.Column(db.DECIMAL(19, 4))
    published = db.Column(db.Boolean)
    marketGroupID = db.Column(db.Integer)
    iconID = db.Column(db.Integer)
    soundID = db.Column(db.Integer)
    graphicID = db.Column(db.Integer)

    def __repr__(self):
        return f"InvTypes('{self.typeID}', '{self.groupID}', '{self.typeName}', '{self.description}')"