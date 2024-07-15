from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT king', max_length=20)]
    endereco: Annotated[str, Field(description='endereço do centro de treinamento', example='rua x 002', max_length=60)]
    proprietario: Annotated[str, Field(description='proprietario do centro de treinamento', example='marcos', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT king', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador da centro de treinamento')]