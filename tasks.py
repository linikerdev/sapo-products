import os
from invoke import task
from app.product.model import Product as ProductModel
from app.db import get_db, Base, engine
from wsgi import app
from app.config import source_path
from app.utils.reader import Reader


@task
def init_db(ctx):
    print("Creating all resources.")
    Base.metadata.create_all()
    engine.execute("insert into widget values (1, 'hey', 'there');")
    print(engine.execute("select * from widget;"))


@task
def drop_all(ctx):
    if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
        print("Dropping tables...")
        Base.metadata.drop_all()


def seed_things():
    classes = [ProductModel]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
   
    ingest = Reader(source_path)
    data_list = ingest.get_file_items()
    session = next(get_db())
  
    session.bulk_insert_mappings(cls, data_list)
    session.commit()


@task
def seed_db(ctx):
    if (
        input("Are you sure you want to drop all tables and recreate? (y/N)\n").lower()
        == "y"
    ):
        print("Dropping tables...")
        Base.metadata.drop_all()
        Base.metadata.create_all()
        seed_things()
        print("DB successfully seeded.")
