""" 
    Hogsmeade (X: 34, Y: 110, Z: 220)
    Kakariko (X: 0, Y: 64, Z: 0)
    Solitude (X: 140, Y: 200, Z: 456)
"""

def euclidian_distance(x1: int, x2: int, z1: int, z2: int):
    return ((x1 - x2)**2 + (z1 - z2)**2)**(1/2)

x = int(input())
z = int(input())

Hogsmeade_distance = float(euclidian_distance(x, 34, z, 220))
Kakariko_distance = float(euclidian_distance(x, 0, z, 0))
Solitude_distance = float(euclidian_distance(x, 140, z, 456))

print(f"Distancia para Hogsmeade: {Hogsmeade_distance:.2f}")
print(f"Distancia para Kakariko: {Kakariko_distance:.2f}")
print(f"Distancia para Solitude: {Solitude_distance:.2f}")