import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.database.base import Base

# Acha a pasta raiz do projeto (subindo 3 níveis a partir de app/database/connection.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = BASE_DIR / ".env"

# Carrega o .env explicitamente apontando para o caminho correto na raiz
load_dotenv(dotenv_path=env_path)

# Pega a URL do Postgres
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(f"A variável DATABASE_URL não foi encontrada no arquivo: {env_path}")

# Cria a engine de conexão com o PostgreSQL
engine = create_engine(DATABASE_URL)

# Fábrica de sessões para as transações
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Abre uma sessão com o banco, entrega para uso e garante o fechamento no final."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()