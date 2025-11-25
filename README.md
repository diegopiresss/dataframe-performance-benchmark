
## Observações iniciais para avaliação do Professor Trucios da disciplina ME315.

1- Esse READ.me tem todas as informações necessárias para utilização dos códigos.
2- O trabalho foi dividido em 3 partes e qmd's:
    - codigo_transformar_dados: utilizado somente para transformar os dados de csv para parquet para a leitura posterior.
    - codigo_trabalho: onde os testes foram rodados propriamente ditos, me aproveitei da estrutura de chunks já que poderia rodar chunks específicos em uma ordem específica. Ele provavelmente não vai rodar de primeira e se rodar irá demorar MUITO dependendo do computador (for loops lendo datasets de 30gb 10 vezes).

3- ONDE OLHAR O RESULTADO FINAL? Entrar no arquivo analise_benchmark.qmd ou analise_benchmark.htlm em que foi feita a análise de todas as amostras geradas em codigo_trabalho.

Estruturamos dessa forma para maior facilidade tanto da execução dos testes tanto para a correção posteriormente.

4- Abaixo tem o link do drive que leva direto para os datasets (tanto csv quanto parquet)


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
├── analise_benchmark.qmd        # Contém a análise final e o relatório final das análises feitas
└── README.md
```

Dados (Download Necessário)

Devido ao tamanho, os datasets brutos não estão no GitHub. 

https://drive.google.com/drive/u/2/folders/1-Si-q3Dhy9AUNdVEoqspdBTU1rQ9MZQT

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
