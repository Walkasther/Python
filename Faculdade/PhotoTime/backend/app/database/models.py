# backend/app/database/models.py

from sqlalchemy import (Column, Integer, String, Enum, DateTime, ForeignKey,
                        DECIMAL, JSON)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Administrador(Base):
    __tablename__ = "administradores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)


class Quiosque(Base):
    __tablename__ = "quiosques"
    id = Column(Integer, primary_key=True, index=True)
    identificador_unico = Column(String(255), unique=True, index=True, nullable=False)
    nome_amigavel = Column(String(255), nullable=False)
    localizacao = Column(String(255), nullable=True)
    status = Column(Enum('ativo', 'inativo', 'offline', 'manutencao', name='status_quiosque'), nullable=False,
                    default='inativo')
    ultimo_heartbeat = Column(DateTime, nullable=True)
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)

    sessoes = relationship("Sessao", back_populates="quiosque")


class TipoProduto(Base):
    __tablename__ = "tipos_produto"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    preco_base = Column(DECIMAL(10, 2), nullable=False)
    configuracao_quantidade = Column(JSON)


class Sessao(Base):
    __tablename__ = "sessoes"
    id = Column(Integer, primary_key=True, index=True)
    quiosque_id = Column(Integer, ForeignKey("quiosques.id"), nullable=False)
    codigo_sessao = Column(String(8), unique=True, index=True, nullable=False)
    status = Column(Enum('ativa', 'expirada', 'finalizada', name='status_sessao'), nullable=False, default='ativa')
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)

    quiosque = relationship("Quiosque", back_populates="sessoes")
    pedidos = relationship("Pedido", back_populates="sessao")


class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    sessao_id = Column(Integer, ForeignKey("sessoes.id"), nullable=False)
    valor_total = Column(DECIMAL(10, 2), nullable=False)
    status_pagamento = Column(Enum('pendente', 'aprovado', 'recusado', name='status_pagamento_pedido'), nullable=False,
                              default='pendente')
    status_impressao = Column(Enum('nao_iniciado', 'imprimindo', 'concluido', 'falha', name='status_impressao_pedido'),
                              nullable=False, default='nao_iniciado')
    id_transacao_pagamento = Column(String(255), nullable=True)
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)

    sessao = relationship("Sessao", back_populates="pedidos")
    fotos = relationship("Foto", back_populates="pedido")


class Foto(Base):
    __tablename__ = "fotos"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    caminho_original = Column(String(255), nullable=False)
    caminho_editado = Column(String(255), nullable=True)
    dados_edicao = Column(JSON)

    pedido = relationship("Pedido", back_populates="fotos")
