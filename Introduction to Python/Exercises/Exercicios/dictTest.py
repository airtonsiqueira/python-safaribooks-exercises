nomes = ['Anna', 'Beatriz', 'Carlos', 'David', 'Emma',
         'Fabiana', 'Gabriela', 'Heitor', 'Icaro', 'Jorge']

idades = [21, 17, 19, 26, 14, 32, 24, 14, 22, 21]

estados = ['SP', 'RJ', 'MG', 'MG', 'SP', 'RJ', 'PR', 'BA', 'BA', 'SP']

data = []
pessoas = []
for i, idade in enumerate(idades):
    dados = {"idade": idade, "estado": estados[i]}
    data.append(dados)

for i, d in enumerate(data):
    pessoa = {nomes[i]: d}
    pessoas.append(pessoa)

print(pessoas)
