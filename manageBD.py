import psycopg2 as pg
from models import *


class Connection:
    _user: str = 'pumxvadejwyjtj'
    _pass: str = 'f9c6675931e156cffe64579f73c770f0c72a23022544b5d744a5697e6e3f9546'
    _host: str = 'ec2-54-156-8-21.compute-1.amazonaws.com'
    _database: str = 'd96l7jhuq6fdkd'
    _port_id: int = 5432
    _connect = None

    def __init__(self) -> None:
        try:
            self._connect = pg.connect(user=self._user, password=self._pass, host=self._host, dbname=self._database,
                                       port=self._port_id)

        except Exception as ex:
            print('connection failed')
            print(ex)

        return

    def close(self) -> None:
        try:
            self._connect.close()
        except Exception as ex:
            print(f'Fallo al desconectar:\n {ex}')
        return


class LogIn(Connection):

    def __init__(self) -> None:
        super().__init__()

    def Log(self, ident: str, contrasena: str) -> Agricultor:
        cursor = self._connect.cursor()
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
        finally:
            self.close()
        return None
