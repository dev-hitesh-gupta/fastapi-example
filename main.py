from fastapi import FastAPI
from controllers import router
from iris_controller import  iris_router
app = FastAPI(debug=True)

app.include_router(router)
app.include_router(iris_router)