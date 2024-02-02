from schemas.schema import ProductResponse, PageResponse, ListProductsResponse
from fastapi import HTTPException
from services.ProductService import listAllProducts


def listProducts(limit, offset, min_price, max_price) -> ListProductsResponse:
    try:
        result = listAllProducts(limit, offset, min_price, max_price)

        data = []
        pageData = None

        for product in result["data"]:
            data.append(ProductResponse(**product))
        for page in result["page"]:
            if page is not None:
                pageData = PageResponse(limit=limit, **page)

        return ListProductsResponse(data=data, page=pageData)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error occurred")

