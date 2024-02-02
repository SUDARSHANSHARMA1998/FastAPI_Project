from schemas.schema import CreateOrderResponse, Order
from fastapi import HTTPException
from services.OrderService import createOrderInstance


def createOrder(order: Order) -> CreateOrderResponse:
    try:
        result = createOrderInstance(order)
        response = CreateOrderResponse(orderId = str(result.inserted_id))

        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unexpected error occurred")