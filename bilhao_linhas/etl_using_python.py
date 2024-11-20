from csv import reader
from collections import defaultdict
import time
from pathlib import Path
from pprint import pprint

PATH_TO_DATA = Path('data//measurements.txt')


def processar_temperaturas(path_to_data: Path) -> dict:
    """
    Processa as temperaturas de estações meteorológicas e retorna um dicionário
    """
    print('Iniciando processamento temperaturas...')
    
    start_time = time.time()

    temperaturas_por_estacao = defaultdict(list)
    
    with open(path_to_data, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            estacao, temp = str(row[0]), float(row[1])
            temperaturas_por_estacao[estacao].append(temp)
    
    print('Processamento de temperaturas concluído.Calculando estatistico...')
    
    results = {}
    
    for estacao, temps in temperaturas_por_estacao.items():
        min_temp = min(temps)
        max_temp = max(temps)
        mean_temp = sum(temps) / len(temps)
        results[estacao] = (min_temp, max_temp, mean_temp)
        
    print('Cálculo de médias concluído.')
    
    print('Ordenando resultados...')
    
    sorted_results = dict(sorted(results.items()))
    
    formatted_results = {estacao: f'{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}' for estacao, (min_temp, max_temp, mean_temp) in sorted_results.items()}
    
    elapsed_time = time.time() - start_time
    
    print(f'Processamento de temperaturas concluído em {elapsed_time:.2f} segundos.')
    
    return formatted_results


if __name__ == '__main__':
    results = processar_temperaturas(PATH_TO_DATA)
    