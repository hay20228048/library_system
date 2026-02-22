from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.helper.exceptions import (AlreadyExistsError, BorrowError,
                                   NotFoundError)
from app.presentation.routes.book_routes import router as book_router
from app.presentation.routes.member_routes import router as member_router

app = FastAPI()


# rl_prefix="/books": Means every route in book_routes.py will start with:
app.include_router(book_router, prefix="/books")
app.include_router(member_router, prefix="/members")


# Global error handler for ValueError from Service Layer
# It works whenever Service Layer raises ValueError message


@app.exception_handler(ValueError)
async def handle_value_error(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"error": str(exc)})


@app.exception_handler(NotFoundError)
async def handle_not_found(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"error": str(exc)})


@app.exception_handler(AlreadyExistsError)
async def handle_exists(request: Request, exc: AlreadyExistsError):
    return JSONResponse(status_code=400, content={"error": str(exc)})


@app.exception_handler(BorrowError)
async def handle_borrow_error(request: Request, exc: BorrowError):
    return JSONResponse(status_code=400, content={"error": str(exc)})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # FastAPI uses 422 Unprocessable Entity by default for validation errors.
    return JSONResponse(status_code=422, content={"errors": exc.errors()})


# Global error handler that Catch ANY unexpected error,
# e.g: Database connection crash,Bug in code,Missing fields, .. the return code is 500 means Internal Server Error
@app.exception_handler(Exception)
async def handle_general_error(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
