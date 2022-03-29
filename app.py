import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.logging.logger import get_logger
from scripts.constants.configurations import Service


from scripts.services.sample import sample_router
from scripts.services.user import user_router

LOG = get_logger()

app = FastAPI(title="MAPHIS backend services",
              version="0.1",
              description="This is the API service layer for MAPHIS application")
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["GET", "POST", "DELETE", "PUT"],
                   allow_headers=["*"])

app.include_router(sample_router)
app.include_router(user_router)

service_obj = Service()


if __name__ == '__main__':
    LOG.info(f'Starting MAPHIS API service layer on {service_obj.host}:{service_obj.port}')
    uvicorn.run(app, host=service_obj.host, port=int(service_obj.port))
