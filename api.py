from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_retrieval import FunctionRetriever
from code_generator import generate_code

app = FastAPI(
    title="Automation Assistant API",
    description="API for executing automation functions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize retriever
retriever = FunctionRetriever()

class ExecuteRequest(BaseModel):
    query: str

class ExecuteResponse(BaseModel):
    function: str
    code: str

@app.get("/")
async def root():
    """Root endpoint that provides API information"""
    return {
        "message": "Automation Assistant API",
        "endpoints": {
            "/execute": "POST - Execute automation functions",
            "/docs": "GET - API documentation"
        }
    }

@app.post("/execute")
async def execute_endpoint(request: ExecuteRequest):
    try:
        print(f"Received query: {request.query}")
        
        matches = retriever.retrieve_function(request.query)
        print(f"Found matches: {matches}")
        
        if not matches:
            raise HTTPException(
                status_code=404,
                detail=f"No matching function found for query: {request.query}"
            )
        
        match = matches[0]
        function_name = match["function_name"]
        generated_code = generate_code(function_name)
        
        return ExecuteResponse(
            function=function_name,
            code=generated_code
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )