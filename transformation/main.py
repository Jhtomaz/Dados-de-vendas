from pathlib import Path
import pandas as pd

path_name = Path(__file__).parent.parent / "data" / "Base_Vendas_Aula_PowerBI - Vendas.csv"
output_path = Path(__file__).parent.parent / "output" / "Base_Vendas_Aula_PowerBI - Vendas_Transformada.csv"
def create_dataframe(path: Path) -> pd.DataFrame:
    print(f"Carregando dados do arquivo: {path}")

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path, decimal=',')
    print(f"Dados carregados com sucesso. Número de linhas: {len(df)}")
    return df

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    print("Normalizando nomes das colunas...")
    df_sales = df.rename(
        columns={
            "Data":"data",
            "ID_Venda":"id_venda",
            "ID_Cliente":"id_cliente",
            "ID_Produto":"id_produto",
            "ID_Vendedor":"id_vendedor",
            "Quantidade":"quantidade",
            "Preco_Unitario":"preco_unitario",
        }
    )

    print("Nomes das colunas normalizados com sucesso.")
    return df_sales

def column_types(df: pd.DataFrame) -> pd.DataFrame:
    print("Alterando tipos de dados das colunas...")
    df = df.astype({
        'data': 'datetime64[ns]',
        'id_venda': 'string',
        'id_cliente': 'int64',
        'id_produto': 'int64',
        'id_vendedor': 'int64',
        'quantidade': 'int64',
        'preco_unitario': 'float64'
    })
    print("Tipos de dados das colunas alterados com sucesso.")
    return df

def data_transformations() -> pd.DataFrame:
    print("Iniciando transformações de dados...")
    df = create_dataframe(path_name)
    df = normalize_columns(df)
    df = column_types(df)
    print("Transformações de dados concluídas com sucesso.")
    df.to_csv(output_path, index=False, decimal=',')
    print(f"Dados transformados salvos em: {output_path}")

    
if __name__ == "__main__":
    data_transformations()