from collections import Counter
import pandas as pd

df = pd.read_csv('busca.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values




# minha abordagem inicial foi separar 90% para treino e 10% para teste
porcentagem_de_treino = 0.9

tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = len(Y) - tamanho_de_treino

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
acertos = resultado == teste_marcacoes

total_acertos = sum(acertos)
total_elementos = len(teste_dados)
taxa_acerto = 100.0 * total_acertos / total_elementos

print("Taxa de acerto do algoritmo: %f" % taxa_acerto)
print("Total de elementos do conjunto de testes: {}".format(total_elementos))

# eficacia do algoritmo que chuta sempre 0 ou chuta sempre 1
acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100 * acerto_base / len(teste_marcacoes)
print("Taxa de acerto base (do algoritmo burro  para comparação): %f" % taxa_de_acerto_base)