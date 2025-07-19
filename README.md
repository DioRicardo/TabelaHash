# TabelaHash

# Trabalho da Faculdade - Disciplina Estrutura de Dados.

Enunciado:

Com o objetivo de criar um sistema novo de emplacamento de veículos, deputados em do Distrito Federal – DF, decidiram que o último número da placa dos veículos, irá representar o estado de registro dele. Para isso, sua equipe de desenvolvedores foi encarregada de desenvolver uma Tabela Hash com endereçamento em cadeia de 10 posições (cada posição do vetor deve ser uma lista encadeada), representando os números de 0 a 9 que irão representar os 26 estados e o Distrito Federal (total 27).

A função hash deve seguir as seguintes regras:
	A entrada da função hash deve ser uma string com 2 letras, representando a sigla do estado e/ou distrito federal.
	Caso a sigla seja DF (Distrito Federal), por questões de superstição, os deputados solicitaram que o retorno da função seja 7 sempre.
	Caso contrário, a função deve retornar a posição com base no valor ASCII das duas letras e seguindo a seguinte regra:

posição=(〖CHAR1〗_ASCII+ 〖CHAR2〗_ASCII )MOD 10

Onde 〖CHAR1〗_ASCII e 〖CHAR2〗_ASCII são os valores ASCII da primeira e segunda letra, respectivamente (Tabela ASCII no final do documento).