# SEL0456
Repositório para disciplina SEL0456 - Técnicas em Desenvolvimento de Software Livre

## Conteúdo

### Projeto1
  Diretório contendo os arquivos do Trabalho 1 (uso de Git e Makefile).

  ***Descrição:***
  - O projeto é composto por um arquivo principal (main.c) e aquivos com funções implementadas em C, assim como seus respectivos arquivos de cabeçalho.

  - Os arquivos são divididos entre os diretórios:
    - `src`: Armazena as implementações de funções (.c);
    - `include`: Define os cabeçalhos das funções implementadas (.h);
    - `build`: Armazena temporariamente os arquivos compilados de cada bloco de código (.o);
      
  - A construção do projeto pode ser feita a partir dos arquivos make, as seguintes receitas foram implementadas:
    - ```make```: Compilação completa do projeto;
    - ```make clean```: Exclusão dos blocos de arquivos compilados do diretório `build`;
    - ```make distclean```: Exclusão de todos os aquivos compilados do projeto;
