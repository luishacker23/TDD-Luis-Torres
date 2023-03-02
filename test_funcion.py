from funcion import encontrar_menor

def test_numero_menor():
    assert encontrar_menor([3,12,6,42,2]) == 2
    assert encontrar_menor([32,2,66,32,12]) == 2
    assert encontrar_menor([32,26,22,15,12]) == 12