from gestor_contraseñas import hashear
from flask import Flask,request,redirect,render_template,session
from datetime import datetime
from models import db,Usuario,Post,Reaccion,Comentario

app = Flask(__name__)
app.secret_key = "MV4T7&M93yxnW4CynPHYkr"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        usuario = Usuario.query.filter_by(username=request.form["usuario"]).first()
        if usuario and usuario.password == hashear(request.form["password"]):
            session["usuario"] = usuario.username
            return redirect("/")
        return render_template("login.html", error="Credenciales Incorrectas")
    return render_template("login.html", error=None)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        if Usuario.query.filter_by(username=request.form["usuario_register"]).first():
            return render_template("register.html", exist_user="Este usuario ya esta registrado")
        nuevo = Usuario(username=request.form["usuario_register"], password=hashear(request.form["password_register"]))
        db.session.add(nuevo)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html", exist_user=None)

@app.route("/crear",methods=["GET","POST"])
def crear():
    if "usuario" not in session:
        return redirect("/login")
    if request.method == "POST":
        autor = Usuario.query.filter_by(username=session["usuario"]).first()
        if not autor:
            session.clear()
            return redirect("/login")
        nuevo_post = Post(
            titulo = request.form["titulo"],
            contenido = request.form["contenido"],
            fecha = datetime.now().strftime("%d/%m/%Y"),
            autor_id = autor.id
        )
        db.session.add(nuevo_post)
        db.session.commit()
        return redirect("/")
    return render_template("crear.html",error=None)

@app.route("/post/<int:id>")
def ver_post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", post=post)

@app.route("/reaccion/<int:post_id>/<tipo>")
def reaccion(post_id,tipo):
    if "usuario" not in session:
        return redirect("/login")
    autor = Usuario.query.filter_by(username = session["usuario"]).first()
    ya_reacciono = Reaccion.query.filter_by(
        usuario_id = autor.id,
        post_id = post_id,
        tipo = tipo
    ).first()
    if ya_reacciono:
        db.session.delete(ya_reacciono)
    else:
        nuevo = Reaccion(tipo=tipo, usuario_id=autor.id, post_id=post_id)
        db.session.add(nuevo)
    db.session.commit()
    return redirect(f"/post/{post_id}")

@app.route("/comentar/<int:post_id>",methods=["POST"])
def comentar(post_id):
    if "usuario" not in session:
        return redirect("/login")

    autor = Usuario.query.filter_by(username=session["usuario"]).first()
    new_comentario = Comentario(
        contenido = request.form["contenido"],
        fecha = datetime.now().strftime("%d/%m/%Y"),
        usuario_id = autor.id,
        post_id = post_id
    )
    db.session.add(new_comentario)
    db.session.commit()
    return redirect(f"/post/{post_id}")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    if "usuario" not in session:
        return redirect("/login")
    post = Post.query.get_or_404(id)
    if post.autor.username != session["usuario"]:
        return redirect("/")
    db.session.delete(post)
    db.session.commit()
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False)