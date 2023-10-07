import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base


Base: declarative_base = declarative_base()


class FileHash(Base):
    __tablename__ = "file_hash"

    id = Column(Integer, primary_key=True)
    timestamp_id = Column(Integer, ForeignKey("timestamps.id"))
    file_path = Column(String)
    hash_type = Column(String)
    file_hash = Column(String)


class FileHashHistory(Base):
    __tablename__ = "file_hash_history"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    file_path = Column(String)
    hash_type = Column(String)
    file_hash = Column(String)


class FileAccessCount(Base):
    __tablename__ = "file_access_count"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    file_path = Column(String, ForeignKey("file_hash.file_path"))
    access_count = Column(Integer)


class EnabledHash(Base):
    __tablename__ = "enabled_hash"

    id = Column(Integer, primary_key=True)
    hash_type = Column(String)
    enabled = Column(Integer)


class Timestamp(Base):
    __tablename__ = "timestamps"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


def create_database(db_path: str):
    engine = create_engine(db_path)
    Base.metadata.create_all(engine)
    print(f"Database created at {db_path}")


if __name__ == "__main__":
    # Pass your database path here
    db_path='sqlite:////home/hendrik/Documents/Projects/TBDiC/data/HashKeeper.db'
    create_database(db_path)
