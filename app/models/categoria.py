from app.database.base import Base
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.produto import Produto

class Categoria(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30),nullable=False)

    #relacionamento com produto
    produtos: Mapped[list["Produto"]] = relationship(back_populates="categorias",cascade="all,delete-orphan")