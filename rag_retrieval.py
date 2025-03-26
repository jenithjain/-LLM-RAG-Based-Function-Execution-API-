import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import inspect
import importlib
import pickle
import os

class FunctionRetriever:
    def __init__(self, module_name="automation_functions", index_path="e:\\InterLLM\\automation_assistant\\function_index"):
        self.index_path = index_path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Load or create FAISS index
        if os.path.exists(f"{index_path}.faiss"):
            self.index = faiss.read_index(f"{index_path}.faiss")
            with open(f"{index_path}.pkl", 'rb') as f:
                self.functions = pickle.load(f)
            self.function_names = list(self.functions.keys())
        else:
            self._initialize_index(module_name)
    
    def _initialize_index(self, module_name):
        # Load the module containing automation functions
        self.module = importlib.import_module(module_name)
        
        # Extract functions and their docstrings
        self.functions = {}
        for name, func in inspect.getmembers(self.module, inspect.isfunction):
            if func.__doc__:
                self.functions[name] = func.__doc__.strip()
        
        # Create embeddings
        self.function_names = list(self.functions.keys())
        descriptions = list(self.functions.values())
        embeddings = self.model.encode(descriptions)
        
        # Initialize FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings).astype('float32'))
        
        # Save index and metadata
        faiss.write_index(self.index, f"{self.index_path}.faiss")
        with open(f"{self.index_path}.pkl", 'wb') as f:
            pickle.dump(self.functions, f)
    
    def retrieve_function(self, query, top_k=1):
        """Retrieve the best-matching functions using context-aware search."""
        try:
            # Debug print
            print(f"Available functions: {self.functions}")
            
            # Encode query
            query_embedding = self.model.encode([query])
            
            # Search in FAISS index
            distances, indices = self.index.search(
                np.array(query_embedding).astype('float32'), 
                top_k
            )
            
            # Return results
            results = []
            for idx in indices[0]:
                if idx < len(self.function_names):  # Add boundary check
                    results.append({
                        "function_name": self.function_names[idx],
                        "description": self.functions[self.function_names[idx]]
                    })
            
            return results
        except Exception as e:
            print(f"Error in retrieve_function: {e}")
            return []

    def update_index(self, new_function_name, description):
        """Add new function to the index."""
        embedding = self.model.encode([description])
        self.index.add(np.array(embedding).astype('float32'))
        self.functions[new_function_name] = description
        self.function_names.append(new_function_name)
        
        # Save updated index
        faiss.write_index(self.index, f"{self.index_path}.faiss")
        with open(f"{self.index_path}.pkl", 'wb') as f:
            pickle.dump(self.functions, f)