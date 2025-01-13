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
    print(peliculas)
        
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
    print("\n" + "-"*50 + "\n")
    test_pelicula_mas_ganancias(pelis)
    print("\n" + "-"*50 + "\n")
    test_pelicula_mas_ganancias(pelis, genero='Drama')
    print("\n" + "-"*50 + "\n")
    test_media_presupuesto_por_genero(pelis)
    print("\n" + "-"*50 + "\n")
    test_peliculas_por_actor(pelis)
    print("\n" + "-"*50 + "\n")
    test_peliculas_por_actor(pelis, 2010, 2020)
    print("\n" + "-"*50 + "\n")
    test_actores_mas_frecuentes(pelis, 3, 2005, 2015)
    print("\n" + "-"*50 + "\n")
    test_recaudacion_total_por_año(pelis)
    print("\n" + "-"*50 + "\n")
    test_recaudacion_total_por_año(pelis, {'Drama', 'Acción'})
    print("\n" + "-"*50 + "\n")
    test_incrementos_recaudacion_por_año(pelis)
    print("\n" + "-"*50 + "\n")
    test_incrementos_recaudacion_por_año(pelis, {'Drama', 'Acción'})