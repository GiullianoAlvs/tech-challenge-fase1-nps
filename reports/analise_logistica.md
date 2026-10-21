# Logística e satisfação do cliente

Análise dos 2.500 pedidos da [base preparada](../data/processed/nps_tratado.csv). A regra adotada é detrator `< 7`, neutro `7 a < 9` e promotor `>= 9`, sem arredondamento. O [notebook de logística](../notebooks/02_eda_logistica.ipynb) contém o cálculo, as tabelas e os gráficos.

## Resultados

| Dias de atraso | Pedidos | Nota média | Detratores |
|---:|---:|---:|---:|
| 0 | 277 | 6,86 | 143 (51,62%) |
| 1 | 615 | 5,55 | 455 (73,98%) |
| 2 | 646 | 4,58 | 568 (87,93%) |
| 3–4 | 795 | 3,10 | 776 (97,61%) |
| 5 ou mais | 167 | 1,28 | 167 (100%) |

O atraso tem correlação de Spearman de **−0,586** com a nota. A diferença entre os grupos sem atraso e com um dia é de **−1,31 ponto** na média. A piora prossegue nos dias seguintes; a base não revela um ponto único de ruptura causal. Mesmo sem atraso, 51,62% dos pedidos são de detratores. [Veja o volume e a detração por faixa](figures/logistica_detratores_por_atraso.png) e a [distribuição das notas individuais](figures/logistica_distribuicao_notas_atraso.png).

As correlações isoladas com a nota são **+0,000** para o prazo previsto, **+0,026** para tentativas de entrega e **−0,040** para o valor do frete. As taxas de detratores por grupos dessas variáveis oscilam menos que por atraso. [Comparação das quatro variáveis logísticas](figures/logistica_correlacoes.png) e [taxas por prazo, tentativas e frete](figures/logistica_prazo_tentativas_frete.png).

## Implicações

Monitorar entregas desde o primeiro dia fora do prazo e acompanhar os casos que acumulam dias de atraso são hipóteses operacionais para teste. Qualquer ação deve registrar quantos pedidos alcançou, custo e satisfação posterior. A análise isolada não sustenta uma regra de prioridade baseada apenas em frete, número de tentativas ou prazo previsto.

Os resultados descrevem os pedidos fornecidos. O arquivo não contém datas dos eventos nem comprova representatividade de outros períodos. As diferenças são associações observadas; reduzir atrasos não tem efeito causal quantificado por esta análise.
