from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import IntegrityError
import models, schemas
from db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/product/list", response_model=list[schemas.Product])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    skip = (page - 1) * 10
    product = db.query(models.Products).offset(skip).limit(10).all()
    return product


@app.get("/product/{pid}/info", response_model=schemas.Product)
def product_info(pid: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.product_id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return product


@app.post("/product/add", response_model=schemas.Product)
def product_add(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = models.Products(**product.model_dump())
    try:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=" SKU exists")


@app.put("/product/{pid}/update", response_model=schemas.Product)
def product_update(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Products).filter(models.Products.product_id == pid).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product Not Found")

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product
