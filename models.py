from dataclasses import dataclass
from datetime import date, time


@dataclass(frozen=True, order=False)
class Agricultor:
    id: str
    mail: str
    full_name: str


@dataclass(frozen=True, order=False)
class Cultivo:
    __id: str
    __name: str
    __ph_min: float
    __ph_max: float
    __temp_min: float
    __temp_max: float
    __hum_min: float
    __hum_max: float


class Estado:
    __agid: str
    history: set[tuple]

    def __init__(self, farmer: Agricultor, data: set[tuple]) -> None:
        self.__agid = farmer.id
        self.history = data
        return

    def update(self, new: list[tuple]) -> None:
        for i in new:
            self.history.add(i)
        return


class Alerta(Estado):

    def __init__(self, farmer: Agricultor, data: set[tuple]) -> None:
        super().__init__(farmer, data)

