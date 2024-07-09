from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='Nome do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example='24')]
    peso: Annotated[PositiveFloat, Field(description='peso do Atleta', example='123.4')]
    altura: Annotated[PositiveFloat, Field(description='altura do Atleta', example='1.34')]
    sexo: Annotated[str, Field(description='sexo do Atleta', example='M', max_length=1)]