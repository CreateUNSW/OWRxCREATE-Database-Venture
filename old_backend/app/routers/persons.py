from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/persons",
    tags=["persons"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["persons"])
async def read_persons():
    return []


@router.get("/me", tags=["persons"])
async def read_person_me():
    return {"zid": "my_zid"}


@router.get("/{zid}", tags=["persons"])
async def read_person(zid: str):
    return {"zid": zid}