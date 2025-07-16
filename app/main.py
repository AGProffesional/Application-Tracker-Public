from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


from app.routes import router
from app.database import engine, Base
from app.extensions import limiter

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    yield
    print("Disposing database engine...")
    engine.dispose()


app = FastAPI(lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Adds security to prevent making direct calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(router)
