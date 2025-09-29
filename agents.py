from crewai import Agent

# ----------------------------
# Create Agents
# ----------------------------
user_agent = Agent(
    name="UserAgent",
    role="user",
    goal="Provide search queries for running shoes and filter preferences.",
    backstory="You are a helpful user agent that provides search queries."
)

search_agent = Agent(
    name="SearchAgent",
    role="assistant",
    goal="Search Amazon, Flipkart, and eBay for products based on user queries.",
    backstory="You are a smart search agent that searches online stores."
)

aggregator_agent = Agent(
    name="AggregatorAgent",
    role="assistant",
    goal="Aggregate search results from multiple stores and apply filters based on user preferences.",
    backstory="You are an aggregator agent that combines and filters search results."
)
