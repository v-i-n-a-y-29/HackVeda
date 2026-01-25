
import sys
import os

# Ensure backend is in path
sys.path.append(os.getcwd())

try:
    from rag.rag_engine import run_fisheries_agent
    print("✅ Import successful!")
    
    print("🔎 Testing RAG Query...")
    # This might fail if DB is not ready yet, but we will run it after DB generation
    response = run_fisheries_agent("What is the conservation status of Salmon?")
    print(f"📝 Response: {response[:100]}...") # Print first 100 chars
    
except ImportError as e:
    print(f"❌ Import Failed: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"❌ Execution Failed: {e}")
    import traceback
    traceback.print_exc()
