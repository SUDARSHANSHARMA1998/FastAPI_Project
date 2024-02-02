# FASTAPI BACKEND TASK

💫 Welcome! 🎉

This backend exercise involves creating a sample backend application in FastAPI, Python, and MongoDB for an ecommerce applicationn. The application needed to have the following APIs:

`GET /ecommerce/products`:
- Lists all available products in the system.
- Supports pagination with limit/offset query parameters.
- Filters products based on min_price and max_price query parameters.

**Sample Request URL**
```
http://127.0.0.1:8000/ecommerce/products?limit=1&min_price=100&max_price=900
```
**Sample Response Body**
```
{
  "data": [
    {
      "id": "65bcc84886932a1637810947",
      "name": "Smart Watch",
      "price": 129.99,
      "quantity": 22
    }
  ],
  "page": {
    "limit": 1,
    "nextOffset": 1,
    "prevOffset": null,
    "total": 9
  }
}
```

`GET /ecommerce/orders`: 
- Creates a new order with fields: createdOn, items, totalAmount, and userAddress.

**Sample request body**
```
{
  "items": [
    {
      "productId": "65bcc84886932a163781093a",
      "purchasedQuantity": 2
    }
  ],
  "userAddress": {
    "city": "Kanpur",
    "country": "India",
    "zipCode": "208002"
  }
}
```
**Sample response body**
```
{
  "orderId": "65bd2ac6ab1c29a60dcd68cf"
}
```

Note - For more information checkout FastAPI inbuilt documentation - 
```
http://127.0.0.1:8000/docs
```

## Schemas

> **All pydantic schemas are defined in schemas/schema.py**


### Collections
### Products Collection
Each product represents a collection within a MongoDB database to store information about products.
```
{
    "_id": ObjectId,   # MongoDB's default unique identifier for the document
    "name": str,       # Name of the product
    "price": float,    # Price of the product
    "quantity": int    # Available quantity of the product
}
```

### Orders Collection
It represents a collection within a MongoDB database to store information about customer orders.
```
{
    "_id": ObjectId,        # MongoDB's default unique identifier for the document
    "items": [
        {
            "productId": ObjectId,      # Reference to the product in the order
            "purchasedQuantity": int    # Quantity of the product purchased
        }
        # ... (Additional items can be included in the list)
    ],
    "totalAmount": float,               # Total amount of the order
    "userAddress": {
        "city": str,                    # City in the user's address
        "country": str,                 # Country in the user's address
        "zipCode": str                  # Zip code in the user's address
    }
}

```

## Getting Set Up
Ensure Python, FastAPI, uvicorn, pydantic, and pymongo packages are installed.

## Run server
Use this command to run the server
```
uvicorn main:app --reload
```
Note - Connection with the **MongoDB** would be taken care automatically once the server starts running

## Code Structure
- main.py runs the server using the uvicorn package.
- database.py manages the connection to MongoDB.
- schemas/schemas.py defines schemas for products and orders.
- routes.py maps routes to controller functions.
- The controller folder stores controller functions for each resource (e.g., order, product).
- The services folder contains helper functions for each controller.
