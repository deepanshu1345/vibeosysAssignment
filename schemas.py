from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class Category(str, Enum):
    finished = "finished"
    semi_finished = "semi_finished"
    raw = "raw"

class UOM(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductsBase(BaseModel):
    name : str
    category : Category
    description : str
    products_img : str
    sku : str
    unit_of_measurement : UOM
    lead_time : int

class Product(ProductsBase):
    product_id : int
    create_date : datetime
    update_date: datetime
    class Config:
        from_attributes = True

class ProductCreate(ProductsBase):
    pass

class ProductUpdate(ProductsBase):
    pass