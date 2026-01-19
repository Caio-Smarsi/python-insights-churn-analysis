# Análise de Churn e Retenção de Clientes com Python

Este projeto consiste na análise de uma base de dados com aproximadamente 50 mil clientes para identificar os principais motivos de cancelamento (churn). Através do tratamento de dados e visualização estatística, foram propostas ações estratégicas que poderiam reduzir a taxa de cancelamento de **56% para 18%**.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem base para manipulação de dados.
* **Pandas**: Limpeza, tratamento e análise exploratória da base de dados.
* **Plotly**: Criação de gráficos interativos (histogramas) para análise de causa raiz.

---

## ⚙️ Fluxo de Trabalho Técnico

O desenvolvimento seguiu uma metodologia rigorosa de Ciência de Dados:

1. **Importação e Inspeção**: Carga da base `cancelamentos.csv` e análise inicial da estrutura dos dados.
2. **Data Cleaning**: 
   * Exclusão de colunas irrelevantes para a análise (ex: `CustomerID`).
   * Tratamento de valores nulos via `dropna()` para garantir a integridade estatística.
3. **Análise Exploratória**: Identificação de que 56% da base total de clientes havia cancelado o serviço.
4. **Visualização de Dados**: Geração de histogramas cruzando cada variável (idade, contrato, gastos, etc.) com a coluna de cancelamento.

---

## 📊 Insights e Decisões Estratégicas

A análise detalhada revelou três padrões críticos de cancelamento:

* **Tipo de Contrato**: 100% dos clientes com contrato mensal cancelaram o serviço.
  * *Ação*: Oferecer incentivos e descontos para migração aos planos trimestrais e anuais.
* **Atendimento ao Cliente**: Clientes com mais de 4 ligações para o call center apresentam taxa de cancelamento total.
  * *Ação*: Implementar alerta de retenção após a 3ª ligação do cliente.
* **Atraso de Pagamento**: Clientes com mais de 20 dias de atraso cancelam em todos os casos.
  * *Ação*: Criar régua de cobrança e negociação intensiva a partir do 15º dia de atraso.

---

## 🚀 Como Executar

1. Certifique-se de possuir o arquivo `cancelamentos.csv` no diretório.
2. Instale as dependências:
   ```bash
   pip install pandas plotly nbformat ipykernel