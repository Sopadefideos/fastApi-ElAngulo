import fastapi as api
from .apis import users

router = api.APIRouter()
router.include_router(users.router)
