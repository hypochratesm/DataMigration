import os
import sys
import pandas as pd
import partial
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class DBConn:

    def __init__(self
                 , user: str
                 , password: str
                 , host: str
                 , port: str
                 , name: str = str):
        query = f"mysql://{user}:{password}@{host}:{port}/{name}?charset=utf8"
        self.conn = create_engine(query, pool_recycle=1)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.conn))

        Base = declarative_base(self.conn)
        metadata = Base.metadata
        metadata.reflect(self.conn)

        self.tables = list(metadata.tables.keys())

        for table in self.tables:
            table_inst = metadata.tables[table]
            setattr(self, table, table_inst)
            setattr(self, f"get_{table}", partial(self._select, model=table_inst))
            setattr(self, f"add_{table}", partial(self._select, model=table_inst))

    def _select(self, model):
        sql = self.session.query(model)
        df = pd.read_sql(str(sql), self.conn)
        df.columns = [col.replace(f"{str(model)}_", "") for col in df.columns]
        return df

    def _insert(self, model, **kwargs):
        sql = model.insert().values(**kwargs)
        self.execute(sql)

    def execute(self, sql: str):
        self.conn.execute(sql)
        self.commit()

    def commit(self):
        self.session.commit()
