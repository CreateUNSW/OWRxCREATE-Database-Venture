from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/locations",
    tags=["locations"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["locations"])
async def read_locations():
    return []

@router.get("/{location_id}", tags=["locations"])
async def read_location(location_id: int):
    return {}