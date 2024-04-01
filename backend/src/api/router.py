from fastapi import APIRouter

from src.api.routes import finetuning, health
from src.api.tags import Tags

API_V1_PREFIX = "/api/v1"

api_router = APIRouter(prefix=API_V1_PREFIX)
api_router.include_router(health.router, prefix="/health", tags=[Tags.HEALTH])
api_router.include_router(finetuning.router, prefix="/finetuning", tags=[Tags.FINETUNING])