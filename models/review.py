from models.base_model import BaseModel


class State(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""
