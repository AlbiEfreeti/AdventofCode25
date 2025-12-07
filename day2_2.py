def es_invalido(n):
    s = str(n)
    L = len(s)

    for k in range(1, L):
        if L % k == 0:
            trozo = s[:k]
            if trozo * (L // k) == s:
                return True

    return False



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
