# Tech Challenge – Fase 1 | NPS Preditivo

> Quais sinais da operação estão associados à detração do cliente no NPS de um e-commerce, e como a empresa pode agir **antes** da pesquisa?

Projeto do Tech Challenge da Fase 1 da Pós-Tech (AI Scientist). O repositório reúne o entendimento do negócio, o tratamento da base, a análise exploratória (EDA), a apresentação gerencial e o vídeo executivo.

| Acesso rápido | |
|---|---|
| 🎥 Vídeo executivo (4min46s) | [youtube.com/watch?v=VUlYIZ7LXd4](https://www.youtube.com/watch?v=VUlYIZ7LXd4) |
| 📊 Apresentação gerencial | [PDF](reports/apresentacao_gerencial.pdf) · [HTML interativo](reports/apresentacao_gerencial.html) |
| 📝 Partes 1 e 2: negócio e definição da target | [questoes_1_e_2_negocio_e_target.md](reports/questoes_1_e_2_negocio_e_target.md) |
| 🧹 Tratamento da base | [notebooks/01_tratamento_dados.ipynb](notebooks/01_tratamento_dados.ipynb) |
| 🔎 EDA de logística | [notebooks/02_eda_logistica.ipynb](notebooks/02_eda_logistica.ipynb) · [síntese](reports/analise_logistica.md) |
| 🔎 EDA de atendimento e perfil | [notebooks/03_eda_atendimento_perfil.ipynb](notebooks/03_eda_atendimento_perfil.ipynb) |

---

## Sumário

1. [Contexto e problema de negócio](#1-contexto-e-problema-de-negócio)
2. [Objetivo](#2-objetivo)
3. [Entregáveis](#3-entregáveis)
4. [Equipe](#4-equipe)
5. [Estrutura do repositório](#5-estrutura-do-repositório)
6. [Base de dados](#6-base-de-dados)
7. [Premissas e decisões](#7-premissas-e-decisões)
8. [Metodologia](#8-metodologia)
9. [Principais resultados](#9-principais-resultados)
10. [Como reproduzir](#10-como-reproduzir)
11. [Padrões do projeto](#11-padrões-do-projeto)
12. [Checklist da entrega](#12-checklist-da-entrega)

---

## 1. Contexto e problema de negócio

Hoje o NPS é coletado só **depois** que a jornada de compra termina. Quando um cliente responde como detrator, o atraso, a entrega frustrada ou o atendimento ruim já aconteceram e a empresa só consegue remediar. A área de Experiência do Cliente acaba trabalhando de forma reativa.

O projeto responde a duas perguntas:

- **Analítica:** quais fatores operacionais estão mais associados à satisfação do cliente?
- **Estratégica:** como usar esses sinais da operação para agir de forma proativa, antes da pesquisa de NPS?

## 2. Objetivo

1. Responder às perguntas de negócio e definir a variável que representa a satisfação (partes 1 e 2 do desafio).
2. Tratar e documentar a base de pedidos, deixando-a pronta para análise.
3. Identificar, com foco em negócio, os fatores mais críticos para a satisfação: o que está associado aos detratores, se existe um "ponto de ruptura" na experiência e que perfil de cliente tende a ter NPS mais alto ou mais baixo.
4. Comunicar os resultados para um público não técnico, em uma apresentação gerencial e em um vídeo executivo.

> A parte 4 do desafio (modelo preditivo) é **opcional** e não foi realizada pelo grupo.

## 3. Entregáveis

| Entregável | Onde está |
|---|---|
| Partes 1 e 2: entendimento do negócio e definição da target | [reports/questoes_1_e_2_negocio_e_target.md](reports/questoes_1_e_2_negocio_e_target.md) |
| Tratamento e preparação da base | [notebook 01](notebooks/01_tratamento_dados.ipynb) · base tratada em [data/processed/nps_tratado.csv](data/processed/nps_tratado.csv) |
| EDA de logística | [notebook 02](notebooks/02_eda_logistica.ipynb) · [síntese](reports/analise_logistica.md) |
| EDA de atendimento e perfil | [notebook 03](notebooks/03_eda_atendimento_perfil.ipynb) |
| Apresentação gerencial (storytelling para público não técnico) | [PDF](reports/apresentacao_gerencial.pdf) · [HTML interativo](reports/apresentacao_gerencial.html) |
| Vídeo executivo (até 5 minutos) | [YouTube](https://www.youtube.com/watch?v=VUlYIZ7LXd4) |
| Parte 4: modelo preditivo (opcional) | Não realizada, por decisão do grupo |

## 4. Equipe

Gabriel Balbine de Andrades, Gerferson André Silva Costa, Giulliano Alves Souza Machado, Matheus da Silva Lima e Yan Marcel Ramos. As frentes do projeto abrangem negócio e variável-alvo, preparação dos dados, EDA de logística, EDA de atendimento e perfil, e apresentação dos resultados.

## 5. Estrutura do repositório

```
tech-challenge-fase1-nps/
├── data/
│   ├── raw/                                   # base original (nunca editar)
│   │   └── desafio_nps_fase_1.csv
│   └── processed/                             # base tratada, gerada pelo notebook 01
│       └── nps_tratado.csv
├── notebooks/
│   ├── 01_tratamento_dados.ipynb              # limpeza, validações e categoria NPS
│   ├── 02_eda_logistica.ipynb                 # entrega, atraso, tentativas, frete
│   └── 03_eda_atendimento_perfil.ipynb        # atendimento, reclamações, perfil
├── reports/
│   ├── questoes_1_e_2_negocio_e_target.md     # partes 1 e 2 do desafio
│   ├── analise_logistica.md                   # síntese e limitações da EDA de logística
│   ├── apresentacao_gerencial.pdf             # slides para público não técnico
│   ├── apresentacao_gerencial.html            # mesma apresentação, navegável no navegador
│   └── figures/                               # gráficos gerados pelos notebooks
├── scripts/
│   └── verificar_eda_logistica.py             # reproduz a base e o notebook 02
├── .github/workflows/ci.yml                   # verificação em push e pull request
├── requirements.txt
├── requirements-dev.txt
├── .pre-commit-config.yaml                    # verificações antes de cada commit
├── .gitignore
└── README.md
```

> Os notebooks de EDA partem sempre de `data/processed/nps_tratado.csv`, nunca da base bruta, para que todas as análises usem os mesmos tratamentos e a mesma categoria de NPS. O CSV não guarda a ordem das categorias, então ela é reaplicada ao carregar:
>
> ```python
> df = pd.read_csv(ROOT / "data" / "processed" / "nps_tratado.csv")
> df["nps_category"] = pd.Categorical(
>     df["nps_category"], categories=["Detrator", "Neutro", "Promotor"], ordered=True
> )
> ```

## 6. Base de dados

**Arquivo:** `data/raw/desafio_nps_fase_1.csv`. São **2.500 pedidos** (uma linha por pedido/cliente) e **19 variáveis**.

Diagnóstico inicial da base bruta:

- Sem valores nulos.
- Sem linhas duplicadas e sem `customer_id` ou `order_id` repetidos.
- Todas as colunas são numéricas, exceto `customer_region` (5 regiões, distribuídas de forma equilibrada).
- **NPS geral da base: −79,96** (84,36% detratores, 11,24% neutros e 4,40% promotores). A regra de categorização usada está na [seção 7](#7-premissas-e-decisões).

### Dicionário de dados

Legenda da coluna **Papel na análise**: **Fator** = variável operacional ou de perfil analisada na EDA · **ID** = identificador, não analisado · **Alvo** = variável que representa a satisfação · **Pós-pesquisa** = medida junto ou depois do NPS, não serve como sinal antecipado (ver 7.3) · **A confirmar** = depende de quando o dado é registrado.

| Grupo | Variável | Descrição | Faixa observada | Papel na análise |
|---|---|---|---|---|
| Identificação | `customer_id` | Identificador do cliente | 1 – 2.500 | ID |
| Identificação | `order_id` | Identificador do pedido | 50.001 – 52.500 | ID |
| Cliente | `customer_age` | Idade do cliente (anos) | 18 – 69 | Fator |
| Cliente | `customer_region` | Região do Brasil | 5 categorias | Fator |
| Cliente | `customer_tenure_months` | Tempo de relacionamento com a empresa (meses) | 1 – 119 | Fator |
| Pedido | `order_value` | Valor do pedido (R$) | 7,76 – 1.983,81 | Fator |
| Pedido | `items_quantity` | Quantidade de itens no pedido | 1 – 6 | Fator |
| Pedido | `discount_value` | Valor do desconto concedido (R$) | 0,02 – 230,33 | Fator |
| Pedido | `payment_installments` | Número de parcelas | 1 – 11 | Fator |
| Logística | `delivery_time_days` | **Prazo de entrega previsto** (dias), ver premissa 7.1 | 2 – 14 | Fator |
| Logística | `delivery_delay_days` | Dias de atraso em relação ao prazo previsto | 0 – 8 | Fator |
| Logística | `freight_value` | Valor do frete (R$) | 2,62 – 76,13 | Fator |
| Logística | `delivery_attempts` | Tentativas de entrega | 1 – 3 | Fator |
| Atendimento | `customer_service_contacts` | Contatos com o atendimento | 0 – 7 | Fator |
| Atendimento | `resolution_time_days` | Tempo de resolução (dias) | 0 – 11 | Fator |
| Atendimento | `complaints_count` | Quantidade de reclamações | 0 – 11 | A confirmar |
| Resultado | `nps_score` | Nota NPS (0 a 10, contínua, com decimais) | 0 – 10 | **Alvo** |
| Resultado | `repeat_purchase_30d` | Recompra em até 30 dias (1 = sim) | 0 / 1 | Pós-pesquisa |
| Resultado | `csat_internal_score` | Nota de satisfação interna (CSAT) | 0 – 10 | Pós-pesquisa |

### Variáveis criadas no tratamento

A base tratada (`data/processed/nps_tratado.csv`) mantém as 19 colunas originais e acrescenta 6:

| Variável | Regra | Para que serve |
|---|---|---|
| `nps_category` | Detrator / Neutro / Promotor (ver premissa 7.2) | Segmentação da EDA |
| `is_detractor` | 1 se `nps_category` = Detrator | Proporção de detratores por grupo (basta tirar a média) |
| `total_delivery_days` | `delivery_time_days + delivery_delay_days` | Tempo real de entrega percebido pelo cliente |
| `is_late` | 1 se `delivery_delay_days > 0` | Indicador simples de atraso para a EDA e os slides |
| `flag_discount_over_order_value` | 1 se `discount_value > order_value` | Marca os pedidos da premissa 7.4 |
| `flag_resolution_without_contact` | 1 se `resolution_time_days > 0` e `customer_service_contacts = 0` | Marca os pedidos da premissa 7.4 |

## 7. Premissas e decisões

### 7.1 Prazo x atraso de entrega

O dicionário original descreve `delivery_time_days` como "tempo total de entrega", mas em **121 pedidos** o atraso é maior que esse tempo, o que seria impossível se o atraso estivesse incluído nele. O grupo levou a dúvida ao canal de dúvidas do desafio. A orientação do professor (05/10/2026) foi:

- `delivery_time_days` = **prazo previsto** de entrega;
- `delivery_delay_days` = **dias de atraso** em relação a esse prazo;
- tempo real de entrega = prazo previsto + atraso.

Essa é a interpretação adotada em todo o projeto.

### 7.2 Categorias de NPS com notas decimais

Em 2.075 dos 2.500 pedidos a nota tem casas decimais (ex.: 6,9 e 8,4), então a regra clássica com notas inteiras não basta. A regra adotada usa **intervalos**, sem arredondar a nota:

| Categoria | Regra | Equivalência na escala inteira |
|---|---|---|
| Detrator | `nps_score < 7` | 0 a 6 |
| Neutro | `7 <= nps_score < 9` | 7 e 8 |
| Promotor | `nps_score >= 9` | 9 e 10 |

> Arredondar a nota antes de categorizar (ex.: 6,5 → 7) mudaria a categoria de **180 clientes (7,20%)**: 134 detratores passariam a neutros e 46 neutros passariam a promotores. Por isso a regra por intervalos foi mantida em todas as análises.

### 7.3 Informações registradas depois da pesquisa (*data leakage*)

Como o objetivo é agir **antes** da pesquisa de NPS, só fazem sentido como sinais antecipados as informações disponíveis durante a jornada:

- `csat_internal_score` e `repeat_purchase_30d` são medidos junto ou depois do NPS. Usá-los para antecipar a nota seria "colar a resposta" (vazamento de informação).
- `complaints_count` fica em aberto até se confirmar em que momento a reclamação é registrada na jornada.
- `customer_id` e `order_id` são apenas identificadores.

### 7.4 Tratamento da base

Detalhes e código no notebook `01_tratamento_dados.ipynb`. **Nenhuma linha foi removida.**

| Verificação | Resultado | Decisão |
|---|---|---|
| Tipos, nulos, duplicados e faixas válidas | Nenhum problema | Nenhuma correção necessária |
| Atraso maior que o prazo | 121 pedidos | Mantidos: coerente com a premissa 7.1 |
| Desconto maior que o valor do pedido | 35 pedidos | Mantidos e marcados em `flag_discount_over_order_value`. Hipótese: `order_value` já é o valor com desconto |
| Tempo de resolução sem contato com o atendimento | 511 pedidos | Mantidos e marcados em `flag_resolution_without_contact`. 95,69% deles têm reclamação, então o tempo de resolução pode se referir a reclamações abertas por outro canal |
| Outliers (critério IQR) | 6 colunas, de 0,48% a 7,04% da base (maior: `customer_service_contacts`) | Mantidos: são valores possíveis e mostram justamente os casos extremos da experiência |

## 8. Metodologia

O projeto segue as etapas do **CRISP-DM** aplicáveis a um estudo exploratório:

| Etapa | O que é feito | Onde está |
|---|---|---|
| 1. Entendimento do negócio | Problema, importância do NPS, áreas beneficiadas, reflexão sobre recompra, boca a boca e market share, e definição da target | [reports/questoes_1_e_2_negocio_e_target.md](reports/questoes_1_e_2_negocio_e_target.md) |
| 2. Entendimento dos dados | Perfil da base, dicionário e premissas | Este README + notebook 01 |
| 3. Preparação dos dados | Tipos, nulos, duplicados, outliers, consistência e criação de variáveis | `01_tratamento_dados.ipynb` |
| 4. Análise exploratória | Fatores críticos, o que está associado aos detratores, ponto de ruptura e perfil de cliente, comparando a proporção de detratores e a nota média entre grupos | `02_eda_logistica.ipynb` e `03_eda_atendimento_perfil.ipynb` |
| 5. Comunicação | Storytelling para público não técnico: insights, fatores mais associados à satisfação, recomendações e limitações | Apresentação gerencial e vídeo executivo |

## 9. Principais resultados

Os números descrevem **associações** observadas nos 2.500 pedidos; não medem causa e efeito.

- **Ponto de partida:** NPS de **−79,96**. 84,36% dos clientes são detratores e 4,40% são promotores.
- **Atraso na entrega** é o fator com a associação mais forte com a nota. A proporção de detratores vai de **51,62%** nos pedidos entregues no prazo para **73,98%** com 1 dia de atraso e chega a **97,61% a 100,00%** com 3 dias ou mais. Só 11,08% dos pedidos chegaram no prazo.
- **Ponto de ruptura:** não há um único dia de virada. A proporção de detratores já é maior a partir do primeiro dia de atraso e continua subindo nas faixas seguintes.
- **Reclamações e atendimento:** com até 1 reclamação, 28,28% são detratores; com 2, 65,34%. Entre os pedidos sem contato com o suporte, 70,76% são detratores; com 4 contatos ou mais, 97,73%.
- **Perfil do cliente e condições do pedido** (idade, região, tempo de casa, valor, desconto, parcelas) mostram proporções de detratores parecidas, entre 81,38% e 87,25% em todos os grupos.

Recomendações, limitações e o detalhamento estão na [apresentação gerencial](reports/apresentacao_gerencial.pdf) e nos notebooks 02 e 03.

## 10. Como reproduzir

**Pré-requisitos:** Python 3.11 ou superior e Git.

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/GiullianoAlvs/tech-challenge-fase1-nps.git
   cd tech-challenge-fase1-nps
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Linux/macOS: `source .venv/bin/activate`

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Abra o Jupyter e execute os notebooks **na ordem numérica** (01, 02 e 03):

   ```bash
   jupyter lab
   ```

   O notebook `01` gera `data/processed/nps_tratado.csv`, que é usado pelos notebooks seguintes.

   Para reproduzir a base e verificar a execução do notebook de logística e suas figuras:

   ```bash
   python scripts/verificar_eda_logistica.py
   ```

   Para instalar as verificações locais de formatação e integridade dos arquivos:

   ```bash
   python -m pip install -r requirements-dev.txt
   pre-commit install
   pre-commit run --all-files
   ```

5. Para ver a apresentação, abra o [PDF](reports/apresentacao_gerencial.pdf) ou baixe o [HTML](reports/apresentacao_gerencial.html) e abra no navegador (setas para navegar, F para tela cheia).

## 11. Padrões do projeto

- **Notebooks** numerados na ordem de execução: `NN_descricao.ipynb`.
- **Nomes** de arquivos, variáveis e funções em `snake_case`. As colunas originais ficam em inglês, como na base, e as colunas novas seguem o mesmo padrão (ex.: `nps_category`).
- **Comentários e textos** em português, com uma célula de markdown explicando o objetivo de cada seção.
- **Caminhos relativos** com `pathlib`, sem caminhos absolutos do computador de cada um.
- **`data/raw/` é somente leitura.** Toda alteração gera um arquivo novo em `data/processed/`.
- **Antes de cada commit**, rode *Restart Kernel and Run All* para garantir que o notebook executa do zero.
- **Gráficos** gerados pelos notebooks vão para `reports/figures/` com nome descritivo (ex.: `logistica_detratores_por_atraso.png`).

## 12. Checklist da entrega

- [x] Repositório público no GitHub
- [x] Partes 1 e 2: entendimento do negócio e definição da target
- [x] Tratamento e preparação da base
- [x] Análise exploratória (EDA) de logística, atendimento e perfil
- [x] Código organizado em notebooks e scripts, com nomes padronizados e comentários
- [x] Estrutura de pastas clara (`data/`, `notebooks/`, `reports/`, `scripts/`)
- [x] README com objetivo, descrição da base, metodologia e como reproduzir
- [x] Apresentação de storytelling para público não técnico
- [x] Vídeo executivo de até 5 minutos
- [ ] Parte 4: modelo preditivo (opcional, não realizada)
