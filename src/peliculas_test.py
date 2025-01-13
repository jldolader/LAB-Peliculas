from peliculas import *

def test_lee_peliculas(ruta):
    print('TEST PELICULAS')
    peliculas = lee_peliculas(ruta)
    print(f'Total registros leídos: {len(peliculas)}')
    print(f'Mostrando los tres primeros registros:')
    for p in peliculas[:3]:
        print('\t', p)
    return peliculas

def test_pelicula_mas_ganancias(pelis, genero=None):
    print(f'Test de pelicula_mas_ganancias (genero={genero}):')
    print(pelicula_mas_ganancias(pelis, genero))
    
def test_media_presupuesto_por_genero(pelis):
    print('Test de media_presupuesto_por_genero:')
    
    print(media_presupuesto_por_genero(pelis))
def test_peliculas_por_actor(pelis, año_inicial=None, año_final=None):
    print(f'Test de peliculas_por_actor (año_inicial={año_inicial}, año_final={año_final}):')
    
    peliculas = peliculas_por_actor(pelis, año_inicial, año_final)
    
    for actor in ['Robert Downey Jr.', 'Christian Bale', 'Adam Driver']:
        print(f'{actor}: {peliculas.get(actor, 0)}')
        
def test_actores_mas_frecuentes(pelis, n, año_inicial=None, año_final=None):
    print(f'Test de actores_mas_frecuentes (n={n}, año_inicial={año_inicial}, año_final={año_final}):')
    print(actores_mas_frecuentes(pelis, n, año_inicial, año_final))
    
def test_recaudacion_total_por_año(pelis, generos=None):
    print(f'Test de recaudacion_total_por_año (generos={generos}):')
    print(recaudacion_total_por_año(pelis, generos))
    
def test_incrementos_recaudacion_por_año(pelis, generos=None):
    print(f'Test de incrementos_recaudacion_por_año (generos={generos}):')
    print(incrementos_recaudacion_por_año(pelis, generos))
    
if __name__ == '__main__':
    pelis = test_lee_peliculas('data/peliculas.csv')
    test_pelicula_mas_ganancias(pelis)
    test_pelicula_mas_ganancias(pelis, genero='Drama')
    #test_media_presupuesto_por_genero(pelis)
    #test_peliculas_por_actor(pelis)
    #test_peliculas_por_actor(pelis, año_inicial=2010, año_final=2020)
    #test_actores_mas_frecuentes(pelis, n=3, año_inicial=2005, año_final=2015)
    #test_recaudacion_total_por_año(pelis)
    #test_recaudacion_total_por_año(pelis, generos={'Drama', 'Acción'})
    #test_incrementos_recaudacion_por_año(pelis)
    #test_incrementos_recaudacion_por_año(pelis, generos={'Drama', 'Acción'})