from fastapi  import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
  return [
    {
      "id": 1,
      "data": "Post 1"
    },
    {
      "id": 2,
      "data": "Post 2"
    },
  ]

