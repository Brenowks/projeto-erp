import enum
from datetime import datetime
from sqlalchemy import DateTime,Enum, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import current_timestamp
from app.database.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.produto import Produto

class TipoMovimentacao(enum.Enum):
    ENTRADA = "Entrada"
    SAIDA = "Saida"

class MovimentacaoEstoque(Base):
    __tablename__ = "movimentacao_estoque"

    id: Mapped[int] = mapped_column(primary_key=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"))
    tipo: Mapped[str] = mapped_column(Enum(TipoMovimentacao),nullable=False)
    quantidade: Mapped[int] = mapped_column(Numeric(15, 2),nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, server_default=current_timestamp(),nullable=False)

    produtos: Mapped["Produto"] = relationship(back_populates="movimentacao_estoque")
