import uvicorn
from fastapi import FastAPI
from irismodel import IrisMachineLearning
from irismodel import IrisSpecies
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = IrisMachineLearning()

@app.get("/")
async def root():
    return {"message": "Hello This is iris classfier"}

@app.get("/predict")
async def predict():
    pred, prob = model.predict_species(8,1,8,1)
    return {"predict" : pred,
            "probability" : prob}

@app.post("/predict")
async def predict(iris:IrisSpecies):
    pred, prob = model.predict_species(iris.sepal_length, iris.sepal_width,
                                       iris.petal_length, iris.petal_width)
    return {"predict" : pred,
            "probability" : prob}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)