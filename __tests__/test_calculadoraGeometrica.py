import pytest
from calculadoraGeometrica import calculaAreaQuadrado, calculaAreaRetangulo, calculaAreaTriangulo

lado = 5;
base = 3;
altura = 6;

def test_calculaAreaQuadrado():
    resultado_esperado = 25;

    resultado_obtido = calculaAreaQuadrado(lado)

    assert resultado_obtido == resultado_esperado

def test_calculaAreaRetangulo():
    resultado_esperado = 18;

    resultado_obtido = calculaAreaRetangulo(base, altura);

    assert resultado_obtido == resultado_esperado;

def test_calculaAreaTriangulo():
    resultado_esperado = 9;

    resultado_obtido = calculaAreaTriangulo(base, altura)

    assert resultado_obtido == resultado_esperado;