import pytest;
from calculadoraGeometrica import calculaAreaRetangulo;

@pytest.mark.parametrize('base, altura, resultado_esperado',
                        [
                            (3,1,3),
                            (45.5,10,455),
                            (0,5,"A base e altura do retangulo devem ser maiores que zero"),
                            (-1,5,"A base e altura do retangulo devem ser maiores que zero"),
                            (8,-2,"A base e altura do retangulo devem ser maiores que zero"),
                            (9,0,"A base e altura do retangulo devem ser maiores que zero")
                        ]
                        )

def test_calculaAreaTriangulo_array(base, altura, resultado_esperado):
    resultado_obtido = calculaAreaRetangulo(base, altura);
    assert resultado_obtido == resultado_esperado