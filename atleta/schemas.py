from typing import Annotated, Optional
from pydantic import UUID4, Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categoria.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='Nome do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example='24')]
    peso: Annotated[PositiveFloat, Field(description='peso do Atleta', example='123.4')]
    altura: Annotated[PositiveFloat, Field(description='altura do Atleta', example='1.34')]
    sexo: Annotated[str, Field(description='sexo do Atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Categoria do atleta')]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    id: Annotated[UUID4, Field(description='Identificador do Atleta')]
    nome: Annotated[Optional[str], Field(None, description='Nome do Atleta', example='Joao', max_length=50)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Categoria do atleta')]

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do Atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do Atleta', example='24')]