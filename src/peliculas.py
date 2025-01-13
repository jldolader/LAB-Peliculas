import csv
from datetime import date, datetime
from typing import Dict, List, NamedTuple, Set, Tuple

from numpy import mean

Pelicula = NamedTuple("Pelicula", [("fecha_estreno", date), ("titulo", str), ("director", str), ("generos", list[str]),
    ("duracion", int), ("presupuesto", int), ("recaudacion", int), ("reparto", list[str])])


def lee_peliculas(ruta: str) -> List[Pelicula]:
    with open(ruta, mode = 'r', encoding = 'utf-8') as f:
        r = csv.reader(f, delimiter = ';')
        next(r)
        return [Pelicula(
            fecha_estreno = datetime.strptime(d[0], '%d/%m/%Y').date(),
            titulo = str(d[1]),
            director = str(d[2]),
            generos = [g for g in (d[3].split(', '))],
            duracion = int(d[4]),
            presupuesto = int(d[5]),
            recaudacion = int(d[6]),
            reparto = [a for a in (d[7].split(', '))]
        ) for d in r]

def pelicula_mas_ganancias(pelis: List[Pelicula], genero: str = None) -> Tuple[str, int]:
    pelis = sorted(pelis, key=lambda p: p.recaudacion - p.presupuesto, reverse=True)
    for p in pelis:
        if genero is None or genero.lower() in (g.lower() for g in p.generos):
            return (p.titulo, p.recaudacion - p.presupuesto)

def media_presupuesto_por_genero(pelis: List[Pelicula]) -> Dict[str, int]:
    generos_presupuestos = {}
    for p in pelis:
        for genero in p.generos:
            if genero not in generos_presupuestos:
                generos_presupuestos[genero] = []
            generos_presupuestos[genero].append(p.presupuesto)
    return {genero: int(mean(presupuestos)) for genero, presupuestos in generos_presupuestos.items()}

def peliculas_por_actor(pelis: List[Pelicula], año_inicial: int = None, año_final: int = None) -> Dict[str, int]:
    actores_peliculas = {}
    for peli in pelis:
        for actor in peli.reparto:
            if (año_inicial is None or peli.fecha_estreno.year <= año_inicial) and (año_final is None or  peli.fecha_estreno.year <= año_final):
                if actor not in actores_peliculas:
                    actores_peliculas[actor] = []
                actores_peliculas[actor].append(peli.titulo)
    
    return {actor: len(peliculas) for actor, peliculas in actores_peliculas.items()}

def actores_mas_frecuentes(pelis: List[Pelicula], n: int, año_inicial: int = None, año_final: int = None) -> List[str]:
    peliculas_por_actor_dict = peliculas_por_actor(pelis, año_inicial, año_final)
    actores_ordenados = sorted(peliculas_por_actor_dict.items(), key=lambda x: (-x[1], x[0]))
    return [actor for actor, _ in actores_ordenados[:n]]

def recaudacion_total_por_año(pelis: List[Pelicula], generos: Set[str] = None) -> Dict[str, int]:
    recaudacion_por_año = {}
    for peli in pelis:
        if generos is None or any(genero in generos for genero in peli.generos):
            año = str(peli.fecha_estreno.year)
            if año not in recaudacion_por_año:
                recaudacion_por_año[año] = 0
            recaudacion_por_año[año] += peli.recaudacion
    return recaudacion_por_año

def incrementos_recaudacion_por_año(pelis: List[Pelicula], generos: Set[str] = None) -> List[int]:
    recaudacion_por_año = recaudacion_total_por_año(pelis, generos)
    años_ordenados = sorted(recaudacion_por_año.keys())
    incrementos = []
    for i in range(1, len(años_ordenados)):
        incremento = recaudacion_por_año[años_ordenados[i]] - recaudacion_por_año[años_ordenados[i - 1]]
        incrementos.append(incremento)
    return incrementos
