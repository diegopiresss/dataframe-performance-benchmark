# 📊 Benchmark de Processamento de Dados: Pandas vs. Polars vs. R

Este repositório contém os códigos e resultados de um estudo comparativo de performance entre as principais bibliotecas de manipulação de dados em Python e R. O objetivo é analisar velocidade de leitura, consumo de memória RAM e eficiência de armazenamento (CSV vs. Parquet) em um ambiente local (notebook).

## 📂 Estrutura do Projeto

Para reproduzir os testes, organize seus arquivos da seguinte forma:

```text
.
├── datasets/                   # (Não incluído no git) Baixe do link abaixo
│   ├── giga_yellow/            # Dataset de grande volume (>1GB)
│   ├── stackoverflow_wide/     # Dataset com muitas colunas
│   └── yellow_long/            # Dataset com milhões de linhas
│
├── resultados/                 # Onde os logs brutos dos testes serão salvos
│   ├── A1_gigayellow_.../      # Pastas geradas automaticamente pelo script
│   └── ...
│
├── codigo_transformar_dados.qmd # Script para converter os CSVs originais em Parquet
├── codigo_trabalho.qmd          # Script principal que executa os benchmarks
├── monitor_ram.py               # Script auxiliar para monitoramento de recursos em tempo real
├── MASTER_BENCHMARK_DATA.csv    # Tabela consolidada com todos os resultados finais
└── README.md
```

Dados (Download Necessário)

Devido ao tamanho, os datasets brutos não estão no GitHub. [Insira aqui o Link do seu Google Drive]

    Baixe os arquivos.

    Crie uma pasta chamada datasets na raiz do projeto.

    Extraia os dados dentro dela conforme a estrutura acima.

Como Executar

Pré-requisitos

    Python 3.13+ (Bibliotecas: polars, pandas, pyarrow, numpy)

    R 4.4+ (Pacotes: readr, arrow, dplyr, glue)

    Quarto (para renderizar e executar os arquivos .qmd)

Passo a Passo

    Preparação dos Dados: Execute o arquivo codigo_transformar_dados.qmd. Ele irá ler os arquivos CSV originais na pasta datasets/ e gerar as versões .parquet necessárias para o comparativo de formatos.

    Execução do Benchmark: Rode o codigo_trabalho.qmd. Este script irá:

        Iterar sobre todos os cenários (Giga, Wide, Long).

        Testar cada biblioteca (Pandas, Polars, R Base, R Readr).

        Acionar o monitor_ram.py em segundo plano para medir o pico de memória.

        Salvar os logs individuais na pasta resultados/.

    Análise dos Resultados: O arquivo MASTER_BENCHMARK_DATA.csv contém a compilação final das métricas (Tempo, RAM, Speedup). Você pode usá-lo para gerar gráficos ou ler as análises diretamente no relatório final.

Metodologia

O estudo avaliou três cenários (A1, A2, A3) focando em:

    A1 (Leitura Pura): Velocidade bruta de ingestão.

    A2 (Tipagem Manual): Impacto de definir o schema explicitamente.

    A3 (Seleção de Colunas): Eficiência de Projection Pushdown.

Hardware de Teste:

    Processador: Intel Core i7

    RAM: 16 GB (Limite físico intencional)

    Armazenamento: SSD NVMe 500gb

Resultados Principais (Resumo)

    Formato: O uso de Parquet gerou ganhos de até 25x em relação ao CSV.

    Performance: O Polars foi a ferramenta mais eficiente para processar CSVs gigantes, enquanto o R (readr) mostrou excelente desempenho em arquivos Parquet.

    Memória: Em datasets >1GB, todas as bibliotecas saturaram os 16GB de RAM, evidenciando a necessidade de estratégias como Lazy Evaluation ou Chunking para máquinas locais.

    Desenvolvido por Diego Pires, Henry Koiti Honda e Joaquim Bertoldi Nucci
