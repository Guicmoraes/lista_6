#1.Batalha medieval
unidades = []
class UnidadeMedieval:
    def __init__(self,nome):
        self.nome = nome

    def mover(self):
        print('movendo unidade de ',self.nome)
    
    def atacar(self):
        print('unidade de',self.nome,'atacando')
    
class Soldado(UnidadeMedieval):
    def __init__(self,nome):
        super().__init__(nome)

soldado = Soldado('Soldados')
unidades.append(soldado)

class Arqueiros(UnidadeMedieval):
    def __init__(self,nome):
        super().__init__(nome)

arqueiro = Arqueiros('Arqueiros')
unidades.append(arqueiro)

class Cavalheiro(UnidadeMedieval):
    def __init__(self,nome):
        super().__init__(nome)

cavalheiro = Cavalheiro('cavalheiros')
unidades.append(cavalheiro)

for i in range(len(unidades)):
    unidades[i].mover()
    unidades[i].atacar()

#2.Streaming:
assinaturas = []
class Assinatura():
    def __init__(self,tipo,preço,detalhes):
        self.tipo = tipo
        self.preço = preço
        self.detalhes = detalhes
    
    def calcular_preço(self):
        return self.preço
    
    def exibir_detalhes(self):
        return self.detalhes

class AssinaturaSimples(Assinatura):
    def __init__(self,tipo,preço,detalhes):
        super().__init__(tipo,preço,detalhes)

Simples = AssinaturaSimples('Assinatura Simples',29.99,'Essa assinatura fornece acesso a filmes e séries em qualidade padrão')
assinaturas.append(Simples)


class AssinaturaPremium(Assinatura):
    def __init__(self,tipo,preço,detalhes):
        super().__init__(tipo,preço,detalhes)

Premium = AssinaturaPremium('Assinatura Premium',49.99,'Essa assinatura fornece acesso a filmes e séries em qualidade HD e Ultra HD')
assinaturas.append(Premium)


for i in (assinaturas):    
    print(Simples.tipo)
    a_s_preço = Simples.calcular_preço()
    a_s_detalhes = Simples.exibir_detalhes()
    print('preço = {}'.format(a_s_preço),'\ndetalhes = ',a_s_detalhes)
    print('')
    print(Premium.tipo)
    a_p_preço = Premium.calcular_preço()
    a_p_detalhes = Premium.exibir_detalhes()
    print('preço = {}'.format(a_p_preço),'\nDetalhes = ',a_p_detalhes)
    break

