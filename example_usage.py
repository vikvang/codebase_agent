# Initialize the system
rag = EnhancedCodeRAG()

# Index your codebase
rag.index_codebase("/path/to/your/codebase")

# Perform a search
results = rag.search("How does the authentication system work?") 