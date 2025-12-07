def es_invalido(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mitad = len(s) // 2
    return s[:mitad] == s[mitad:]


def main():
    total = 0
    with open("input2.txt") as f:
        contenido = f.read().strip()
        rangos = contenido.split(",")

        for r in rangos:
            a, b = map(int, r.split("-"))
            for x in range(a, b + 1):
                if es_invalido(x):
                    total += x

    print("Suma total de IDs inválidos:", total)


if __name__ == "__main__":
    main()
