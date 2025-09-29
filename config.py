import os

# ----------------------------
# Configuration
# ----------------------------
MEMORY_FOLDER = "./CrewAI_Memory"
os.makedirs(MEMORY_FOLDER, exist_ok=True)

USER_MEMORY_FILE = f"{MEMORY_FOLDER}/user_agents_mem.json"
SEARCH_MEMORY_FILE = f"{MEMORY_FOLDER}/search_agents_mem.json"
AGG_MEMORY_FILE = f"{MEMORY_FOLDER}/aggregator_agent_mem.json"

MOCK_PRODUCTS_EXTRACTED = "products.json"
