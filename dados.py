import csv

#lê arquivo csv com os dados de acesso coletados
def carregar_acessos():

    X = []
    Y = []

    arquivo = open("./acesso.csv", 'r')
    leitor = csv.reader(arquivo)

    #joga fora primeira linha descritiva
    next(leitor)

    for home, como_funciona, contato, comprou in leitor:
        dado = [int(home), int(como_funciona), int(contato)]
        X.append(dado)
        Y.append(int(comprou))
    return X, Y
