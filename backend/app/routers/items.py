from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/items",
    tags=["items"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_items():
    return []


@router.get("/{sku}")
async def read_item(sku: int):
    #if sku not in items_db:
    #    raise HTTPException(status_code=404, detail="Item not found")
    return {"sku": sku}


@router.put(
    "/{sku}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(sku: int):
    #if sku != "plumbus":
    #    raise HTTPException(
    #        status_code=403, detail="You can only update the item: plumbus"
    #    )
    return {"sku": sku}