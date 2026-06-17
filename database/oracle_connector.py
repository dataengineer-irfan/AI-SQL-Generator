import oracledb

from config.settings import settings


class OracleConnector:

    def __init__(self):
        self.connection = None

    def connect(self):
        if settings.ORACLE_SYSDBA:
            self.connection = oracledb.connect(
                user=settings.ORACLE_USER,
                password=settings.ORACLE_PASSWORD,
                dsn=settings.ORACLE_DSN,
                mode=oracledb.AUTH_MODE_SYSDBA
            )
        else:
            self.connection = oracledb.connect(
                user=settings.ORACLE_USER,
                password=settings.ORACLE_PASSWORD,
                dsn=settings.ORACLE_DSN
            )
        return self.connection

    def get_connection(self):
        if self.connection is None:
            self.connect()
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
