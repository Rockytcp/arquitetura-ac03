import abc
from unittest import TestCase, main


class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado



class OperacaoFabrica(object):

    def criar(self, operador):
        if operador == 'soma':
            return Soma()
        elif operador == 'subtracao':
            return Subtracao()
        elif operador == 'divisao':
            return Divisao()
        elif operador == 'multiplicacao':
            return Multiplicacao()
        else: 
            return None


class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass
    
class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado
    
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        if valor2 == 0:
            return 'impossivel dividir por 0'
        resultado = valor1 / valor2
        return resultado


class Testes(TestCase):

    def test_soma(self):
        calculador = Calculadora()
        resultado = calculador.calcular(2,3,'soma')
        self.assertEqual(resultado, 5)
    
    def test_subtracao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(2,4,'subtracao')
        self.assertEqual(resultado, -2)
    
    def test_multiplicacao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(2,5,'multiplicacao')
        self.assertEqual(resultado, 10)

    def test_divisao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(4,2,'divisao')
        self.assertEqual(resultado, 2)

    def test_operacao(self):
        calculador = Calculadora()
        resultado = calculador.calcular(4,2, 'subtrair')
        self.assertEqual(resultado, 0)

    def test_divisao_por_zero(self):
        calculador = Calculadora()
        resultado = calculador.calcular(5,0, 'divisao')
        self.assertEqual(resultado, 'impossivel dividir por 0')

    
calculador = Calculadora()
calcular = calculador.calcular(5,5, 'soma')
print(calcular)

if __name__ == '__main__':
    main()
