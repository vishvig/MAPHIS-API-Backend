# Importing 3rd party API hosting and validation packages
from fastapi import APIRouter
from pydantic import ValidationError

# Importing general utilities for logging and validation
from scripts.logging.logger import get_logger
from scripts.schemas.responses import (
    DefaultResponse,
    DefaultFailureResponse,
)

# Importing API related requests/response validators
from scripts.schemas.sample import (
    ReturnTextRequest,
    TwoNumberCalculatorRequest
)

# Importing API service handler class
from scripts.core.handlers.sample import SampleHandler


# Initializing necessary API, utils and handler classes
LOG = get_logger()
dashboard_handler = SampleHandler()
sample_router = APIRouter(prefix='/sample')


@sample_router.get('/alphav1/hello-world', tags=["sample"])
async def hello_world():
    try:
        response_json = dashboard_handler.hello_world()
        return DefaultResponse(status="success", message=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )


@sample_router.post('/alphav1/return-text', tags=["sample"])
async def return_text(request_data: ReturnTextRequest):
    try:
        response_json = dashboard_handler.return_text(request_data=request_data)
        return DefaultResponse(status="success", message=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )


@sample_router.post('/alphav1/calculator', tags=["sample"])
async def return_text(request_data: TwoNumberCalculatorRequest):
    try:
        response_json = dashboard_handler.two_number_calc(request_data=request_data)
        return DefaultResponse(status="success", message="Calculated successfully", data=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )
