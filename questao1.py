import numpy as np # type: ignore # Importando a biblioteca de computação numérica

# Definição de vetores
v = []
v.append(np.array([1, 1j, 1], dtype='complex128'))
v.append(np.array([4, 3, 2], dtype='complex128'))
v.append(np.array([2+3j, complex(np.sqrt(3), np.pi), 3], dtype='complex128'))
v.append(np.array([complex(np.cos(np.pi/2), np.sin(np.pi/2)), 1, complex(np.exp(-2), 0)], dtype='complex128'))

beta = []
beta.append(3+4j)
beta.append(np.exp(-np.pi/2) + 0j)
beta.append(-12345+28413j)

# Funções
def soma(u, v):
    #Alterado:
    w = u + v #soma de vetores
    return w #retorna a soma

def verifica_soma(u, v):
    #fazer toda a lógica para ver se a soma dos vetores resultam em outro vetor do mesmo conjunto
    w = soma(u, v)
    if w.shape == (3,) and w.dtype == 'complex128': #ver se o vetor tem o mesmo tamanho (3) e o tipo dele
        return True
    return False

print('Testando fechamento da soma:')
for i in range(len(v)):
  for k in range(len(v) - i - 1):
    print(verifica_soma(v[i], v[k+i+1]) , ' => ', v[i], ' , ', v[k+i+1])


def produto(beta, u):
    #alterado:
    modulo_beta = np.abs(beta)
    w = modulo_beta * u #multiplicação de um vetor por um escalar complexo
    return w #retorna a multiplicação

def verifica_produto(beta, u):
    #fazer toda a lógica para ver se o produto de um escalar e um vetor resultam em outro vetor do mesmo conjunto
    w = produto(beta, u)
    if w.shape == (3,) and w.dtype == 'complex128': #para verificar o tamanho do array e o tipo
        return True 
    return False

print('--------------------------------------')
print('Testando fechamento do produto escalar:')
for i in range(len(beta)):
  for k in range(len(v)):
    print(verifica_produto(beta[i], v[k]), ' => ', beta[i], ' , ', v[k])
    
    
    
# proponha o vetor nulo
    #alterado:
    nulo = np.zeros(3, dtype='complex128')

def verifica_nulo(v):
  # Já implementado, não se preocupar
    return np.all(soma(v, nulo) == v) # retorna True se todos valores de v+nulo forem iguais a v e False caso contrário

print('--------------------------------------')
print('Testando vetor nulo:')
for i in range(len(v)):
  print(verifica_nulo(v[i]), ' => ', v[i])
  
  
# proponha o vetor inverso
def inverso(v):
    w = -v
    return w

def verifica_inverso(v):
  # Já implementado, não se preocupar
    return np.all(soma(v, inverso(v)) == nulo) # retorna True se todos valores de v+inverso(v) forem iguais a nulo e False caso contrário

print('--------------------------------------')
print('Testando vetor inverso:')
for i in range(len(v)):
  print(verifica_inverso(v[i]), ' => ', v[i])
  
  
def verifica_comutatividade(u, v):
    soma1 = soma(u, v) #usa a função soma para u + v
    soma2 = soma(v, u) #usa a função soma para v + u
    return np.array_equal(soma1, soma2) #analisa se os resultados são iguais, se sim, true, caso não, false

print('--------------------------------------')
print('Testando comutatividade:')
for i in range(len(v)):
  for k in range(len(v) - i - 1):
    print(verifica_comutatividade(v[i], v[k+i+1]) , ' => ', v[i], ' , ', v[k+i+1]) # type: ignore


def verifica_associatividade(u, v, w):
    soma1 = soma(u, soma(v, w)) #Chama a função soma duas vezes. Primeiro somando v + w e na segunda o u + o resultado de v + w
    soma2 = soma(soma(u, v), w) #Chama a função soma duas vezes. Primeiro somando u + v e na segunda o resultado de (u + v) + w
    return np.array_equal(soma1, soma2) #analisa se os resultados são iguais, se sim, true, caso não, false

print('--------------------------------------')
print('Testando associatividade:')
for i in range(len(v)):
  for k in range(len(v) - i - 1):
    for l in range(len(v) - i - k - 2):
      print(verifica_associatividade(v[i], v[k+i+1], v[k+i+l+2]) , ' => ', v[i], ' , ', v[k+i+1], ' , ', v[k+i+l+2])
   
        
def verifica_distributividade_1(beta, u, v):
    resultado1 = produto(beta, soma(u, v)) #Chama a função produto, passando como paramentro o beta e a função soma, somando u + v
    resultado2 = soma(produto(beta, u), produto(beta, v)) #Chama a função soma, passando como paramentro 2x a função produto, multiplicando o mesmo escalar com os vetores u e v, respectivamente
    return np.array_equal(resultado1, resultado2) #analisa se os resultados são iguais, se sim, true, caso não, false

print('--------------------------------------')
print('Testando distributividade 1:')
for i in range(len(beta)):
  for k in range(len(v)):
    for l in range(len(v) - k - 1):
      print(verifica_distributividade_1(beta[i], v[k], v[k+l+1]), ' => ', beta[i], ' , ', v[k], ' , ', v[k+l+1])


def verifica_distributividade_2(beta, gama, u):
    resultado1 = produto(beta + gama, u) #Chama a função produto com os paramentros beta + gama e o vetor u
    resultado2 = soma(produto(beta, u), produto(gama, u)) #Chama a função soma com os paramentros sendo 2x a função produto, que é chamada com os paramentros escalar1 e u, escalar2 e u
    return np.array_equal(resultado1, resultado2) #analisa se os resultados são iguais, se sim, true, caso não, false

print('--------------------------------------')
print('Testando distributividade 2:')
for i in range(len(beta)):
  for k in range(len(beta) - i - 1):
    for l in range(len(v)):
      print(verifica_distributividade_2(beta[i], beta[i+k+1], v[l]), ' => ', beta[i], ' , ', beta[i+k+1], ' , ', v[l])


def verifica_distributividade_3(beta, gama, u):
    resultado1 = produto(beta, produto(gama, u)) #chama a função produto com os paramentros escalar1 e a função produto, com os paramentros escalar2 e u
    resultado2 = produto(beta * gama, u) #chama a função produto com o paramentro beta*gama e u
    return np.array_equal(resultado1, resultado2) #analisa se os resultados são iguais, se sim, true, caso não, false

print('--------------------------------------')
print('Testando distributividade 3:')
for i in range(len(beta)):
  for k in range(len(beta) - i - 1):
    for l in range(len(v)):
      print(verifica_distributividade_3(beta[i], beta[i+k+1], v[l]), ' => ', beta[i], ' , ', beta[i+k+1], ' , ', v[l])


def verifica_escalar_unitario(u):
    resultado = produto(1, u) #chama a função produto com os paramentros 1 e u
    return np.array_equal(resultado, u) #analisa se os resultados são iguais, se sim, true, caso não, false

print('--------------------------------------')
print('Testando o axioma do escalar unitário:')
for i in range(len(v)):
      print(verifica_escalar_unitario(v[i]), ' => ', v[i])
