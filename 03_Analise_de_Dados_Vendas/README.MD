# Inteligência Artificial e Previsão de Score de Crédito

Este projeto utiliza Machine Learning para automatizar a análise de crédito de clientes bancários. O objetivo é classificar automaticamente o score de crédito em três categorias: **Ruim**, **Ok** ou **Bom**, baseando-se no histórico financeiro e perfil do cliente.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem base para o desenvolvimento do modelo.
* **Pandas**: Manipulação e tratamento das bases de dados.
* **Scikit-learn (Sklearn)**: Biblioteca principal para criação, treinamento e avaliação dos modelos de IA.
* **LabelEncoder**: Ferramenta de pré-processamento para converter dados textuais em formatos numéricos processáveis pela IA.

---

## ⚙️ Fluxo de Desenvolvimento Técnico

1. **Tratamento de Dados (Preprocessing)**:
   * Conversão de variáveis categóricas (como profissão e mix de crédito) em números utilizando o `LabelEncoder`, visto que modelos de IA operam exclusivamente com dados matemáticos.
2. **Divisão da Base**:
   * Separação dos dados entre **X** (características do cliente) e **y** (o score que desejamos prever).
   * Divisão em bases de **treino e teste** (proporção 70/30) para validar a eficácia do modelo em dados desconhecidos.
3. **Treinamento de Modelos**:
   * Foram testados e comparados dois algoritmos distintos:
     * **Random Forest (Floresta de Decisão)**.
     * **KNN (K-Nearest Neighbors)**.
4. **Avaliação de Performance**:
   * Utilização da métrica `accuracy_score` para identificar qual modelo apresenta maior precisão nas previsões.
5. **Predição em Novos Dados**:
   * Aplicação do melhor modelo (Random Forest) para prever o score de novos clientes importados via `novos_clientes.csv`.

---

## 🚀 Como Executar

1. Certifique-se de que os arquivos `clientes.csv` e `novos_clientes.csv` estejam no diretório.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas scikit-learn