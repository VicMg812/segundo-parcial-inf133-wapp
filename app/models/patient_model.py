from database import db

class Hospytal(db.Model):
    __tablename__ = "patients"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    ci = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `Animal`
    def __init__(self, name, last_name, ci, birth_date):
        self.name = name
        self.last_name = last_name
        self.ci = ci
        self.birth_date= birth_date

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Hospytal.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Hospytal.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, name=None, last_name=None, ci=None, birth_date=None):
        if name is not None:
            self.name = name
        if last_name is not None:
            self.last_name = last_name
        if ci is not None:
            self.ci = ci
        if birth_date is not None:
            self.birth_date=birth_date
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()