# 📦 Sistema de Controle de Estoque

Um sistema prático de gerenciamento de estoque executado diretamente no terminal, desenvolvido em Python. Este projeto foi criado como parte de uma atividade acadêmica do curso de Engenharia de Software.

## 🚀 Funcionalidades

O sistema apresenta um menu interativo de terminal com as seguintes opções:
- **1. Visualizar Estoque:** Lista todos os produtos cadastrados com seus respectivos preços e quantidades.
- **2. Registrar Entrada:** Adiciona unidades a um produto existente no estoque.
- **3. Registrar Saída:** Deduz unidades de um produto, incluindo validação para impedir que o estoque fique com saldo negativo.
- **4. Sair:** Encerra o programa com segurança.
- **Tratamento de Exceções (Fallback):** Validação contra entradas inválidas de menu.

## 💻 Tecnologias e Conceitos Aplicados

Este projeto foi construído utilizando apenas a biblioteca padrão do Python e serviu para consolidar os seguintes conceitos lógicos e estruturais da programação:

* **Estruturas de Dados Flexíveis:** Uso de **Listas de Dicionários** para armazenar múltiplas propriedades de entidades do mundo real.
* **Laços de Repetição Infinitos:** Implementação de menus de console com `while True` e comandos de quebra `break`.
* **Iterações:** Varredura de listas e dicionários com laços `for` para buscar itens específicos.
* **Condicionais Aninhadas:** Uso de `if`/`elif`/`else` combinados para garantir regras de negócio rigorosas (proteção de estoque negativo).
* **Conversão e Formatação:** Uso da função `int()` para tratamento de entradas do usuário via `input()` e *f-strings* para a formatação amigável das informações na tela.

## 🛠️ Como Executar o Projeto

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/Edumopee/Projeto-modelagem-estoque-python.git](https://github.com/Edumopee/Projeto-modelagem-estoque-python.git)
