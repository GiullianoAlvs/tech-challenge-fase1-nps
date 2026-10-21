# Tech Challenge – Fase 1 | NPS Preditivo

> Como antecipar a insatisfação do cliente de um e-commerce **antes** da pesquisa de NPS, usando dados operacionais de pedido, logística e atendimento.

Projeto desenvolvido para o Tech Challenge da Fase 1 da Pós-Tech. O repositório reúne a base preparada, as análises exploratórias de logística, atendimento e perfil, além da estrutura para o modelo preditivo opcional.

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
9. [Como reproduzir](#9-como-reproduzir)
10. [Padrões do projeto](#10-padrões-do-projeto)
11. [Cronograma](#11-cronograma)
12. [Checklist da entrega](#12-checklist-da-entrega)

---

## 1. Contexto e problema de negócio

Hoje o NPS é coletado só **depois** que a jornada de compra termina. Quando um cliente responde como detrator, o atraso, a entrega frustrada ou o atendimento ruim já aconteceram e a empresa só consegue remediar. A área de Experiência do Cliente acaba trabalhando de forma reativa.

O projeto responde a duas perguntas:

- **Analítica:** quais fatores operacionais realmente influenciam a satisfação do cliente?
- **Estratégica:** como sair de uma gestão reativa para um modelo **preditivo e proativo**, que sinalize o risco de insatisfação antes da pesquisa?

## 2. Objetivo

1. Tratar e documentar a base de pedidos, deixando-a pronta para análise.
2. Identificar, com foco em negócio, os fatores mais críticos para a satisfação: o que gera detratores, se existe um "ponto de ruptura" na experiência e que perfil de cliente tende a ter NPS mais alto ou mais baixo.
3. *(Opcional)* Construir um modelo que estime o NPS (ou o risco de detração) a partir de variáveis disponíveis **durante** a jornada, e explicar como a empresa usaria o modelo na prática.

## 3. Entregáveis

| Entregável | Status | Link |
|---|---|---|
| Repositório público (tratamento e análises) | Em andamento | este repositório |
| EDA de logística | Concluída | [notebook 02](notebooks/02_eda_logistica.ipynb) · [síntese](reports/analise_logistica.md) |
| EDA de atendimento e perfil | Concluída e integrada | [notebook 03](notebooks/03_eda_atendimento_perfil.ipynb) |
| Modelo preditivo (opcional) | Ainda não integrado à branch principal | [notebook 04](notebooks/04_modelo_preditivo.ipynb) |
| Apresentação (storytelling para público não técnico) | A fazer | — |
| Vídeo executivo (até 5 minutos) | A fazer | — |

## 4. Equipe

Gabriel Balbine de Andrades, Gerferson André Silva Costa, Giulliano Alves Souza Machado, Matheus da Silva Lima e Yan Marcel Ramos. As frentes do projeto abrangem negócio e variável-alvo, preparação dos dados, EDA de logística, EDA de atendimento e perfil, e apresentação dos resultados.

O modelo preditivo é construído pelo grupo inteiro em sessões conjuntas.

## 5. Estrutura do repositório

```
tech-challenge-fase1-nps/
├── data/
│   ├── raw/                              # base original (nunca editar)
│   │   └── desafio_nps_fase_1.csv
│   └── processed/                        # base tratada, gerada pelo notebook 01
│       └── nps_tratado.csv
├── notebooks/
│   ├── 01_tratamento_dados.ipynb         # P2 – limpeza, validações e categoria NPS
│   ├── 02_eda_logistica.ipynb            # P3 – entrega, atraso, tentativas, frete
│   ├── 03_eda_atendimento_perfil.ipynb   # P4 – atendimento, reclamações, perfil
│   └── 04_modelo_preditivo.ipynb         # todos – modelo e avaliação (opcional)
├── models/                               # modelos treinados (.joblib)
├── reports/
│   ├── analise_logistica.md              # resultados e limitações da EDA de logística
│   └── figures/                          # gráficos exportados para os slides
├── scripts/
│   └── verificar_eda_logistica.py        # reproduz a base e o notebook 02
├── .github/workflows/ci.yml             # verificação em push e pull request
├── requirements.txt
├── requirements-dev.txt
├── .pre-commit-config.yaml              # verificações antes de cada commit
├── .gitignore
└── README.md
```

> **Para P3 e P4:** a EDA deve partir sempre de `data/processed/nps_tratado.csv`, nunca da base bruta. Assim todos trabalham com os mesmos tratamentos e a mesma categoria de NPS. O CSV não guarda a ordem das categorias, então reaplique-a ao carregar:
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
- **NPS geral da base: −80** (84% detratores, 11% neutros, 4% promotores). A regra de categorização usada está na [seção 7](#7-premissas-e-decisões).

### Dicionário de dados

Legenda da coluna **Uso no modelo**: **Feature** = pode entrar no modelo · **ID** = identificador, não usar · **Target** = variável alvo · **Vazamento** = medida depois ou junto do NPS, não usar como entrada · **A confirmar** = depende de quando o dado é registrado.

| Grupo | Variável | Descrição | Faixa observada | Uso no modelo |
|---|---|---|---|---|
| Identificação | `customer_id` | Identificador do cliente | 1 – 2.500 | ID |
| Identificação | `order_id` | Identificador do pedido | 50.001 – 52.500 | ID |
| Cliente | `customer_age` | Idade do cliente (anos) | 18 – 69 | Feature |
| Cliente | `customer_region` | Região do Brasil | 5 categorias | Feature |
| Cliente | `customer_tenure_months` | Tempo de relacionamento com a empresa (meses) | 1 – 119 | Feature |
| Pedido | `order_value` | Valor do pedido (R$) | 7,76 – 1.983,81 | Feature |
| Pedido | `items_quantity` | Quantidade de itens no pedido | 1 – 6 | Feature |
| Pedido | `discount_value` | Valor do desconto concedido (R$) | 0,02 – 230,33 | Feature |
| Pedido | `payment_installments` | Número de parcelas | 1 – 11 | Feature |
| Logística | `delivery_time_days` | **Prazo de entrega previsto** (dias), ver premissa 7.1 | 2 – 14 | Feature |
| Logística | `delivery_delay_days` | Dias de atraso em relação ao prazo previsto | 0 – 8 | Feature |
| Logística | `freight_value` | Valor do frete (R$) | 2,62 – 76,13 | Feature |
| Logística | `delivery_attempts` | Tentativas de entrega | 1 – 3 | Feature |
| Atendimento | `customer_service_contacts` | Contatos com o atendimento | 0 – 7 | Feature |
| Atendimento | `resolution_time_days` | Tempo de resolução (dias) | 0 – 11 | Feature |
| Atendimento | `complaints_count` | Quantidade de reclamações | 0 – 11 | A confirmar |
| Resultado | `nps_score` | Nota NPS (0 a 10, contínua, com decimais) | 0 – 10 | **Target** |
| Resultado | `repeat_purchase_30d` | Recompra em até 30 dias (1 = sim) | 0 / 1 | Vazamento |
| Resultado | `csat_internal_score` | Nota de satisfação interna (CSAT) | 0 – 10 | Vazamento |

### Variáveis criadas no tratamento

A base tratada (`data/processed/nps_tratado.csv`) mantém as 19 colunas originais e acrescenta 6:

| Variável | Regra | Para que serve |
|---|---|---|
| `nps_category` | Detrator / Neutro / Promotor (ver premissa 7.2) | Segmentação da EDA e target de classificação |
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

Em 2.075 dos 2.500 pedidos a nota tem casas decimais (ex.: 6,9 e 8,4), então a regra clássica com notas inteiras não basta. A regra adotada usa **intervalos**:

| Categoria | Regra | Equivalência na escala inteira |
|---|---|---|
| Detrator | `nps_score < 7` | 0 a 6 |
| Neutro | `7 <= nps_score < 9` | 7 e 8 |
| Promotor | `nps_score >= 9` | 9 e 10 |

> **Atenção:** arredondar a nota antes de categorizar (ex.: 6,5 → 7) mudaria a categoria de **180 clientes (7,2%)**: 134 detratores passariam a neutros e 46 neutros passariam a promotores. Qualquer mudança nessa regra precisa ser alinhada entre P1 e P2 e atualizada aqui e no notebook 01.

### 7.3 Vazamento de informação (*data leakage*)

O modelo deve funcionar **antes** da pesquisa de NPS, então não pode usar informação gerada depois dela ou junto com ela:

- `csat_internal_score` e `repeat_purchase_30d` **ficam fora** das variáveis de entrada.
- `complaints_count` fica em avaliação até o grupo confirmar quando a reclamação é registrada na jornada.
- `customer_id` e `order_id` são identificadores e não entram no modelo.

### 7.4 Tratamento da base

Detalhes e código no notebook `01_tratamento_dados.ipynb`. **Nenhuma linha foi removida.**

| Verificação | Resultado | Decisão |
|---|---|---|
| Tipos, nulos, duplicados e faixas válidas | Nenhum problema | Nenhuma correção necessária |
| Atraso maior que o prazo | 121 pedidos | Mantidos: coerente com a premissa 7.1 |
| Desconto maior que o valor do pedido | 35 pedidos | Mantidos e marcados em `flag_discount_over_order_value`. Hipótese: `order_value` já é o valor com desconto |
| Tempo de resolução sem contato com o atendimento | 511 pedidos | Mantidos e marcados em `flag_resolution_without_contact`. 96% deles têm reclamação, então o tempo de resolução pode se referir a reclamações abertas por outro canal |
| Outliers (critério IQR) | 6 colunas, de 0,5% a 7% da base (maior: `customer_service_contacts`) | Mantidos: são valores possíveis e mostram justamente os casos extremos da experiência |

## 8. Metodologia

O projeto segue o **CRISP-DM**:

| Etapa | O que é feito | Onde está | Responsável |
|---|---|---|---|
| 1. Entendimento do negócio | Problema, importância do NPS, áreas beneficiadas e definição da target | `reports/` + slides | P1 |
| 2. Entendimento dos dados | Perfil da base, dicionário e premissas | Este README + notebook 01 | P2 |
| 3. Preparação dos dados | Tipos, nulos, duplicados, outliers, consistência e criação de variáveis | `01_tratamento_dados.ipynb` | P2 |
| 4. Análise exploratória | Fatores críticos, o que gera detratores, ponto de ruptura e perfil de cliente | `02_eda_logistica.ipynb` e `03_eda_atendimento_perfil.ipynb` | P3 e P4 |
| 5. Modelagem *(opcional)* | Escolha da target (regressão ou classificação), seleção de variáveis, divisão treino/teste e treino | `04_modelo_preditivo.ipynb` | Todos |
| 6. Avaliação e uso | Métricas, escolha final e como a empresa usaria o modelo no dia a dia | `04_modelo_preditivo.ipynb` + slides e vídeo | Todos e P5 |

## 9. Como reproduzir

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

4. Abra o Jupyter e execute os notebooks **na ordem numérica**:

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

## 10. Padrões do projeto

- **Notebooks** numerados na ordem de execução: `NN_descricao.ipynb`.
- **Nomes** de arquivos, variáveis e funções em `snake_case`. As colunas originais ficam em inglês, como na base, e as colunas novas seguem o mesmo padrão (ex.: `nps_category`).
- **Comentários e textos** em português, com uma célula de markdown explicando o objetivo de cada seção.
- **Caminhos relativos** com `pathlib`, sem caminhos absolutos do computador de cada um.
- **`data/raw/` é somente leitura.** Toda alteração gera um arquivo novo em `data/processed/`.
- **Antes de cada commit**, rode *Restart Kernel and Run All* para garantir que o notebook executa do zero.
- **Gráficos** usados nos slides vão para `reports/figures/` com nome descritivo (ex.: `nps_por_faixa_atraso.png`).

## 11. Cronograma

Entrega final: **terça, 03/11/2026**.

| Etapa | Período | Marcos principais |
|---|---|---|
| 1. Fundamentos | 03/10 – 11/10 | Repositório criado e base tratada (P2) · Partes 1 e 2 (P1) · Esqueleto dos slides (P5) |
| 2. EDA | 08/10 – 18/10 | Check-in do grupo em 14/10 · EDA logística (P3) e EDA atendimento/perfil (P4) até 18/10 |
| 3. Modelo preditivo | 19/10 – 25/10 | Sessão 1 em 20/10 · Sessão 2 em 24/10 · Notebook do modelo limpo até 25/10 (P2) |
| 4. Finalização | 26/10 – 31/10 | Slides e roteiro até 28/10 · README final até 30/10 · Gravação do vídeo até 31/10 |
| Folga e revisão | 01/11 – 02/11 | Teste de reprodução do repositório do zero |
| **Entrega** | **03/11** | Envio do repositório, dos slides e do vídeo (P2) |

## 12. Checklist da entrega

- [x] Link do repositório público no GitHub
- [x] Tratamento e preparação da base
- [x] EDA de logística executada sobre a base tratada
- [x] EDA de atendimento e perfil integrada à branch principal
- [ ] Modelo preditivo e pipeline (opcional)
- [ ] Código organizado, com nomes claros e comentários
- [x] Estrutura de pastas (`data/`, `notebooks/`, `models/`, `reports/`)
- [x] README com objetivo, base, metodologia e reprodução
- [ ] Slides de storytelling para público não técnico
- [ ] Vídeo executivo de até 5 minutos, com pelo menos um integrante apresentando
