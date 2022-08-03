matriz = [['.' for j in range(20)] for i in range(20)]
l, c = input().split()
l = int(l)
c = int(c)
matriz[l][c] = "+"
comando = input().split()
while comando[0] != "F":
    if comando[0] == "A":
        matriz[l][c] = "#"
    else:
        dist = int(comando[1])
        if comando[0] == "N":
            for n in range(dist):
                l = l - 1
                if matriz[l][c] == ".":
                    matriz[l][c] = "+"
        elif comando[0] == "S":
            for n in range(dist):
                l = l + 1
                if matriz[l][c] == ".":
                    matriz[l][c] = "+"
        elif comando[0] == "L":
            for n in range(dist):
                c = c + 1
                if matriz[l][c] == ".":
                    matriz[l][c] = "+"
        elif comando[0] == "O":
            for n in range(dist):
                c = c - 1
                if matriz[l][c] == ".":
                    matriz[l][c] = "+"
    comando = input().split()

for i in matriz:
    print(" ".join(i))
