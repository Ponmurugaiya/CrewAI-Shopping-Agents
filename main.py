import asyncio
from tasks import run_turn

# ----------------------------
# Simulated Conversation
# ----------------------------
simulated_queries = [
    "Running shoes",
    "Show cheaper than $55",
    "Only Amazon results"
]

async def run_conversation():
    for turn, query in enumerate(simulated_queries, 1):
        print(f"\n=== TURN {turn}: User Query: '{query}' ===")
        await run_turn(query)

if __name__ == "__main__":
    asyncio.run(run_conversation())
