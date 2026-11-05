from decimal import Decimal
import enum
from datetime import datetime
from sqlalchemy import DateTime,Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import current_timestamp
from app.database.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.categoria import Categoria

class ProdutoStatus(enum.Enum):
    RASCUNHO = "rascunho"
    ATIVO = "ativo"
    INATIVO = "inativo"

class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)
    categoria_id: Mapped[int] = mapped_column (ForeignKey("categorias.id"))
    sku: Mapped[str] = mapped_column(String(25), unique=True,nullable=False,index=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False)
    descricao: Mapped[str] = mapped_column(String(255),nullable=True)
    preco: Mapped[Decimal] = mapped_column(Numeric(15, 2),nullable=False)
    status: Mapped[ProdutoStatus] = mapped_column(
        Enum(ProdutoStatus),default=ProdutoStatus.RASCUNHO
    )
    criado_em: Mapped[datetime] = mapped_column(DateTime, server_default=current_timestamp(),nullable=False)

    #relacionamento com categorias
    categoria: Mapped["Categoria"] = relationship(back_populates="produtos")