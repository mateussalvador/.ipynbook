"""
1. Medidor de Tempo (Dificuldade: Fácil)
Objetivo: Crie um decorador chamado @timer que mede o tempo de execução de uma função e imprime a duração em segundos no final.
Dica: Use o módulo time (time.time() ou time.perf_counter()).
Exemplo de Uso:
"""
import time
import functools

def decorador(funcao):
    @functools.wraps(funcao)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função {funcao.__name__} demorou {fim - inicio} segundos para executar.")
    return wrapper

@decorador
def somar(x, y):
    time.sleep(2)
    print(x + y)

somar(5, 3)