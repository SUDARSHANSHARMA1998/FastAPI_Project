from database import products_collection


def listAllProducts(limit, offset, min_price, max_price):
    dbQuery = {}
    if min_price is not None:
        dbQuery["price_min"] = {"$gte": min_price}
    if max_price is not None:
        dbQuery["price_max"] = {"$lte": max_price}

    # Define the aggregation pipeline
    pipeline = [
        {"$match": {
            "$and": [
                {"price": {"$gte": min_price}} if min_price is not None else {},
                {"price": {"$lte": max_price}} if max_price is not None else {}
            ]
        }},
        {"$facet": {
            "data": [
                {"$skip": offset},
                {"$limit": limit},
                {"$project": {
                    "id": {"$toString": "$_id"},
                    "name": 1,
                    "price": 1,
                    "quantity": 1,
                    "_id": 0
                }}
            ],
            "page": [
                {"$group": {
                    "_id": None,
                    "total": {"$sum": 1},
                    "minPrice": {"$min": "$price"},
                    "maxPrice": {"$max": "$price"}
                }},
                {"$project": {
                    "limit": limit,
                    "nextOffset": {"$cond": [{"$gt": ["$total", offset + limit]}, offset + limit, None]},
                    "prevOffset": {"$cond": [{"$gt": [offset, 0]}, offset - limit, None]},
                    "total": "$total",
                    "minPrice": "$minPrice",
                    "maxPrice": "$maxPrice",
                    "_id": 0
                }}
            ]
        }}
    ]

    result = list(products_collection.aggregate(pipeline))[0]

    return result

