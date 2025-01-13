import csv
from datetime import date, datetime
from typing import Dict, List, NamedTuple, Set, Tuple

Pelicula = NamedTuple("Pelicula", [("fecha_estreno", date), ("titulo", str), ("director", str), ("generos", list[str]),
    ("duracion", int), ("presupuesto", int), ("recaudacion", int), ("reparto", list[str])])


def lee_peliculas(ruta: str) -> List[Pelicula]:
    with open(ruta, mode = 'r', encoding = 'utf-8') as f:
        r = csv.reader(f, delimiter = ';')
        next(r)
                
        return [Pelicula(
            fecha_estreno = datetime.strptime(d[0], '%d/%m/%Y').date(),
            titulo = d[1],
            director = d[2],
            generos = [g for g in (d[3].split(', '))],
            duracion = d[4],
            presupuesto = d[5],
            recaudacion = d[6],
            reparto = [a for a in (d[6].split(', '))]
        ) for d in r]

def pelicula_mas_ganancias(pelis: List[Pelicula], genero: str = None) -> Tuple[str, int]:
    pass

def media_presupuesto_por_genero(pelis: List[Pelicula]) -> Dict[str, int]:
    pass

def peliculas_por_actor(pelis: List[Pelicula], año_inicial: int = None, año_final: int = None) -> Dict[str, int]:
    pass

def actores_mas_frecuentes(pelis: List[Pelicula], n: int, año_inicial: int = None, año_final: int = None) -> List[str]:
    pass

def recaudacion_total_por_año(pelis: List[Pelicula], generos: Set[str] = None) -> Dict[str, int]:
    pass

def incrementos_recaudacion_por_año(pelis: List[Pelicula], generos: Set[str] = None) -> List[int]:
    pass
