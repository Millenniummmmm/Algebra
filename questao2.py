import numpy as np

def gauss(A, B):

    n = len(A)
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)

    A = np.hstack([A, B.reshape(-1, 1)])

    for i in range(n):
        p = np.argmax(np.abs(A[i:, i])) + i
        if A[p, i] == 0:
            raise Exception("Sistema singular ou indefinido.")

        if p != i:
            A[[i, p]] = A[[p, i]]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    # Substituição Reversa
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = (A[i, -1] - np.sum(A[i, i + 1:n] * X[i + 1:])) / A[i, i]

    return X

def combinacao(vetores, vetor_alvo):
  
    n = len(vetor_alvo)  # Tamanho do vetor alvo
    A = np.array(vetores)  # Matriz composta pelos vetores fornecidos
    B = np.array(vetor_alvo)  # Vetor alvo

    try:
        # Tentar resolver o sistema usando a função gauss
        coef = gauss(A, B)
        resultado = True  # Se conseguiu resolver, é combinação linear
    except Exception as e:
        # Se deu erro na função gauss, não é combinação linear
        resultado = False
        coef = None

    return resultado, coef


print('Caso 1')
vetores = np.array([[0,0,1],[0,1,0],[1,0,0]])
vetor_alvo = np.array([1,2,3])

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print('Caso 2')
vetores = np.array([[3.5, 2.1, 2, 4], [5.25, 3.15, 3.0, 6.0], [4.2, 2.52, 2.4, 4.8], [-4.9, -2.94, -2.8, -5.6]])
vetor_alvo = np.array([1,2,3,4])

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print('Caso 3')
vetores = np.array([[np.exp(3), np.exp(-2), np.exp(-4), np.sin(np.pi/2), np.cos(np.pi/6), 0], [5.43, 13, 2.5, 1, 1, 2], [8.145, 19.5, 3.75, 1.5, 1.5, 3.], [1, 4, 7.8, np.tan(np.pi/6), np.tanh(1), 3], [1, 4, 7.8, np.tan(np.pi/6), np.tanh(1), 3]])
vetor_alvo = np.array([1,2,3,4,5,6])

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")
