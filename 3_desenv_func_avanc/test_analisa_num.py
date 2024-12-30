import pytest 

from main import analisar_numeros


@pytest.mark.parametrize("list, result", [
    ([1, 2, 3, 4, 5], {'media':3, 'maior': 5, 'menor':1, 'pares':2}),
    ([4, 2, 70, 30, 22], {'media':25.6, 'maior': 70, 'menor':2, 'pares':5}),
    ([7, 52, 33, 56, 5, 10, 13, 33, 19], {'media':25.33, 'maior': 56, 'menor':5, 'pares':3}),
    ([60, 31, 70.2], {'media':53.73, 'maior': 70.2, 'menor':31, 'pares':1}),
])

def test_analisa_nums(list, result):

    assert analisar_numeros(list) == result



