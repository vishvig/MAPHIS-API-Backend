import importlib
import uvicorn
from fastapi.staticfiles import StaticFiles
from brotli_asgi import BrotliMiddleware

from core import *
from utils import *
from utils.common_utils import *
from utils.logger_util import get_logger

from constants.configurations import Service

from exceptions import MaphisEndpointException


LOG = get_logger()

app = FastAPI(title="MAPHIS backend services",
              version="0.2",
              description="This is the API service layer for MAPHIS application")


@app.exception_handler(MaphisEndpointException)
async def exception_handler(request, _exec: MaphisEndpointException):
    LOG.error(f'{_exec.type}: {_exec.message}')
    return JSONResponse(status_code=_exec.status, content={"message": f'{_exec.type}: {_exec.message}'})


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["GET", "POST", "DELETE", "PUT"],
                   allow_headers=["*"])
app.add_middleware(BrotliMiddleware)

app.mount("/static", StaticFiles(directory="./assets/"), name="static")

for version in [i for i in os.listdir('core') if '__' not in i]:
    endpoint_modules = [i.rstrip('.py') for i in os.listdir(os.path.join('core', version, 'endpoints'))
                        if '__' not in i]
    for endpoint_module in endpoint_modules:
        module = importlib.import_module(f'core.{version}.endpoints.{endpoint_module}')
        try:
            app.include_router(module.router)
        except AttributeError as e:
            print(f'!------- Endpoint router object not found in core.{version}.endpoints.{endpoint_module} -------!')


if __name__ == '__main__':
    LOG.info(f'Starting MAPHIS API service layer on {Service.host}:{Service.port}')
    uvicorn.run(app, host=Service.host, port=int(Service.port))
