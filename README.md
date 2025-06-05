# Conversor CSV para XLSX com Múltiplas Abas

Script Python que converte arquivos CSV grandes (acima de 1 milhão de linhas) para formato XLSX, dividindo automaticamente em múltiplas abas.

## 🚀 Uso

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Colocar arquivos no mesmo diretório:**
   ```
   📁 pasta/
   ├── c.py
   ├── seu_arquivo.csv
   ```

3. **Editar o nome do arquivo no script:**
   ```python
   # Linha 38 do arquivo c.py
   csv_to_xlsx_sheets('SEU_ARQUIVO.csv', 'RESULTADO.xlsx')
   ```

4. **Executar:**
   ```bash
   python c.py
   ```

## 📊 Resultado

- **Entrada**: `arquivo.csv` (1.6M+ linhas)
- **Saída**: `arquivo.xlsx` com múltiplas abas:
  - `Dados_1`: 1.000.000 linhas
  - `Dados_2`: 600.000 linhas (restante)

## ⚙️ Configurações

O script está configurado para:
- **Delimitador**: `;` (ponto e vírgula)
- **Encoding**: `utf-8`
- **Máximo por aba**: 1.000.000 linhas

Para alterar, edite os parâmetros na função `csv_to_xlsx_sheets()`.

## 🔧 Resolução de Problemas

**Erro "No module named 'openpyxl'":**
```bash
pip install openpyxl
```

**Erro de parsing CSV:**
- Verifique se o delimitador é `;`
- Verifique se o encoding é `utf-8`

**Arquivo muito grande:**
- O script otimiza automaticamente a memória
- Para arquivos >2GB, considere dividir antes

## 📝 Limitações

- Excel: máximo 1.048.576 linhas por aba
- Requer pandas e openpyxl instalados
- Funciona apenas com CSV delimitado por `;`
