"""
Arthur ->  10
Luiz   ->  30
Pedro  -> 100
"""

tantan_price = int(input())


if tantan_price > 30 and tantan_price < 100:
    print("Pedro")
else:
    if tantan_price > 10 and tantan_price <= 30:
        print("Luiz")
    elif tantan_price > 0 and tantan_price <= 10:
        print("Arthur")
    else:
        print("Nenhum")