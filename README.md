Flask App para Upload e Análise de Arquivos XLSX
Este projeto é um aplicativo web simples desenvolvido com Flask para o upload de arquivos no formato .xlsx, onde os dados são analisados para agrupar e somar as variações de produtos e as unidades vendidas. O aplicativo lê os arquivos enviados, processa os dados e exibe os resultados diretamente na interface do usuário.

Funcionalidades
Upload de arquivos .xlsx contendo dados de vendas.
Leitura e processamento dos dados de vendas.
Filtragem e agrupamento por variação de produto.
Exibição do total de unidades vendidas por variação.
Requisitos
Python 3.x
Bibliotecas Python:
Flask
Pandas
openpyxl (necessária para leitura de arquivos .xlsx)
Instalação
Clone este repositório para sua máquina local:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Inicie o servidor Flask:

bash
Copiar código
python app.py
Acesse o aplicativo no navegador em http://127.0.0.1:5000.


No navegador, acesse a página inicial do aplicativo.

Faça o upload de um arquivo .xlsx com os seguintes dados obrigatórios:

Coluna Nome da Variação: Nome da variação do produto.
Coluna Unidades (Pedido pago): Número de unidades vendidas.
Exemplo de planilha:

Nome da Variação	Unidades (Pedido pago)
Tamanho M	15
Tamanho G	10
Tamanho M	5
Após o upload, o aplicativo processará o arquivo e exibirá o total de vendas por variação.

Contribuição
Se você quiser contribuir, sinta-se à vontade para abrir um pull request ou sugerir melhorias abrindo uma issue.

Licença
Este projeto é licenciado sob a MIT License.

Esse README cobre a funcionalidade do projeto, o ambiente necessário para executá-lo e instruções básicas sobre como utilizá-lo.
