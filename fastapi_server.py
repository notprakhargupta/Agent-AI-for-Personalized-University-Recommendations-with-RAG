
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_agent import rag_pipeline

app = FastAPI()

# Request model
class Query(BaseModel):
    query: str

# Endpoint for university recommendations
@app.post("/recommendations/")
async def get_recommendations(query: Query):
    try:
        response = rag_pipeline(query.query)
        return {"recommendations": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
