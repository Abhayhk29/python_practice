from fastapi import APIRouter

# router = APIRouter(
#     prefix="/auth",
#     tags=["auth"],
#     responses={404: {"message": "Not found"}}
# )

router = APIRouter()

@router.get('/auth')
async def get_auth():
    return {"message": "auth route"}