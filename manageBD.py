from datetime import datetime as dt
from os import stat
import psycopg2 as pg
from models import *


class Connection:
    _user: str = 'pumxvadejwyjtj'
    _pass: str = 'f9c6675931e156cffe64579f73c770f0c72a23022544b5d744a5697e6e3f9546'
    _host: str = 'ec2-54-156-8-21.compute-1.amazonaws.com'
    _database: str = 'd96l7jhuq6fdkd'
    _port_id: int = 5432
    _connector = None

    def connect(self) -> None:
        try:
            self._connector = pg.connect(user=self._user, password=self._pass, host=self._host, dbname=self._database,
                                         port=self._port_id)

        except Exception as ex:
            print('connection failed')
            print(ex)

        return

    def close(self) -> None:
        try:
            self._connector.close()
        except Exception as ex:
            print(f'Fallo al desconectar:\n {ex}')
        return


class LogIn(Connection):

    def __init__(self) -> None:
        super().__init__()
        super().connect()

    def log(self, ident: str, contrasena: str) -> Agricultor:
        cursor = self._connector.cursor()
        try:
            cursor.execute("SELECT * FROM Agricultor WHERE Agricultor.AG_ID = %s", (ident,))
            result = cursor.fetchone()
            try:
                if contrasena == result[2]:
                    return Agricultor(result[0], result[1], result[3] + ' ' + result[4])
            except TypeError as tp:
                return None

        except Exception as ex:
            print(ex)

        return None


class CropState(Connection):
    def __init__(self) -> None:
        super().__init__()
        super().connect()

    def load_usr_crops(self, usr: Agricultor) -> set[Cultivo]:
        cursor = self._connector.cursor()
        op_result = set()
        cursor.execute("SELECT DISTINCT E.CUL_ID, C.NOMBRE, C.PH_MIN, C.PH_MAX, C.TEMPE_MIN, C.TEMPE_MAX, C.HUM_MIN, "
                       "C.HUM_MAX FROM Estado E JOIN Cultivo C ON E.CUL_ID = C.CUL_ID WHERE E.AG_ID = %s", (usr.id,))
        result = cursor.fetchall()
        for i in result:
            op_result.add(Cultivo(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        return op_result

    def search_crop(self, name: str) -> Cultivo:
        cursor = self._connector.cursor()
        cursor.execute("SELECT * FROM CULTIVO WHERE CULTIVO.nombre = %s", (name,))
        result = cursor.fetchone()
        return Cultivo(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])


class Statistic(Connection):
    lastRegister: dt = None
    lastAlert: dt = None

    def __init__(self) -> None:
        super().__init__()
        super().connect()

    def stats(self, usr: Agricultor) -> Estado:
        conn = self._connector.cursor()
        result = []

        if self.lastRegister is None:
            try:
                conn.execute("SELECT * FROM Estado WHERE Estado.AG_ID = %s ORDER BY fecha ASC, hora ASC", (usr.id,))
                result = conn.fetchall()

            except Exception as ex:
                print(ex)

        else:
            try:
                conn.execute(
                    "SELECT * FROM Estado WHERE Estado.AG_ID = %s AND Estado.Fecha >= %s AND Estado.Hora > %s ORDER "
                    "BY fecha ASC, hora ASC",
                    (usr.id, self.lastRegister.date(), self.lastRegister.time()))
                result = conn.fetchall()

            except Exception as ex:
                print(ex)

        if len(result) == 0:
            return Estado()
        self.lastRegister = dt(year=result[-1][2].year, month=result[-1][2].month, day=result[-1][2].day,
                               hour=result[-1][3].hour, minute=result[-1][3].minute, second=result[-1][3].second,
                               microsecond=result[-1][3].microsecond)

        return Estado(usr, set(result))

    def search_alerts(self, usr: Agricultor) -> Alerta:
        conn = self._connector.cursor()
        result = []

        if self.lastAlert is None:
            try:
                conn.execute("SELECT E.AG_ID, E.CUL_ID, E.FECHA, E.HORA, E.PH, E.TEMPE, E.HUM FROM Estado E JOIN "
                             "Cultivo C ON E.CUL_ID = C.CUL_ID WHERE (E.PH < C.PH_MIN OR "
                             "E.PH > C.PH_MAX) OR (E.TEMPE < C.TEMPE_MIN OR E.TEMPE > C.TEMPE_MAX) OR (E.HUM < "
                             "C.HUM_MIN OR E.HUM > C.HUM_MAX) AND E.AG_ID = %s", (usr.id,))
                result = conn.fetchall()
            except Exception as ex:
                print(ex)

        else:
            try:
                conn.execute(
                    "SELECT E.AG_ID, E.CUL_ID, E.FECHA, E.HORA, E.PH, E.TEMPE, E.HUM FROM Estado E JOIN "
                    "Cultivo C ON E.CUL_ID = C.CUL_ID WHERE (E.PH < C.PH_MIN OR "
                    "E.PH > C.PH_MAX) OR (E.TEMPE < C.TEMPE_MIN OR E.TEMPE > C.TEMPE_MAX) OR (E.HUM < "
                    "C.HUM_MIN OR E.HUM > C.HUM_MAX) AND E.AG_ID = %s AND Estado.Fecha >= %s AND Estado.Hora > %s ORDER"
                    "BY fecha ASC, hora ASC",
                    (usr.id, self.lastAlert.date(), self.lastAlert.time()))
                result = conn.fetchall()

            except Exception as ex:
                print(ex)

        if len(result) == 0:
            return Alerta()
        self.lastRegister = dt(year=result[-1][2].year, month=result[-1][2].month, day=result[-1][2].day,
                               hour=result[-1][3].hour, minute=result[-1][3].minute, second=result[-1][3].second,
                               microsecond=result[-1][3].microsecond)

        return Alerta(usr, set(result))
