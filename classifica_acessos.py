from dados import carregar_acessos

X, Y = carregar_acessos()

#minha abordagem inicial foi separar 90% para treino e 10% para teste
treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferenca = resultado - teste_marcacoes

acertos = [d for d in diferenca if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_dados)
taxa_acerto = 100.0 * total_acertos/total_elementos

print("Taxa de acerto: {}".format(taxa_acerto))
print("Total de elementos: {}".format(total_elementos))
