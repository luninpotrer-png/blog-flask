from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    post = db.relationship("Post", backref="autor")
    comentario = db.relationship("Comentario", backref="autor")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    reacciones = db.relationship("Reaccion", backref="post")
    comentarios = db.relationship("Comentario", backref="post")

class Reaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))