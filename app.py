from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        if file and file.filename.endswith('.xlsx'):
            # Salvar o arquivo na pasta 'uploads'
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Ler os dados do XLSX
            df = pd.read_excel(filepath)

            # Filtrar e agrupar as variações e unidades vendidas
            df.columns = df.columns.str.strip()  # Remove espaços em branco dos nomes das colunas
            df = df[df['Nome da Variação'] != '-']  # Remove linhas com apenas '-'

            # Agrupar e somar as unidades vendidas
            totais = df.groupby('Nome da Variação')['Unidades (Pedido pago)'].sum().reset_index()

            # Formatar os resultados
            resultados = [f'Total de vendas no {row["Nome da Variação"]}: {row["Unidades (Pedido pago)"]}' for index, row in totais.iterrows()]

    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
