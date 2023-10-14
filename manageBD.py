import psycopg2 as pg


class TestConnection:
    __user: str = 'postgres'
    __pass: str = 'udc'
    __host: str = 'localhost'
    __database: str = 'DemeterBD'
    __port_id: int = 5432

    def __init__(self) -> None:
        try:
            connect = pg.connect(user=self.__user, password=self.__pass, host=self.__host, dbname=self.__database, port=self.__port_id)
            print('connection established')
            connect.close()
        except Exception as ex:
            print('connection failed')
            print(ex)

        return
