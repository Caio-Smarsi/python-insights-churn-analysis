# Automação de Cadastro de Produtos (RPA)

Este projeto consiste em uma automação robótica de processos (RPA) desenvolvida para realizar o cadastro em massa de produtos em uma plataforma web. O objetivo é substituir a alimentação manual de dados por um fluxo automatizado, mitigando erros de digitação e otimizando o tempo de operação.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal para desenvolvimento da lógica.
* **PyAutoGUI**: Controle automatizado de periféricos (mouse e teclado).
* **Pandas**: Manipulação e leitura da base de dados em formato `.csv`.
* **Time**: Gerenciamento de intervalos e sincronização com o carregamento do sistema.

---

## ⚙️ Fluxo de Execução

O algoritmo foi estruturado nos seguintes passos técnicos:

1. **Inicialização**: Abertura do navegador e acesso ao sistema corporativo.
2. **Autenticação**: Preenchimento automatizado de credenciais de login.
3. **Leitura de Dados**: Importação da base de dados `produtos.csv` via Pandas.
4. **Processamento em Lote**: Iteração sobre as linhas da tabela para preenchimento dos campos:
   * Código, Marca, Tipo, Categoria, Preço Unitário e Custo.
5. **Tratamento de Dados**: Validação de campos opcionais para evitar o preenchimento de valores nulos (`NaN`).

## 🎥 Demonstração da Execução (RPA)

No vídeo abaixo, é possível observar o script em operação real: realizando o login, processando a base de dados `produtos.csv` e automatizando o preenchimento de cada campo no sistema corporativo sem intervenção humana.

https://github.com/user-attachments/assets/fa00a236-3dc0-44eb-ab79-7503d5f40232


