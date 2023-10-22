import psycopg2 as pg
# from psycopg2 import Connection


class Connection:
    _user: str = 'us_Connect'
    _pass: str = 'con'
    _host: str = 'localhost'
    _database: str = 'DemeterBD'
    _port_id: int = 5432
    _connect = None

    def __init__(self) -> None:
        try:
            self._connect = pg.connect(user=self._user, password=self._pass, host=self._host, dbname=self._database,
                                       port=self._port_id)
            print('connection established')

        except Exception as ex:
            print('connection failed')
            print(ex)

        return

    def close(self) -> None:
        try:
            self._connect.close()
        except Exception as ex:
            print(f'Fallo al desconectar:\n {ex}')
        print("Cerrando....")
        return


class LogIn(Connection):

    def __init__(self) -> None:
        self._user = 'us_Login'
        self._pass = 'log'
        super().__init__()

    def connect(self, ident: str, contrasena: str) -> bool:
        cursor = self._connect.cursor()
        try:
            cursor.execute("SELECT CLAVE FROM Agricultor WHERE Agricultor.AG_ID = %s", (ident,))
            result = cursor.fetchone()
            try:
                if result[0] == contrasena:
                    return True
            except TypeError as tp:
                return False

        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return False
