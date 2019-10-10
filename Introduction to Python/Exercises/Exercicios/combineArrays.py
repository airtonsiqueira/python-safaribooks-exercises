nomes = ['Anna', 'Beatriz', 'Carlos', 'David', 'Emma',
         'Fabiana', 'Gabriela', 'Heitor', 'Icaro', 'Jorge']
frutas = ['Amora', 'Banana', 'Caqui', 'Damasco',
          'Escropari', 'Figo', 'Goiaba', 'Hawthorn', 'Ingá', 'Jaca']


apelidos = [nome + ' ' + frutas[i] for i, nome in enumerate(nomes)]

# Caso algum dos arrays seja menor, adiciona até o tamanho desse,
# Excluindo os excessos
# tam = len(nomes) if len(nomes) < len(frutas) else len(frutas)
# apelidos = [nomes[i] + ' ' + frutas[i] for i in range(0, tam)]

for a in apelidos:
    print(a)
