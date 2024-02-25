import csv

marca, modelo, distancia_entre_eixos, altura, peso_total_padrao, tamanho_motor, potencia_motor, rotacoes_maximas_minuto, eficiencia_combustivel_cidade, eficiencia_combustivel_rodovia, preco = ([] for i in range(11))

with open('Dados.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    for i, row in enumerate(reader):
        # Uso da Amostragem Aleatória Sistemática de 5 em 5
        #if i % 5 == 0:
            marca.append(row[2])
            modelo.append(row[5])
            distancia_entre_eixos.append(row[8])
            altura.append(row[11])
            peso_total_padrao.append(row[12])
            tamanho_motor.append(row[15])
            potencia_motor.append(row[20])
            rotacoes_maximas_minuto.append(row[21])
            eficiencia_combustivel_cidade.append(row[22])
            eficiencia_combustivel_rodovia.append(row[23])
            preco.append(row[24])

def shell_sort(vetor):
    
    n = len(vetor)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = vetor[i]
            j = i
            while j >= gap and vetor[j - gap] > temp:
                vetor[j] = vetor[j - gap]
                j -= gap
            vetor[j] = temp
        gap //= 2

    return vetor


print(shell_sort(altura))


"""
for item in marca:
    print(item)

for item in modelo:
    print(item)

for item in distancia_entre_eixos:
    print(item)
    
for item in altura:
    print(item)

for item in peso_total_padrao:
    print(item)
    
for item in tamanho_motor:
    print(item)

for item in potencia_motor:
    print(item)

for item in rotacoes_maximas_minuto:
    print(item)

for item in eficiencia_combustivel_cidade:
    print(item)

for item in eficiencia_combustivel_rodovia:
    print(item)

for item in preco:
    print(item)
"""
