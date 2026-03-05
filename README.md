# 📝 Blog con Flask + SQLite

> Proyecto web completo desarrollado antes de entrar a la universidad | Full web project built before starting university

---

## 🇪🇸 Español

### 📋 Descripción
Blog web desarrollado con Python y Flask antes de iniciar la carrera de Ingeniería Informática. Permite a grupos de amigos registrarse, publicar posts y leerlos. Incluye autenticación completa, base de datos SQL y diseño minimalista profesional.

### ⚙️ Tecnologías usadas
- **Python 3**
- **Flask** — framework web
- **Flask-SQLAlchemy** — ORM para base de datos
- **SQLite** — base de datos local
- **HTML/CSS** — interfaz de usuario
- **JavaScript** — validación de formularios
- **Jinja2** — motor de plantillas
- **Google Fonts (Inter + Playfair Display)** — tipografía

### 🚀 Cómo instalarlo y usarlo

**1. Cloná el repositorio:**
```bash
git clone https://github.com/luninpotrer-png/blog-flask.git
cd blog-flask
```

**2. Instalá las dependencias:**
```bash
pip install flask flask-sqlalchemy
```

**3. Ejecutá el programa:**
```bash
python app.py
```

**4. Abrí el navegador en:**
```
http://127.0.0.1:5000
```

### 📁 Estructura del proyecto
```
blog-flask/
├── app.py
├── models.py
├── gestor_contraseñas.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── crear.html
│   └── post.html
└── static/
    ├── styles.css
    └── script.js
```

### 🗺️ Rutas disponibles
| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Lista de todos los posts |
| `/login` | GET, POST | Inicio de sesión |
| `/register` | GET, POST | Registro de usuario |
| `/crear` | GET, POST | Crear nuevo post |
| `/post/<id>` | GET | Ver post individual |
| `/eliminar/<id>` | GET | Eliminar post propio |
| `/logout` | GET | Cerrar sesión |

### ✨ Características
- Registro e inicio de sesión con SHA-256
- Protección contra fuerza bruta (bloqueo tras 3 intentos)
- Sessions de Flask para autenticación real
- CRUD completo de posts
- Base de datos SQLite con SQLAlchemy
- Relaciones entre tablas (Usuario → Posts)
- Validación de formularios con JavaScript
- Mostrar/ocultar contraseña
- Diseño minimalista profesional
- Nav responsivo con usuario activo

### 👨‍💻 Sobre el autor
Soy Owen, autodidacta de 18 años de Perú. Desarrollé este proyecto antes de iniciar Ingeniería Informática en marzo del 2026. Es mi sexto proyecto personal y el segundo con interfaz web, el primero usando base de datos SQL. Actualmente entrenando en TryHackMe con enfoque en ciberseguridad defensiva.

---

## 🇬🇧 English

### 📋 Description
A full web blog built with Python and Flask before starting my Computer Engineering degree. Allows groups of friends to register, publish posts and read them. Includes full authentication, SQL database and professional minimalist design.

### ⚙️ Technologies used
- **Python 3**
- **Flask** — web framework
- **Flask-SQLAlchemy** — ORM for database
- **SQLite** — local database
- **HTML/CSS** — user interface
- **JavaScript** — form validation
- **Jinja2** — template engine
- **Google Fonts (Inter + Playfair Display)** — typography

### 🚀 How to install and use

**1. Clone the repository:**
```bash
git clone https://github.com/luninpotrer-png/blog-flask.git
cd blog-flask
```

**2. Install dependencies:**
```bash
pip install flask flask-sqlalchemy
```

**3. Run the program:**
```bash
python app.py
```

**4. Open your browser at:**
```
http://127.0.0.1:5000
```

### ✨ Features
- Registration and login with SHA-256 hashing
- Brute force protection (lockout after 3 attempts)
- Flask sessions for real authentication
- Full CRUD for posts
- SQLite database with SQLAlchemy
- Table relationships (User → Posts)
- JavaScript form validation
- Show/hide password toggle
- Professional minimalist design
- Responsive nav with active user badge

### 👨‍💻 About the author
I'm Owen, an 18-year-old self-taught developer from Peru. I built this project before starting my Computer Engineering degree in March 2026. This is my sixth personal project and my second web app, the first one using a SQL database. Currently training on TryHackMe focused on defensive cybersecurity.

---

> ⭐ Si te gustó el proyecto no olvides dejar una estrella / If you liked the project don't forget to leave a star!