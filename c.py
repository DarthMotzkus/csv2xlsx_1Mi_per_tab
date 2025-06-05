import pandas as pd

def csv_to_xlsx_sheets(csv_file, xlsx_file, max_rows=1000000):
    """
    Converte CSV para XLSX com múltiplas abas
    
    Parâmetros:
    - csv_file: caminho do arquivo CSV
    - xlsx_file: caminho do arquivo XLSX de saída  
    - max_rows: máximo de linhas por aba (padrão: 1 milhão)
    """
    print("Carregando CSV...")
    
    # Ler CSV com delimitador ; e encoding utf-8
    df = pd.read_csv(csv_file, 
                    delimiter=';', 
                    encoding='utf-8',
                    on_bad_lines='skip',
                    low_memory=False)
    
    print(f"✅ CSV carregado com sucesso!")
    print(f"Colunas: {len(df.columns)}")
    print(f"Primeiras colunas: {list(df.columns[:5])}")
    
    print(f"Total de linhas: {len(df):,}")
    print(f"Criando abas com até {max_rows:,} linhas cada...")
    
    # Dividir em múltiplas abas
    with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
        for i in range(0, len(df), max_rows):
            chunk = df[i:i+max_rows]
            sheet_name = f'Dados_{i//max_rows + 1}'
            chunk.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Aba '{sheet_name}' criada: {len(chunk):,} linhas")
    
    print(f"✅ Arquivo criado: {xlsx_file}")

# EXECUÇÃO
if __name__ == "__main__":
    csv_to_xlsx_sheets('sos_esocial_2024.csv', 'sos_esocial_2024.xlsx')