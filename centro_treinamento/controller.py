from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.contrib.dependencias import DatabaseDependency
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel
router = APIRouter()

@router.post(path='/', summary='Criar um novo Centro de treinamento', status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)
async def post(db_session: DatabaseDependency, centro_treinamento_in:CentroTreinamentoIn= Body(...))-> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    
    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out


 
@router.get(path='/', summary='Consultar Centro de treinamento', status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])
async def query(db_session: DatabaseDependency)-> list[CentroTreinamentoOut]:
    centro_treinamento: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return centro_treinamento

@router.get(path='/{id}', summary='Consultar uma Centro de treinamento pelo id', status_code=status.HTTP_200_OK, response_model=CentroTreinamentoOut)
async def query(id: UUID4,db_session: DatabaseDependency)-> list[CentroTreinamentoOut]:
    centro_treinamento: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Centro de treinamento não encontrada no id: {id}')
    
    return centro_treinamento 