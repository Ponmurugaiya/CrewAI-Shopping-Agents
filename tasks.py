import asyncio
from memory import PersistentMemory
from config import USER_MEMORY_FILE, SEARCH_MEMORY_FILE, AGG_MEMORY_FILE
from utils import search_store, parse_intent_entities, aggregate_results

# ----------------------------
# Persistent Memories
# ----------------------------
user_memory = PersistentMemory(USER_MEMORY_FILE)
search_memory = PersistentMemory(SEARCH_MEMORY_FILE)
agg_memory = PersistentMemory(AGG_MEMORY_FILE)

# ----------------------------
# Agent Tasks
# ----------------------------
async def user_agent_task(query):
    history = user_memory.get("history", [])
    history.append(query)
    user_memory.set("history", history)

    intent, entities = parse_intent_entities(query)
    user_memory.set("last_intent", intent)
    user_memory.set("last_entities", entities)
    print(f"[UserAgent] Intent: {intent}, Entities: {entities}")
    return intent, entities

async def search_agent_task(query):
    async def search_amazon():
        results = search_memory.get("amazon")
        if not results:
            results = search_store("Amazon", query)
            search_memory.set("amazon", results)
        return results or []

    async def search_flipkart():
        results = search_memory.get("flipkart")
        if not results:
            results = search_store("Flipkart", query)
            search_memory.set("flipkart", results)
        return results or []

    async def search_ebay():
        total_len = len(search_memory.get("amazon", [])) + len(search_memory.get("flipkart", []))
        results = search_memory.get("ebay")
        if total_len < 4 and not results:
            results = search_store("eBay", query)
            search_memory.set("ebay", results)
        return results or []

    amazon_res, flipkart_res, ebay_res = await asyncio.gather(
        search_amazon(),
        search_flipkart(),
        search_ebay()
    )
    return amazon_res, flipkart_res, ebay_res

async def aggregator_agent_task(intent, entities, search_results):
    amazon_res, flipkart_res, ebay_res = search_results
    all_results = [amazon_res, flipkart_res, ebay_res]

    if intent == "filter_store" and "store_name" in entities:
        store = entities["store_name"]
        all_results = [search_memory.get(store.lower()) or []]

    memory_filter = {}
    if intent == "filter_price" and "max_price" in entities:
        memory_filter["max_price"] = entities["max_price"]

    final_results = aggregate_results(all_results, memory_filter)
    agg_memory.set("final", final_results)
    print("[AggregatorAgent] Final Recommendations:", final_results)
    return final_results

async def run_turn(query):
    intent_entities_task = asyncio.create_task(user_agent_task(query))
    search_task = asyncio.create_task(search_agent_task(query))

    intent, entities = await intent_entities_task
    search_results = await search_task

    await aggregator_agent_task(intent, entities, search_results)
