"""
    x = (a + b + (|a - b|)) / 2
    permitido utilizar funções externas para calcular o valor absoluto de um número (abs(), em Python).
    1. Luiz definiu que o programa não poderia utilizar nenhuma estrutura condicional em seu código, como IF e outras;
    2. Pedro proibiu a utilização de quaisquer funções de bibliotecas externas para calcular o máximo da quantidade de diamantes do vencedor;
    3. Arthur falou que, para encontrar o valor final da quantidade máxima de diamantes, seria obrigatório utilizar a seguinte função para encontrar o máximo entre 2 valores: x = (a + b + (|a - b|)) / 2.
"""

def biggest_number(a: int, b: int):
    return (a + b + abs(a - b)) // 2

a = int(input()) # Arthur
l = int(input()) # Luiz
p = int(input()) # Pedro
h = int(input()) # Hora

a_total = a * h
l_total = l * h
p_total = p * h

max_a_l = biggest_number(a_total, l_total)
max_al_p = biggest_number(max_a_l, p_total)

print(max_al_p)