def sumar(a, b):
    return int(a) + int(b)

def restar(a, b):
    return int(a) - int(b)

if __name__ == "__main__":
    import sys
    print(sumar(sys.argv[1], sys.argv[2]))
    print(restar(sys.argv[1], sys.argv[2]))
