import math
import matplotlib.pyplot as plt

# Passo 1: Organizar
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

# Passo 2: Calcular a amplitude
def descobrir_amplitude(vetor):
    resultado = vetor[-1] - vetor[0]
    return resultado

# Passo 3: Calcular a quantidade de classes
def calcular_quantidade_classes(vetor):
    tamanho = len(vetor)
    resultado = 1 + 3.3 * math.log10(tamanho)
    return math.ceil(resultado)

# Passo 4: Calcular a amplitude de cada classe
def calcular_amplitude_classes(amplitude, quantidade):
    resultado = amplitude / quantidade
    return math.ceil(resultado)

# Passo 5: Calcular intervalos
def calcular_intervalos(vetor_ordenado, quantidade_classes, amplitude_classes):
    intervalos = []
    limite_inferior = min(vetor_ordenado)
    for _ in range(quantidade_classes):
        limite_superior = limite_inferior + amplitude_classes
        intervalos.append((limite_inferior, limite_superior))
        limite_inferior = limite_superior
    return intervalos

# Passo 5: Calcular a frequencia
def calcular_frequencia(vetor_ordenado, intervalos):
    frequencia = [0] * len(intervalos)
    acumulador = 0
    for i, valor in enumerate(vetor_ordenado):
        for j, (limite_inferior, limite_superior) in enumerate(intervalos):
            if limite_inferior <= valor < limite_superior:
                frequencia[j] += 1
                acumulador += 1
                break
    return frequencia

# Passo 6: Calcular o ponto_médio
def calcular_ponto_medio(intervalos):
    ponto_medio = []
    for limite_inferior, limite_superior in intervalos:
        ponto_medio.append((limite_inferior + limite_superior) / 2)
    return ponto_medio

# Passo 7: Calcular a frequencia acumulada
def calcular_frequencia_acumulada(frequencia):
    return [sum(frequencia[:i+1]) for i in range(len(frequencia))]

# Passo 8: Plotar a tabela
def plotar_tabela_distribuicao_frequencias(intervalos, ponto_medio, frequencia, frequencia_acumulada, nome):
    plt.figure(figsize=(8, 6))
    plt.axis('off')  # Desabilita os eixos
    colLabels = ['Intervalo', 'Ponto Médio', 'Frequência', 'Frequência Acumulada']
    tabela = plt.table(cellText=list(zip(intervalos, ponto_medio, frequencia, frequencia_acumulada)), colLabels=colLabels, loc='center')
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(10)
    tabela.scale(1.2, 1.2)
    plt.title(nome)
    plt.show()

# Controller de processos
def tabela_distribuicao_frequencias(vetor, nome):
    vetor_ordenado = ordenar_shell_sort(vetor)

    amplitude_total = descobrir_amplitude(vetor_ordenado)
    quantidade_classes = calcular_quantidade_classes(vetor_ordenado)
    amplitude_classes = calcular_amplitude_classes(amplitude_total, quantidade_classes)

    intervalos = calcular_intervalos(vetor_ordenado, quantidade_classes, amplitude_classes)

    ponto_medio = calcular_ponto_medio(intervalos)
    frequencia = calcular_frequencia(vetor_ordenado, intervalos)
    frequencia_acumulada = calcular_frequencia_acumulada(frequencia)

    plotar_tabela_distribuicao_frequencias(intervalos, ponto_medio, frequencia, frequencia_acumulada, nome)

    return
