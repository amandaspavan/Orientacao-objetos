# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self):
        self.cor = "vermelho"
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def acelerar(self):
        self.velocidade = True
    def desacelerar(self):
        self.velocidade = False

# Crie uma instância da classe carro.
meu_carro = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
meu_carro.ligar()
meu_carro.acelerar()

# Faça o carro "parar" utilizando os métodos da sua classe.
meu_carro.desacelerar()
meu_carro.desligar()

print('meu_carro está ligado? {}'.format(meu_carro.ligado))
print('meu_carro está acelerando? {}'.format(meu_carro.velocidade))