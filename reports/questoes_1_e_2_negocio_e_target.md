# Tech Challenge – Fase 1

> **Pós-Tech FIAP · Pós-graduação em AI Scientist**

Equipe:
- Gabriel Balbine de Andrades
- Gerferson André Silva Costa
- Giulliano Alves Souza Machado
- Matheus da Silva Lima
- Yan Marcel Ramos

---

## Questão 1 – Perguntas de negócio

### 1.1 Qual problema de negócio está sendo resolvido?

O problema de negócio central consiste na incapacidade de a empresa atuar de maneira preventiva sobre a experiência do cliente, em razão da dependência de uma medição essencialmente reativa da satisfação. No cenário descrito pelo desafio, o Net Promoter Score (NPS) é coletado apenas depois do encerramento da jornada de compra, de modo que a organização toma conhecimento da insatisfação quando o ciclo já se completou e pouco resta a fazer além de remediar os danos. A consequência prática é que a área de Experiência do Cliente passa a operar em regime de retaguarda, apagando incêndios, em vez de antecipar-se aos problemas e priorizar ações corretivas com base em evidências.

Esse diagnóstico ganha relevância quando se reconhece que a experiência do cliente deixou de ser um atributo acessório e passou a constituir fator estratégico de diferenciação e de criação de valor nas organizações de serviços, conforme apontam os estudos de Muniz et al. (2026) e de Norabuena-Mendoza et al. (2025). Nesse sentido, o problema de negócio se desdobra em dois questionamentos complementares: o primeiro, de natureza analítica, busca identificar quais fatores operacionais realmente influenciam a satisfação do cliente; o segundo, de natureza estratégica, investiga como realizar a transição de uma gestão de experiência passiva e reativa para um modelo preditivo e proativo, capaz de sinalizar riscos antes mesmo da aplicação da pesquisa de NPS. A resposta a essas duas perguntas é o que permite converter dados operacionais de pedidos, logística e atendimento em insights acionáveis, orientando decisões que protejam a retenção e a saúde financeira do negócio.

### 1.2 Por que o NPS é importante para um e-commerce?

O NPS é uma das métricas mais estratégicas para o comércio eletrônico porque mede a lealdade do cliente em um ambiente em que a concorrência está a apenas um clique de distância, o que torna a recomendação espontânea um ativo particularmente valioso. A lógica da métrica, consagrada a partir dos trabalhos de Reichheld, sustenta-se na ideia de que uma única pergunta é capaz de sintetizar a disposição do consumidor em recomendar a marca, funcionando como indicador simples e, ao mesmo tempo, eficaz para identificar pontos de melhoria e aprimorar a experiência, tal como descrevem Maia, Matos e Rodrigues (s.d.). Ao segmentar os respondentes em promotores, neutros e detratores, o indicador permite mapear a variabilidade de percepção entre os consumidores e identificar quem atua como defensor da marca e quem se tornou detrator em razão de ruídos na experiência.

Em uma loja virtual, a experiência do consumidor não se resume à navegação no site: o NPS é influenciado por toda a cadeia operacional, englobando o valor do pedido, o frete, o tempo total de entrega, os atrasos logísticos e a eficiência do suporte. Essa leitura encontra respaldo no estudo de Araújo e Morgado (2024), que demonstra o efeito do Net Promoter Score sobre a frequência de compras e a experimentação de novos canais em um varejista brasileiro, evidenciando que a satisfação medida pelo indicador se traduz em comportamento concreto de compra e de expansão do relacionamento. De modo convergente, a pesquisa de Silva, Pedrosa e Gomes (2020) reforça que a avaliação sistemática da satisfação é condição para a melhoria contínua dos serviços, ainda que originalmente aplicada ao setor público, o que evidencia a transposição do conceito para contextos diversos.

No arcabouço do CRISP-DM, melhorar a satisfação medida por NPS constitui meta de negócio fundamental, porque se conecta diretamente à retenção de clientes e à saúde financeira da empresa. Clientes promotores, com notas nove e dez, atuam como embaixadores da marca e, no meio digital, essa condição se converte em avaliações positivas, recomendações em redes sociais e menor dependência de mídia paga para a atração de tráfego. O acompanhamento contínuo do indicador permite, ainda, criar estratégias específicas para converter clientes neutros, com notas sete e oito, em promotores ativos, ampliando a base leal sem custo adicional relevante. Já a identificação de clientes insatisfeitos abre espaço para intervenções rápidas, antes que migrem para concorrentes ou deixem de comprar, o que dialoga diretamente com as práticas de fechamento de ciclo descritas por Caires (s.d.) na gestão de uma célula de retratação voltada à reversão de detratores.

### 1.3 Quais áreas poderiam se beneficiar desses insights?

Todas as áreas da empresa podem se beneficiar do escore, porque a insatisfação se forma ao longo de toda a jornada, desde a interação com os canais digitais até o uso do produto propriamente dito. Na área de atendimento, a análise da relação entre a quantidade de contatos, o tempo de resolução e a satisfação do cliente permite otimizar fluxos de suporte e dimensionar equipes com base em evidências, e não em percepções. No que se refere ao layout do site e à facilidade de navegação, os dados convidam a empresa a considerar o envelhecimento e a diversidade da população brasileira, uma vez que nem todos os usuários dominam com a mesma desenvoltura as plataformas digitais, o que impõe o desafio de atender a públicos distintos sem excluir nenhum deles.

Nas formas de pagamento e nas campanhas de desconto, os insights ajudam a avaliar se a concessão de descontos ou a oferta de um número maior de parcelas compensa eventuais insatisfações ou se a percepção do produto efetivamente atende às expectativas do consumidor. Na logística e nas operações, a análise evidencia como o tempo total de entrega, os atrasos e as múltiplas tentativas de entrega afetam a nota atribuída pelo cliente, subsidiando a renegociação de contratos com transportadoras à luz de metas objetivas de desempenho, tais como as previstas nos acordos de nível de serviço discutidos por Malheiros e Mauro (s.d.). Por fim, na estratégia de Customer Relationship Management, os modelos preditivos permitem priorizar ações preventivas de retenção voltadas a clientes que vivenciaram experiências operacionais ruins, agindo antes mesmo que respondam à pesquisa de NPS e, com isso, transformando a gestão da experiência em atividade prospectiva.

### 1.4 Reflexão: como o NPS impacta a recompra, o boca a boca e o market share em e-commerce?

#### Recompra

Quanto à recompra, os promotores apresentam frequência de compra significativamente maior e menor sensibilidade a preço, pois confiam na logística e no atendimento e geram receita recorrente sem a necessidade de novos investimentos em anúncios. Os detratores, por sua vez, dificilmente voltam a comprar de forma espontânea e carregam risco iminente de churn, entendido como a taxa de cancelamento ou abandono. Essa relação não é apenas intuitiva: no estudo de Araújo e Morgado (2024), o Net Promoter Score aparece associado à intensidade de compras e à exploração de outros canais de venda, o que sustenta a tese de que a satisfação antecipa comportamento de recompra.

#### Boca a boca

No que tange ao boca a boca, o impacto é simétrico e igualmente poderoso. No polo positivo, os promotores atuam como advogados da marca, produzindo avaliações favoráveis e recomendações diretas que atraem novos compradores a custo praticamente nulo. No polo negativo, em plataformas digitais e redes sociais, o alcance de um detrator é amplificado, e reclamações públicas sobre atrasos ou mau atendimento afastam potenciais compradores antes mesmo que experimentem a loja. Essa dinâmica reforça a relevância das práticas de escuta e de resposta ao cliente, uma vez que demonstrar que a voz do consumidor foi considerada reduz o efeito destrutivo da insatisfação sobre a reputação da marca, como sugerem Muniz et al. (2026) e Caires (s.d.).

#### Market share em e-commerce

Em relação ao market share, em um mercado de alto crescimento e concorrência acirrada, a expansão da participação não depende apenas da captura de novos clientes, mas sobretudo da retenção da base existente. Empresas de comércio eletrônico com NPS elevado consolidam sua liderança porque constroem barreiras contra a concorrência fundamentadas em confiança e eficiência operacional, o que amplia o valor do tempo de relacionamento e eleva o retorno de longo prazo de cada consumidor. Sob essa ótica, o NPS deixa de ser um número de acompanhamento e passa a funcionar como indicador antecedente de desempenho financeiro, razão pela qual sua gestão proativa interessa tanto às áreas operacionais quanto à alta direção.

### 1.5 Quais indicadores de mercado poderiam complementar essa análise?

A análise construída até aqui se sustenta em variáveis internas da operação, mas ganha robustez quando confrontada com indicadores externos que situam o desempenho da empresa em relação ao mercado.

**Benchmarks de NPS.** A primeira recomendação é comparar o resultado médio da organização com a média do próprio setor de comércio eletrônico e, sobretudo, com o NPS dos concorrentes diretos, uma vez que o indicador só adquire significado pleno quando referenciado a um parâmetro de comparação. Complementam essa visão os rankings setoriais de experiência do cliente, o índice de recomendação por categoria de produto e a taxa de migração de clientes para concorrentes, sem os quais a empresa não consegue distinguir se sua insatisfação é um problema interno ou apenas o reflexo de um patamar geral de exigência do mercado.

**SLA logístico.** No que se refere ao SLA logístico, os indicadores de mercado a incorporar são o *On-Time Delivery* (OTD), entendido como o percentual de entregas realizadas dentro do prazo combinado, o *On-Time In-Full* (OTIF), que agrega a completude dos pedidos ao cumprimento do prazo, e o índice de avarias tolerável no transporte, conforme a lógica contratual discutida por Malheiros e Mauro (s.d.). Vale acrescentar o *lead time* prometido comparado ao realizado, o custo logístico por pedido e o índice de entregas frustradas, que na base corresponde às tentativas de entrega superiores a uma.

**Indicadores econômicos e de mercado.** Recomenda-se incorporar indicadores econômicos e de mercado que funcionam como pano de fundo da jornada. A inflação medida pelo IPCA, com destaque para a variação dos preços de combustíveis e de fretes, a taxa básica de juros Selic, o índice de confiança do consumidor e a taxa de desemprego ajudam a separar a insatisfação causada pela experiência de entrega da insatisfação provocada pelo contexto econômico e pela redução do poder de compra. Somam-se a eles os calendários de sazonalidade do varejo, como a Black Friday e o Natal, períodos em que os picos de demanda tendem a pressionar o prazo logístico e a derrubar o NPS, e os indicadores digitais de tráfego, taxa de conversão, abandono de carrinho e volume de avaliações públicas, que alimentam a discussão sobre boca a boca e reputação da marca.

**Indicadores complementares de experiência.** Por fim, indicadores como o *Customer Effort Score*, o CSAT externo, o *First Contact Resolution* e o *Customer Lifetime Value* fecham o conjunto ao capturar dimensões que o NPS não mede isoladamente. Vale registrar que a própria base oferece um caminho para construir indicadores derivados: o `csat_internal_score` interno em conjunto com o NPS pode funcionar como sinal complementar de satisfação, enquanto a razão entre contatos de atendimento e tempo de resolução permite compor um indicador de esforço do cliente. Essas correlações serão verificadas no decorrer das análises dos dados.

---

## Questão 2 – Definição da target

Nessa segunda etapa, busca-se uma avaliação de entendimento conceitual, não técnico.

### 2.1 Qual variável representa a satisfação do cliente?

No conjunto de dados do Tech Challenge, a variável que representa a satisfação do cliente é a `nps_score`. Trata-se de uma variável registrada em escala numérica de zero a dez, o que oferece ao cientista de dados a flexibilidade de abordá-la sob dois enquadramentos distintos, conforme o objetivo analítico.

- **Modelo de regressão:** mantém-se a `nps_score` como variável contínua, com o propósito de estimar a nota exata que o cliente atribuirá.
- **Modelo de classificação:** a nota é convertida em categorias discretas, seja pela segmentação clássica em promotores, neutros e detratores, seja pelo agrupamento binário entre clientes satisfeitos e insatisfeitos.

### 2.2 Por que ela foi escolhida?

A variável `nps_score` foi escolhida por ser o indicador padrão de lealdade e satisfação amplamente consolidado no varejo e no comércio eletrônico. Do ponto de vista analítico e de negócio, ela cumpre três papéis essenciais:

1. **Sintetizador da jornada ponta a ponta:** captura a percepção acumulada do cliente sobre todas as etapas operacionais, incluindo o preço do frete, o prazo logístico, a qualidade do produto e o suporte de atendimento.
2. **Rotulagem para a ação:** a métrica divide os clientes em grupos com comportamentos financeiros bastante distintos. Os promotores geram recompra e recomendação orgânica, enquanto os detratores representam risco de churn e de deterioração da imagem da marca.
3. **Alinhamento estratégico:** a diretoria de Experiência do Cliente adota o NPS como indicador-chave de desempenho. Empregar a `nps_score` como variável-alvo assegura que o modelo preditivo permaneça alinhado às metas de negócio da organização.

### 2.3 Em que momento da jornada essa informação é coletada?

A `nps_score` é coletada estritamente após o encerramento da jornada de compra, ou seja, de forma reativa, no pós-venda. Essa é a principal dor operacional apontada no desafio: por ser coletada apenas no fim do ciclo, a empresa não consegue agir preventivamente. Quando o cliente responde à pesquisa atribuindo uma nota de detrator, a falha logística ou o ruído no atendimento já ocorreram, a insatisfação já se consolidou e o cliente pode até ter decidido não voltar a comprar na plataforma. É justamente essa defasagem temporal que justifica a construção de um modelo capaz de antecipar o resultado da pesquisa a partir de sinais operacionais disponíveis durante a jornada.

### 2.4 Existe algum risco de usar essa variável de forma inadequada?

Sim. O uso inadequado da variável `nps_score` pode comprometer a validade do modelo preditivo por meio de quatro armadilhas clássicas:

1. **Vazamento de dados (*data leakage*):** se o objetivo é construir um modelo que antecipe a insatisfação antes ou durante a jornada, a `nps_score` jamais pode ser utilizada como variável de entrada, e qualquer informação gerada após a resposta do cliente à pesquisa deve ser excluída do treinamento, sob pena de vazamento temporal.
2. **Proxy incorreto e sinal fraco:** o NPS é um *proxy* conveniente da satisfação, mas pode funcionar apenas como sinal fraco do comportamento real. Um cliente pode atribuir nota alta por cortesia e ainda assim abandonar a plataforma, ou dar nota baixa e continuar comprando por falta de alternativas no mercado. Otimizar o modelo isoladamente para prever o NPS pode, por isso, afastar a equipe da otimização do impacto financeiro real, como retenção e valor vitalício do cliente.
3. **Viés de amostra e de seleção:** a `nps_score` só existe para os clientes que concluíram a compra e aceitaram responder à pesquisa. Os consumidores que abandonaram o processo, que tiveram pedidos cancelados antes da entrega ou que simplesmente ignoraram o convite não possuem essa variável preenchida, de modo que treinar o modelo apenas sobre os respondentes introduz viés de seleção nos dados históricos.
4. **Desalinhamento entre o ponto de corte e a ação operacional:** tratar a previsão do NPS como exercício puramente estatístico, orientado apenas pela busca de maior acurácia ou menor erro, sem definir um limite de decisão, é arriscado. Se o modelo aponta que um cliente tem risco de se tornar detrator, a empresa precisa comparar o custo da ação de retenção, como um cupom de desconto, com o custo de perder esse cliente, calibrando a regra de negócio de modo que a intervenção seja financeiramente vantajosa.

---

## Referências

ARAÚJO, Valéria Luisa Abreu de; MORGADO, Maurício Gerbaudo. Como a satisfação do cliente influencia na frequência de compras e experimentação em outros canais de vendas em um varejista no Brasil. *Retail Management Review*, São Paulo, v. 4, e-34, p. 01-10, jan./dez. 2024. DOI: [10.53946/rmr.v4i1.34](https://doi.org/10.53946/rmr.v4i1.34). Acesso em: 5 out. 2026.

CAIRES, Daniela Fernanda Ferreira. *Estudo de caso sobre a implantação de uma célula de retratação no departamento de Customer Experience (CX) de uma empresa atuante no ramo de seguros: metodologias, ferramentas e desafios no cumprimento da etapa do "Close the Loop" da pesquisa de NPS*. Trabalho de Conclusão de Curso (Graduação em Gestão Empresarial) – Faculdade de Tecnologia Dr. Thomaz Novelino (Fatec), Franca, [s.d.]. Disponível em: https://site.fatecfranca.edu.br/. Acesso em: 5 out. 2026.

MAIA, Paulo Roberto; MATOS, Jaqueline Pereira; RODRIGUES, Priscila de Carvalho. *Diagnóstico da pesquisa de satisfação Net Promoter Score (NPS) com foco no feedback dos clientes*. Pouso Alegre: Universidade do Vale do Sapucaí (Univás), [s.d.]. Disponível em: https://www.univas.edu.br/. Acesso em: 5 out. 2026.

MALHEIROS, Ariani Gomes; MAURO, Paulo Sergio Gaudêncio. *A importância do Service Level Agreement (SLA) na gestão de serviços*. São José do Rio Preto: Faculdade de Tecnologia de São José do Rio Preto (Fatec), [s.d.]. Disponível em: https://fatecsjriopreto.cps.sp.gov.br/. Acesso em: 5 out. 2026.

MUNIZ, Emerson Cleister Lima; SILVA, Edilson dos Santos; MATOS, Ana Grasiella Moraes; SAKURABA, Celso Satoshi. Gestão da experiência do cliente nos serviços: uma revisão sistemática acerca de problemas, ferramentas e soluções. *Desafio Online*, Campo Grande, v. 14, n. 1, art. 4, p. 69-97, jan./abr. 2026. DOI: [10.55028/gt8bd135](https://doi.org/10.55028/gt8bd135). Disponível em: https://desafioonline.ufms.br. Acesso em: 5 out. 2026.

NORABUENA-MENDOZA, César Hernán; FIGUEROA QUITO, Silvia Isabel; ZARZOSA-MÁRQUEZ, Eva Delfina; CHUNGA ANTÓN, Carlos Humberto; TANDAYPAN SALAZAR, Jorge Luis. Índice compuesto de experiencia del cliente para evaluar mejoras en servicios deportivos. *PROHOMINUM: Revista de Ciencias Sociales y Humanas*, [S. l.], v. 7, n. 4, p. 265-277, out./dez. 2025. E-ISSN 2665-0169. DOI: [10.47606/ACVEN/PH0396](https://doi.org/10.47606/ACVEN/PH0396). Disponível em: https://doi.org/10.47606/ACVEN/PH0396. Acesso em: 5 out. 2026.

SILVA, Wander Cleber Pereira da; PEDROSA, Glauco Vitor; GOMES, Marília Miranda Forte. Proposta de modelo de avaliação da satisfação de usuários de serviços públicos. Brasília: Universidade de Brasília, Faculdade do Gama; Information Technology Research and Application Center (ITRAC), 2020. 23 p. Disponível em: https://repositorio.unb.br/handle/10482/39291. Acesso em: 5 out. 2026.
