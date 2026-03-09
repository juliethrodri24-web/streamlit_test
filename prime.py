import math

def is_prime(n):
    """calcula los numeros primos del 1 al 100"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():

    """tiene toda la lógica principal"""

    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()

# Crea la función sign()
def sign(x):
    """Devuelve el signo de número."""
    if x == None:
        return None
    if x < 0:
        return -1
    return 1

# Prueba la función sign()
def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None