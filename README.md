# Social-APP
Esta es una aplicacion web llamada Tattle. 
Tattle es un microblog para compartir informacion y expandir ideas! como Twitter. 

* Frontend fue desarrollado con bootstrap y el backend con Django + Python. 

## Que puedes hacer en esta App?
- Crear una cuenta
- Crear una publicacion
- Comentar una publicacion de otro usuario
- Remover publicacion 
- Editar profile
- Editar publicacion
- Cambiar contraseña

## 🚀 About Me
I'm Renata Cardoso. 😀
I'm Security Engineer and Python Student, but I'm also a mother of two dogs, a gamer and a technology lover.


## Framework 
[Django] (https://docs.djangoproject.com/en/4.0/),
[Bootstrap] (https://getbootstrap.com/)

## Installation
Create a new folder in your desktop 

$BASH
```bash
cd desktop
mkdir new_folder
cd new_folder
code .
```
$BASH

```bash
git clone https://github.com/RenataCardoli/Social-APP.git
cd social-APP
python -m virtualenv venv
(windows) venv\Scripts\activate
(mac) . ./venv/bin/activate 
pip install -r requirements.txt
python manage.py migrate  
python manage.py runserver 
python manage.py createsuperuser

```
## Comentarios
- Esta es una entrega de proyecto Final para el curso de Python en Coderhouse
- En esta APP inclui tambien un /aboutme para que puedas ver mis otros proyectos
- en /about this site puedes ver el formulario de contacto y tambien explicacion de como crear cuenta, publicacion y etc...

## Authors

- [@renataCardoli](https://github.com/RenataCardoli/)

# Opciones de Mejora en la APP

- una vez logeado al cambiar la URL para 'http://127.0.0.1:8000/login/' la pagina presenta el formulario de login. - corregir - 
- implementar reset contraseña, hubo por error en el smtp.django ( Gmail no acepta less secure apps to access gmail accounts )
- Incluir Like y Nombre de usuario en los comentarios. 

## 🛠 Skills
HTML, CSS, Javascript, Bootstrap, SCSS, AJAX and also Python and Django. 
