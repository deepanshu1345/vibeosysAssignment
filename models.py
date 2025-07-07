from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func
from db import Base
import enum


class Category(enum.Enum):
    finished = "finished"
    semi_finished = "semi_finished"
    raw = "raw"


class UOM(enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"


class Products(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(Category), nullable=False)
    description = Column(String(250))
    products_img = Column(String)
    sku = Column(String(100), unique=True)
    unit_of_measurement = Column(Enum(UOM), nullable=False)
    lead_time = Column(Integer)
    create_date = Column(TIMESTAMP, server_default=func.now())
    update_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())