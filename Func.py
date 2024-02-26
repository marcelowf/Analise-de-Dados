import csv
import math
import matplotlib.pyplot as plt

def plotar_tabela_distribuicao_frequencias(intervalos, ponto_medio, frequencia_acumulada):
    plt.figure(figsize=(10, 6))
    plt.bar(ponto_medio, frequencia_acumulada, width=amplitude_classes, align='center', alpha=0.7)
    plt.xlabel('Intervalo')
    plt.ylabel('Frequência Acumulada')
    plt.title('Tabela de Distribuição de Frequências')
    plt.xticks(ponto_medio)
    plt.grid(True)
    plt.show()

def ordenar_shell_sort(vetor):
    tamanho = len(vetor)
    intervalo = tamanho // 2

    while intervalo > 0:
        for i in range(intervalo, tamanho):
            elemento_atual = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > elemento_atual:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = elemento_atual
        intervalo //= 2

    return vetor

def parse_para_double(valor):
    try:
        return float(valor)
    except ValueError:
        return None

def descobrir_amplitude(vetor):
    resultado = vetor[-1] - vetor[0]
    return resultado

def calcular_quantidade_classes(vetor):
    tamanho = len(vetor)
    resultado = 1 + 3.3 * math.log10(tamanho)
    return math.ceil(resultado)

def calcular_amplitude_classes(amplitude, quantidade):
    resultado = amplitude / quantidade
    return math.ceil(resultado)

def tabela_distribuicao_frequencias(vetor):
    vetor_ordenado = ordenar_shell_sort(vetor)
    amplitude_total = descobrir_amplitude(vetor_ordenado)
    quantidade_classes = calcular_quantidade_classes(vetor_ordenado)
    amplitude_classes = calcular_amplitude_classes(amplitude_total, quantidade_classes)

    # Cria uma lista de intervalos e calcula o ponto médio de cada intervalo
    intervalos = []
    ponto_medio = []
    limite_inferior = min(vetor_ordenado)
    for _ in range(quantidade_classes):
        limite_superior = limite_inferior + amplitude_classes
        intervalos.append((limite_inferior, limite_superior))
        ponto_medio.append((limite_inferior + limite_superior) / 2)  # Calcula o ponto médio
        limite_inferior = limite_superior

    # Calcula a frequência e frequência acumulada
    frequencia = [0] * quantidade_classes
    frequencia_acumulada = [0] * quantidade_classes
    total_observacoes = len(vetor_ordenado)
    acumulador = 0
    for i, valor in enumerate(vetor_ordenado):
        for j, (limite_inferior, limite_superior) in enumerate(intervalos):
            if limite_inferior <= valor < limite_superior:
                frequencia[j] += 1
                acumulador += 1
                frequencia_acumulada[j] = acumulador
                break

    # Imprime a tabela de distribuição de frequências
    print("Intervalo\tPonto Médio\tFrequência\tFrequência Acumulada")
    for (limite_inferior, limite_superior), ponto, freq, freq_acumulada in zip(intervalos, ponto_medio, frequencia, frequencia_acumulada):
        print(f"{limite_inferior:.2f} - {limite_superior:.2f}\t{ponto:.2f}\t\t{freq}\t\t{freq_acumulada}")

    return vetor_ordenado

# Carrega os dados do arquivo CSV
marca, modelo, distancia_entre_eixos, altura, peso_total_padrao, tamanho_motor, potencia_motor, rotacoes_maximas_minuto, eficiencia_combustivel_cidade, eficiencia_combustivel_rodovia, preco = ([] for _ in range(11))

with open('Dados.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    for i, row in enumerate(reader):
        marca.append(row[2])
        modelo.append(row[5])
        distancia_entre_eixos.append(parse_para_double(row[8]))
        altura.append(parse_para_double(row[11]))
        peso_total_padrao.append(parse_para_double(row[12]))
        tamanho_motor.append(parse_para_double(row[15]))
        potencia_motor.append(parse_para_double(row[20]))
        rotacoes_maximas_minuto.append(parse_para_double(row[21]))
        eficiencia_combustivel_cidade.append(parse_para_double(row[22]))
        eficiencia_combustivel_rodovia.append(parse_para_double(row[23]))
        preco.append(parse_para_double(row[24]))

# Calcula a tabela de distribuição de frequências para a altura
tabela_distribuicao_frequencias(altura)
