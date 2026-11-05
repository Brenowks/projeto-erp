from app.database.connection import engine
from app.database.base import Base

# Importe todos os seus models para que eles sejam registrados no Base.metadata
from app.models.categoria import Categoria
from app.models.produto import Produto

def criar_banco():
    print("Criando tabelas no banco de dados...")
    # Isso lê todas as classes que herdam de Base e cria as tabelas correspondentes
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    criar_banco()