import csv
import Func

def parse_para_double(valor):
    try:
        return float(valor)
    except ValueError:
        return None

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

Func.tabela_distribuicao_frequencias(distancia_entre_eixos, "Tabela da Distância entre Eixos")
Func.tabela_distribuicao_frequencias(altura, "Tabela da Altura")
Func.tabela_distribuicao_frequencias(peso_total_padrao, "Tabela do Peso Padrão")
Func.tabela_distribuicao_frequencias(tamanho_motor, "Tabela do Tamanho do Motor")
Func.tabela_distribuicao_frequencias(potencia_motor, "Tabela da Potência do Motor")
Func.tabela_distribuicao_frequencias(rotacoes_maximas_minuto, "Tabela de Rotação Máxima por Minuto")
Func.tabela_distribuicao_frequencias(eficiencia_combustivel_cidade, "Tabela de Eficiência na Cidade")
Func.tabela_distribuicao_frequencias(eficiencia_combustivel_rodovia, "Tabela de Eficiência na Rodovia")
Func.tabela_distribuicao_frequencias(preco, "Tabela de Preço")
