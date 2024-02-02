from pydantic import BaseModel
from typing import List, Optional


class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    quantity: int


class PageResponse(BaseModel):
    limit: int
    nextOffset: Optional[int]
    prevOffset: Optional[int]
    total: int


class ListProductsResponse(BaseModel):
    data: List[ProductResponse]
    page: PageResponse | None


class OrderItem(BaseModel):
    productId: str
    purchasedQuantity: int


class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str


class Order(BaseModel):
    items: List[OrderItem]
    userAddress: UserAddress


class CreateOrderResponse(BaseModel):
    orderId: str
