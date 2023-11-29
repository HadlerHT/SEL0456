# API em Flask (Projeto 4)

Este é um projeto simples de API desenvolvido em Flask que oferece funcionalidades para cálculo de fatorial e números da sequência de Fibonacci. A API valida as entradas, realiza os cálculos correspondentes e retorna os resultados em formato JSON.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- **app.py**: Arquivo principal contendo a configuração e definição das rotas da API em Flask.
- **api.py**: Arquivo com a implementação da classe `Api` que realiza validação de entrada, formatação de saída e cálculos de fatorial e Fibonacci.


## Funcionalidades

A API oferece duas principais funcionalidades:

1. **Cálculo de Fatorial (`/myapi` - Método POST):**
   - Endpoint: `/myapi`
   - Método: POST
   - Parâmetro: `"fact"` (fatorial a ser calculado)
   - Limite para entrada: 30
   - Retorna o resultado do cálculo em formato JSON.

2. **Cálculo de Fibonacci (`/myapi` - Método POST):**
   - Endpoint: `/myapi`
   - Método: POST
   - Parâmetro: `"fibo"` (número na sequência de Fibonacci a ser calculado)
   - Limite para entrada: 100
   - Retorna o resultado do cálculo em formato JSON.

## Configuração e Execução

1. Instale as dependências usando o comando: ```pip install -r requirements.txt```
2. Execute o arquivo **app.py**: ```python app.py```

A API estará disponível em *http://127.0.0.1:5000/*.


## Exemplo de Uso

### Cálculo de Fatorial e Fibonacci
- **Endpoint:** `/myapi`
- **Método:** POST
- **Corpo da Requisição:**
```json
{ 
    "fact": 5,
    "fibo": 8
}
```
- **Resposta Esperada:**
```json
{ 
    "fact": { 
        "description": "Value evaluated successfully", 
        "value": 120
    }, 
    "fibo": { 
        "description": "Value evaluated successfully", 
        "value": 21
    } 
}
```

**Observação:** Certifique-se de fornecer entradas válidas dentro dos limites especificados. Se a entrada for inválida, o valor retornado será -1, e a razão da entrada ser inválida será adicionada à descrição.
