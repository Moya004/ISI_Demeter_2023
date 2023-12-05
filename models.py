from dataclasses import dataclass
from datetime import date, time


@dataclass(frozen=True, order=False)
class Agricultor:
    id: str = ''
    mail: str = ''
    full_name: str = ''


@dataclass(frozen=True, order=False)
class Cultivo:
    __id: str = ''
    __name: str = ''
    __ph_min: float = ''
    __ph_max: float = ''
    __temp_min: float = ''
    __temp_max: float = ''
    __hum_min: float = ''
    __hum_max: float = ''


class Estado:
    __ag: Agricultor
    history: list

    def __init__(self, farmer: Agricultor = (), data: list[tuple] = ()) -> None:
        self.__ag = farmer
        self.history = data
        return

    def update(self, new: list[tuple]) -> None:
        for i in new:
            self.history.append(i)
        return

    def __len__(self):
        return self.history.__len__()

    def __str__(self) -> str:
        return f'User: {self.__ag}\ndata: {self.history}'


class Alerta(Estado):

    def __init__(self, farmer: Agricultor = Agricultor(), data: list[tuple] = list()) -> None:
        super().__init__(farmer, data)
