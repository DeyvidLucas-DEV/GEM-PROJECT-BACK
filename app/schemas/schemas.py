from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class AdminLogin(BaseModel):
    e_mail_integrante: str
    password: str

class SubgrupoBase(BaseModel):
    nome_subgrupo: str

class SubgrupoCreate(SubgrupoBase):
    pass

class Subgrupo(SubgrupoBase):
    id_subgrupo: int
    model_config = {"from_attributes": True}

class IntegranteBase(BaseModel):
    nome_integrante: str
    e_mail_integrante: str
    id_subgrupo: int

class IntegranteCreate(IntegranteBase):
    password: str

class Integrante(IntegranteBase):
    id_integrante: int
    model_config = {"from_attributes": True}
