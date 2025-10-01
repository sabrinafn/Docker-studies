from collections.abc import AsyncIterator, Sequence
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

from .config import settings  # Import DB configuration


# -----------------------------
# DATABASE MODEL
# -----------------------------
class Cat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cat_name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    colour: str = Field(default=None, index=True)
    fav_toy: str


# -----------------------------
# DATABASE CONNECTION
# -----------------------------
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables() -> None:
    # Create all database tables if they don't exist
    SQLModel.metadata.create_all(engine)


# -----------------------------
# FASTAPI LIFESPAN
# -----------------------------
@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    create_db_and_tables()  # Ensure tables exist at startup
    yield  # App runs here


# -----------------------------
# FASTAPI APP
# -----------------------------
app = FastAPI(lifespan=lifespan)


# -----------------------------
# SIMPLE GET TEST ENDPOINT
# -----------------------------
@app.get("/")
def hello() -> str:
    return "This is an answer to a simple GET request to test the server!"


# -----------------------------
# POST ENDPOINT TO ADD A CAT
# -----------------------------
@app.post("/cats/")
def adopt_cat(cat: Cat) -> Cat:
    with Session(engine) as session:
        session.add(cat)
        session.commit()
        session.refresh(cat)
        return cat


# -----------------------------
# GET ENDPOINT TO READ ALL CATS
# -----------------------------
@app.get("/cats/")
def read_cats() -> Sequence[Cat]:
    with Session(engine) as session:
        cats = session.exec(select(Cat)).all()
        return cats
