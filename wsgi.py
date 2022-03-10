from pymongo import MongoClient
from flask import Flask, render_template, url_for, redirect,request
import static_data
import re

client = MongoClient(host = 'localhost')
db = client['detlos_reg']

#Colecciones
datos_usuarios = db['registros']

app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        find_user = datos_usuarios.find_one({"username": username})

        if find_user["username"] == username and find_user["password"] == password:
            print(str(find_user))
            return ("Logeado")
        return ("Credenciales incorrectas")

    return render_template("login.html")

@app.route("/register",methods=['GET', 'POST'])
def register():
    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido_1 = request.form["apellido_1"]
        apellido_2 = request.form["apellido_2"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        phone = request.form["phone"]
        city = request.form["city"]
        state = request.form.get("state")
        address = request.form["address"]

        data = (
            nombre,
            apellido_1,
            apellido_2,
            username,
            password,
            confirm_password,
            phone,
            city,
            state,
            address
        )

        data2 = {
            'nombre':nombre,
            'apellido_1':apellido_1,
            'apellido_2':apellido_2,
            'username':username,
            'password':password,
            'phone':phone,
            'city':city,
            'state':state,
            'address':address
        }


        strong_password = static_data.check_password(password)
        
        if  "" in data or state not in static_data.states:
            return ("Ingresa todos los campos")

        if password != confirm_password:
            return ("Las contraseÃ±as no coinciden")
        
        if strong_password != True:
            return strong_password

        if not (re.search("\d\d\d-\d\d\d-\d\d\d\d",phone)):
            return("Numero de telefono invalido")

        if (re.search("\d", nombre)):
            return("Nombre no puede llevar numeros")

        if (re.search("\d", apellido_1)):
            return("Apellido 1 no puede llevar numeros")

        if (re.search("\d", apellido_2)):
            return("Apellidp 2 no puede llevar numeros")


        all_usernames = datos_usuarios.find()
        for x in all_usernames:
            if data2['username'] in x['username']:
                return("Username duplicado")

        
        datos_usuarios.insert_one(data2)
        
        

        return('Registrado')
    return render_template("register.html",list = static_data.states)

if __name__ == "__main__":
    app.run(debug=True)