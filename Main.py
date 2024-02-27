import csv
import Func

def parse_para_double(valor):
    try:
        return float(valor)
    except ValueError:
        return None

def exibir_tabela_distribuicao_frequencia(opcao, dados):
    opcoes = {
        1: "Tabela da Distância entre Eixos",
        2: "Tabela da Altura",
        3: "Tabela do Peso Padrão",
        4: "Tabela do Tamanho do Motor",
        5: "Tabela da Potência do Motor",
        6: "Tabela de Rotação Máxima por Minuto",
        7: "Tabela de Eficiência na Cidade",
        8: "Tabela de Eficiência na Rodovia",
        9: "Tabela de Preço"
    }
    if opcao in opcoes:
        Func.tabela_distribuicao_frequencias(dados[opcao - 1], opcoes[opcao])
    elif opcao == 10:
        print("Saindo do programa...")
        exit()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

dados = [[] for _ in range(9)]

with open('Dados.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        dados[0].append(parse_para_double(row[8]))
        dados[1].append(parse_para_double(row[11]))
        dados[2].append(parse_para_double(row[12]))
        dados[3].append(parse_para_double(row[15]))
        dados[4].append(parse_para_double(row[20]))
        dados[5].append(parse_para_double(row[21]))
        dados[6].append(parse_para_double(row[22]))
        dados[7].append(parse_para_double(row[23]))
        dados[8].append(parse_para_double(row[24]))

while True:
    print("\nEscolha a tabela de distribuição de frequência que deseja visualizar:")
    print("1. Tabela da Distância entre Eixos")
    print("2. Tabela da Altura")
    print("3. Tabela do Peso Padrão")
    print("4. Tabela do Tamanho do Motor")
    print("5. Tabela da Potência do Motor")
    print("6. Tabela de Rotação Máxima por Minuto")
    print("7. Tabela de Eficiência na Cidade")
    print("8. Tabela de Eficiência na Rodovia")
    print("9. Tabela de Preço")
    print("10. Sair")

    opcao = int(input("Digite o número correspondente à opção desejada: "))

    exibir_tabela_distribuicao_frequencia(opcao, dados)
