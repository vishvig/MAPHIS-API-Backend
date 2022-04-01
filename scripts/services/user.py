# Importing 3rd party API hosting and validation packages
from fastapi import APIRouter
from pydantic import ValidationError

# Importing general utilities for logging and validation
from scripts.logging.logger import get_logger
from scripts.schemas.responses import (
    DefaultResponse,
    DefaultFailureResponse,
)
from scripts.errors import MaphisException

# Importing API related requests/response validators
from scripts.schemas.user import (AddUserRequest, DeleteUserRequest, UpdateUserRequest, GetUserRequest)

# Importing API service handler class
from scripts.core.handlers.user import UserHandler


# Initializing necessary API, utils and handler classes
LOG = get_logger()
user_handler = UserHandler()
user_router = APIRouter(prefix='/user')


@user_router.post('/add', tags=["user"])
async def add_user(request_data: AddUserRequest):
    try:
        response_json = user_handler.add_user(request_data=request_data)
        return DefaultResponse(status="success",
                               message="User added successfully",
                               data=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except MaphisException as e:
        LOG.error(e)
        return DefaultFailureResponse(
            status="failed",
            message=e,
            error=e,
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )


@user_router.delete('/{userid}', tags=["user"])
async def delete_user(userid: str):
    try:
        response_json = user_handler.delete_user(userid)
        return DefaultResponse(status="success",
                               message="User deleted successfully",
                               data=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except MaphisException as e:
        LOG.error(e)
        return DefaultFailureResponse(
            status="failed",
            message=e,
            error=e,
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )


@user_router.post('/update', tags=["user"])
async def update_user(request_data: UpdateUserRequest):
    try:
        response_json = user_handler.update_user(request_data=request_data)
        return DefaultResponse(status="success",
                               message="User updated successfully!",
                               data=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except MaphisException as e:
        LOG.error(e)
        return DefaultFailureResponse(
            status="failed",
            message=e,
            error=e,
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )


@user_router.get('/{userid}', tags=["user"])
async def get_user(userid: str):
    try:
        response_json = user_handler.get_user(userid)
        return DefaultResponse(status="success",
                               message="User details fetched successfully!",
                               data=response_json)
    except ValidationError as e:
        LOG.error(f"Request data model validation failed: {e.json()}")
        return DefaultFailureResponse(
            status="failed",
            message="Request data model validation failed!",
            error=e.json(),
        )
    except MaphisException as e:
        LOG.error(e)
        return DefaultFailureResponse(
            status="failed",
            message=e,
            error=e,
        )
    except Exception as e:
        LOG.error(f"There was an issue when processing the request: {e}")
        return DefaultFailureResponse(
            status="failed",
            message="There was an issue when processing the request",
            error=e,
        )
