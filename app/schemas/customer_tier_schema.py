from pydantic import BaseModel


class CustomerTierCreate(BaseModel):

    name: str

    first_slab: float

    second_slab: float

    third_slab: float