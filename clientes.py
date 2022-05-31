from array import array
from unicodedata import category
usuarios = [{
    "id": "1",
    "nombre": "Miguel",
    "apellido": "escobar",
    "username": "Miguelito123",
    "phone": 3015605651
},
{
    "id": "2",
    "nombre": "Angel",
    "apellido": "ocampo",
    "username": "Angelito123",
    "phone": 3015605654
},
{
    "id": "3",
    "nombre": "Carlos",
    "apellido": "ocampo",
    "username": "carlitos123",
    "phone": 3015605654
   
    
}]

# print(usuarios)

extra = [{
    "id": "1",
    "nombre": "Miguel",
    "apellido": "escobar",
    "datos_estra": {
        "habilidades": "qefbnofuwr",
        "educacion": "Chimbis",
        "certificacion": "good",
    }
},
{
    "id": "2",
    "nombre": "Angel",
    "apellido": "ocampo",
    "datos_estra": {
        "habilidades": "qefbnofuwr",
        "educacion": "Chimbis",
        "certificacion": "good",
    },
}]


productos=[
    {
        "id": "1",
        "nombre_product": "Html, CSS, JavaScript",
        "descripcion_product": "bueno, bonito y barato",
        "categoria": "3",
        "price": "10000000",
        "estrellas": 5
    },
    {
        "id": "2",
        "nombre_product": "POO",
        "descripcion_product": "bueno, bonito y barato",
        "categoria": "7",
        "price": "10000000",
        "estrellas": 5
    },
    {
        "id": "3",
        "nombre_product": "Licenciatura en enseñanza",
        "descripcion_product": "bueno, bonito y barato",
        "categoria": "2",
        "price": "10000000",
        "estrellas": 5
    }
]

categorias=[
    {
        "id": "1",
        "nombre": "diseño"
    },
    {
        "id": "2",
        "nombre": "programacion"
    },
    {
        "id": "3",
        "nombre": "educacion"
    }
]

membresia=[
    {
        "id": "1",
        "nombre_membresia": "basic" 
    },
    {
        "id": "2",
        "nombre_membresia": "estandar"
    },
    {
        "id": "3",
        "nombre_membresia":  "premium"
    }
]

# usuarios= proto + productos
# print(usuarios)