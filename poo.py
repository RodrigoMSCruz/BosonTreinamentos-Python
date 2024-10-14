# Orientação a objetos: Paradigma de programação

class veiculo:
    
    def movimentar(self):
        print('Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.num_registro = None

    #Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')

    #Setter
    def set_num_registro(self, registro):
        self._registro = registro
    
    def get_num_registro(self):
        return self._registro

if __name__ == '__main__':
    meu_veiculo = veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro(490321)
    print(f'Registro: {meu_veiculo.get_num_registro()}')

class Carro(veiculo):
    
    # Método __init__ será herdado.
    
    def movimentar(self):
        print('Sou um carro e ando pelas ruas!')

class Motocicleta(veiculo):
    
    def movimentar(self):
        print('Corro muito!')

class Aviao(veiculo):
    
    def __init__(self, name, model, categoria):
        super().__init__(name, model)
        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria



meu_carro = Carro('Volkswagen', 'Polo')
meu_carro.movimentar()
meu_carro.get_fabr_modelo()

seu_carro = Carro('Audi', 'A5 Sportback')
seu_carro.movimentar()
seu_carro.get_fabr_modelo()

meu_aviao = Aviao('Boeing', '747', 'Comercial')
meu_aviao.movimentar()
meu_aviao.get_fabr_modelo()
print(f'')