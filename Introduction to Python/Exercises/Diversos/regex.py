
import re

exemplo0 = "Jessica tem 15 anos de idade, Daniel tem 27 anos de idade. Eduardo tem 39 e seu avô, Oscar, tem 97"
exemplo1 = "Jessica tem 15 anos de idade, mora na rua das orquideas 900 e gosta de pão de batata"
exemplo2 = "Daniel tem 27 anos de idade, é ex jogador de futebol que reside na avenida da liberdade 370"
exemplo3 = "Eduardo tem 39 e aprendeu a jogar xadrez na época que estudava no colégio da rua jiparaná 12"
exemplo4 = "Oscar tem 97 anos e mora num belo sobradinho na travessa imigrantes s/n"
exemplo5 = exemplo1 + " " + exemplo2 + " " + exemplo3 + " " + exemplo4

idades = re.search(r'(tem|Tem)\s(\d{1,3})((anos|ANOS|Anos)|)', exemplo0)
nomes = re.findall(r'[A-Z][a-z]*', exemplo0)
enderecos = re.search(
    r'(Rua|rua|R.|avenida|Avenida|AV.|travessa|Travessa|TRAV.|Trav.)([a-zA-Z_\s]+)+(\d+)', exemplo5)

idadesFiltro = []
print(idades)
# print(nomes)
# print(enderecos)
