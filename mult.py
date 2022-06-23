def multiplicar(a, b):
    return int(a)*int(b)

def dividir(a, b):
    return int(a)/int(b)

if __name__ == "__main__":
    import sys
    print(multiplicar(sys.argv[1], sys.argv[2]))
    print(dividir(sys.argv[1], sys.argv[2]))
