from schemas.schema import Order
from database import products_collection, orders_collection
from bson import ObjectId
from datetime import datetime


def createOrderInstance(order: Order):
    totalAmount = 0

    for item in order.items:
        itemId = ObjectId(item.productId)
        product = products_collection.find_one({"_id": itemId})

        if product["quantity"] < item.purchasedQuantity:
            raise ValueError(f"Insufficient quantity for product with id {item.productId}")

        products_collection.update_one(
            {"_id": itemId},
            {"$inc": {"quantity": -item.purchasedQuantity}}
        )

        totalAmount = totalAmount + product["price"] * item.purchasedQuantity

    # Create order document
    items = [item.dict() for item in order.items]
    order_data = {
        "items": items,
        "totalAmount": totalAmount,
        "userAddress": {
            "city": order.userAddress.city,
            "country": order.userAddress.country,
            "zipCode": order.userAddress.zipCode
        },
        "createdOn": datetime.utcnow()
    }

    # Insert order into MongoDB
    result = orders_collection.insert_one(order_data)

    return result
