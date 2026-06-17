from rag.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()

count = pipeline.build_index()

print(
    f"Indexed {count} schema documents"
)

results = pipeline.retrieve(
    "customer orders"
)

print("\nRetrieved:\n")

for item in results:

    print(item)
    print("-" * 50)
