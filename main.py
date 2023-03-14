from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['movies']) #filtrado de peliculas por categoria
def get_movies_by_category(category: str, year: int):
    return [ item for item in movies if item['category'] == category ]

@app.post('/movies', tags=['movies']) 
# tags: nombre de la pagina pestanha
# body para que la peticion no llegue como query
def create_movie(id: int = Body(), 
                 title: str = Body(), 
                 overview:str = Body(), 
                 year:int = Body(), 
                 rating: float = Body(), 
                 category: str = Body()):
    movies.append({ #para modificar el diccionario movies
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies