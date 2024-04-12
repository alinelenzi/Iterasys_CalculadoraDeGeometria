import pytest
from calculadoraGeometrica import calculaAreaQuadrado

@pytest.mark.parametrize('lado, resultado_esperado',
                        [
                            (2, 4),
                            (5, 25),
                            (6.5, 42.25),
                            (-1, "O lado do quadrado deve ser maior que zero"),
                            (0, "O lado do quadrado deve ser maior que zero")
                        ]
                        )

def test_calculaAreaQuadrado_array(lado, resultado_esperado):
    resultado_obtido = calculaAreaQuadrado(lado)
    assert resultado_obtido == resultado_esperado

