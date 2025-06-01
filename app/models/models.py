from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Subgrupo(Base):
    __tablename__ = "subgrupo"
    id_subgrupo = Column(Integer, primary_key=True, index=True)
    nome_subgrupo = Column(String, nullable=False)
    publicacoes = relationship("Publicacao", back_populates="subgrupo")
    integrantes = relationship("Integrante", back_populates="subgrupo")

class Publicacao(Base):
    __tablename__ = "publicacao"
    id_publicacao = Column(Integer, primary_key=True, index=True)
    id_subgrupo = Column(Integer, ForeignKey("subgrupo.id_subgrupo"))
    tipo = Column(String)
    data_publicacao = Column(Date)
    subgrupo = relationship("Subgrupo", back_populates="publicacoes")
    downloads = relationship("Download", back_populates="publicacao")

class Download(Base):
    __tablename__ = "download"
    id_download = Column(Integer, primary_key=True, index=True)
    id_publicacao = Column(Integer, ForeignKey("publicacao.id_publicacao"))
    data_download = Column(Date)
    publicacao = relationship("Publicacao", back_populates="downloads")

class Integrante(Base):
    __tablename__ = "integrante"
    id_integrante = Column(Integer, primary_key=True, index=True)
    nome_integrante = Column(String)
    e_mail_integrante = Column(String, unique=True)
    password = Column(String)  # deve armazenar hash bcrypt
    id_subgrupo = Column(Integer, ForeignKey("subgrupo.id_subgrupo"))
    subgrupo = relationship("Subgrupo", back_populates="integrantes")
