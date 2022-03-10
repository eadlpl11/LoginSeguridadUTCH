import re

states = ["Aguascalientes",
"Baja California",
"Baja California Sur",
"Campeche",
"Chiapas",
"Chihuahua",
"Ciudad de México",
"Coahuila",
"Colima",
"Durango",
"Estado de México",
"Guanajuato",
"Guerrero",
"Hidalgo",
"Jalisco",
"Michoacán",
"Morelos",
"Nayarit",
"Nuevo León",
"Oaxaca",
"Puebla",
"Querétaro",
"Quintana Roo",
"San Luis Potosí",
"Sinaloa",
"Sonora",
"Tabasco",
"Tamaulipas",
"Tlaxcala",
"Veracruz",
"Yucatán",
"Zacatecas"]

def check_password(password):
    #patron = re.compile(r'')    
    if (len(password) < 8):
        return("La contraseña no es mayor a 8 caracteres")
    elif re.search(r"[$&+,:;=?@#|'<>.^*()%!-]",password) is None:
        return("La contraseña necesita un caracter especial")
    elif re.search(r"\d",password) is None:
        return("La contraseña necesita numero")
    elif re.search("[A-Z]",password) is None:
        return("La contraseña necesita al menos una mayúscula")
    else:
        return True