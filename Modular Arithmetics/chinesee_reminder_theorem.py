def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"Modular reseverse doesn't exists for {a} mod {m}")
    return x % m


def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        raise ValueError("Lists must has the same lenght")
    if not remainders:
        raise ValueError("Lists can't be empty")

    N = 1
    for n in moduli:
        if n <= 0:
            raise ValueError("Modules has to be positives")
        N *= n

    x = 0
    for a_i, n_i in zip(remainders, moduli):
        N_i = N // n_i
        inv = modinv(N_i, n_i)
        x += a_i * N_i * inv

    return x % N, N

remainders = [2, 3, 5]
moduli = [5, 11, 17]

x, N = crt(remainders, moduli)
print(f"x ≡ {x} (mod {N})")