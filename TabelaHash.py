#RU: 4751823 - Dio Ricardo

class ElementoDaLista:
    def __init__(self, sigla = None, nome = None):
        self.sigla = sigla
        self.nomeEstado = nome
        self.proximo = None

    def __str__(self):
        if self is None:
            return "None"
        return f"{self.sigla} -> "


#Exigência de código 2 de 7
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    # Exigência de código 3 de 7
    def inserir(self, estado):
        if self.head is None:
            self.head = estado
            return

        estado.proximo = self.head
        self.head = estado
        return

    def __str__(self):
        if self.head is None:
            return "None"

    def imprimirListaEncadeada(self):
        if self.head is None:
            print(self)
            return
        aux = self.head
        while aux:
            print(aux, end="")
            aux = aux.proximo
        print(aux)


#Exigência de código 1 de 7
class TabelaHash:
    def __init__(self):
        self.tam = 10
        self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]


    #Exigência de código 5 de 7
    def funcaoHash(self, k):
        k = list(k)
        return (ord(k[0]) + ord(k[1])) % self.tam

    def inserir(self, sigla, nomeEstado):
        if sigla == "DF":
            pos = 7
        else:
            pos = self.funcaoHash(sigla)
        add = self.h[pos].inserir(ElementoDaLista(sigla, nomeEstado))


    # Exigência de código 4 de 7
    def imprimeTabela(self):
        for i in range(0, self.tam):
            print(f"{i}: ", end="")
            self.h[i].imprimirListaEncadeada()



#Programa principal

# Array com os estados para facilitar a inserção
estados = [["DF", "Distrito Federal"], ["RJ", "Rio de Janeiro"], ["PR", "Paraná"], ["AC", "Acre"], ["AL", "Alagoas"], ["AM", "Amazonas"], ["AP", "Amapá"], ["BA", "Bahia"], ["CE", "Ceará"], ["ES", "Espírito Santo"], ["GO", "Goiás"], ["MA", "Maranhão"],
    ["MG", "Minas Gerais"], ["MS", "Mato Grosso do Sul"], ["MT", "Mato Grosso"], ["PA", "Pará"], ["PB", "Paraíba"], ["PE", "Pernambuco"], ["PI", "Piauí"], ["RN", "Rio Grande do Norte"], ["RO", "Rondônia"], ["RR", "Roraima"], ["RS", "Rio Grande do Sul"],
    ["SC", "Santa Catarina"], ["SE", "Sergipe"], ["SP", "São Paulo"], ["TO", "Tocantins"]]

#Inicialização da Tabela Hash
tabela = TabelaHash()

#Imprime a tabela vazia, conforme exigência de saída de console 1 de 3.
tabela.imprimeTabela()

print("\n\n") #Apenas para organizar a console.

#Inserindo todos os estados via loop para evitar repetição de código.
for i in range(0, len(estados)):
    #Exigência de código 6 de 7
    tabela.inserir(estados[i][0], estados[i][1])

#Imprime a tabela com os estados cadastrados, conforme exigência de saída de Console 2 de 3.
tabela.imprimeTabela()

print("\n\n") #Apenas para organizar a console.

#Exigência de código 7 de 7
tabela.inserir("DV", "Dio Ricardo Ferreira Vieira")

#Exigência de saída de console 3 de 3.
tabela.imprimeTabela()