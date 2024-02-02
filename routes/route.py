from fastapi import APIRouter, Query
from typing import Optional
from schemas.schema import ListProductsResponse, Order, CreateOrderResponse
from controllers.ProductController import listProducts
from controllers.OrderController import createOrder

router = APIRouter()


# TODO: Incase the routes increases, we can create file for handling model routes separately
@router.get("/products", response_model=ListProductsResponse)
async def fetchProducts(
        limit: int = Query(default=10, title="Number of records to fetch", ge=1),
        offset: int = Query(default=0, ge=0),
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
) -> ListProductsResponse:
    return listProducts(limit, offset, min_price, max_price)


@router.post("/orders", response_model=CreateOrderResponse)
async def addOrder(order: Order) -> CreateOrderResponse:
    return createOrder(order)
