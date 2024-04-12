import pytest;
from calculadoraGeometrica import calculaAreaTriangulo;

@pytest.mark.parametrize('base, altura, resultado_esperado',
                        [
                            (3, 8, 12),
                            (10, 45.5, 227.5),
                            (0, 5, "A base e altura do triangulo devem ser maiores que zero"),
                            (-1, 5, "A base e altura do triangulo devem ser maiores que zero"),
                            (8, -2, "A base e altura do triangulo devem ser maiores que zero"),
                            (9, 0, "A base e altura do triangulo devem ser maiores que zero")
                        ]
                        )
def test_calculaAreaTriangulo_array(base, altura, resultado_esperado):
    resultado_obtido = calculaAreaTriangulo(base, altura)
    assert resultado_obtido == resultado_esperado