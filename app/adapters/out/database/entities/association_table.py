from sqlalchemy import Table, Column, ForeignKey
from app.adapters.out.database.db import database
#database = Database()

association_table = Table(
    "order_products",
    database.Base.metadata,
    Column("order_id", ForeignKey('public.order.id'),primary_key=True),
    Column("product_id", ForeignKey('public.product.id'),primary_key=True),
)