# Flask App para Upload e Análise de Arquivos XLSX

Este projeto é um aplicativo web simples desenvolvido com Flask para o upload de arquivos no formato `.xlsx`, onde os dados são analisados para agrupar e somar as variações de produtos e as unidades vendidas. O aplicativo lê os arquivos enviados, processa os dados e exibe os resultados diretamente na interface do usuário.

## Funcionalidades

- Upload de arquivos `.xlsx` contendo dados de vendas.
- Leitura e processamento dos dados de vendas.
- Filtragem e agrupamento por variação de produto.
- Exibição do total de unidades vendidas por variação.
  
## Requisitos

- Python 3.x
- Bibliotecas Python:
  - Flask
  - Pandas
  - openpyxl (necessária para leitura de arquivos `.xlsx`)

## Instalação

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor Flask:

    ```bash
    python app.py
    ```

5. Acesse o aplicativo no navegador em `http://127.0.0.1:5000`.

## Como Usar

1. No navegador, acesse a página inicial do aplicativo.
2. Faça o upload de um arquivo `.xlsx` com os seguintes dados obrigatórios:
   - Coluna `Nome da Variação`: Nome da variação do produto.
   - Coluna `Unidades (Pedido pago)`: Número de unidades vendidas.
   
   **Exemplo de planilha:**
   
   | Nome da Variação  | Unidades (Pedido pago) |
   |-------------------|------------------------|
   | Tamanho M         | 15                     |
   | Tamanho G         | 10                     |
   | Tamanho M         | 5                      |

3. Após o upload, o aplicativo processará o arquivo e exibirá o total de vendas por variação.

## Contribuição

Se você quiser contribuir, sinta-se à vontade para abrir um pull request ou sugerir melhorias abrindo uma issue.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
