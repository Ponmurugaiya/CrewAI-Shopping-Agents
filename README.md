# CrewAI multi-agent shopping search

CrewAI is a simple **multi-agent framework** built in Python.  
It simulates a **User Agent**, a **Search Agent**, and an **Aggregator Agent** that work together to search for products across multiple stores, filter results, and recommend the best options.

This project is modular, with support for persistent memory and async tasks.

---

## Project Structure

```

CrewAI/
├── crewai/                  # Core package
│   ├── **init**.py
│   ├── agents.py            # All agent definitions
│   ├── memory.py            # Persistent memory class
│   ├── tasks.py             # Async tasks for agents
│   ├── utils.py             # Helper functions
│   └── config.py            # Configuration
├── products.json            # Mock product database
├── main.py           # Entry point script
├── setup.py                 # Packaging configuration
├── README.md                # Project documentation
└── LICENSE                  # License file

````

---

## Features

- **User Agent** → interprets queries and extracts intent/entities  
- **Search Agent** → searches Amazon, Flipkart, and eBay (mocked with `products.json`)  
- **Aggregator Agent** → combines and filters results  
- **Persistent Memory** → remembers search history, filters, and results across turns  
- **Async Execution** → agents run concurrently for efficiency  

---

## Installation

Clone the repo and install in **editable mode**:

```bash
git clone https://github.com/Ponmurugaiya/CrewAI-Shopping-Agents.git
cd crewai
pip install -e .
````

---

## Usage

### Run the conversation demo

```bash
python main.py
```

or if installed with an entry point:

```bash
crewai
```

### Example Output

```
=== TURN 1: User Query: 'Running shoes' ===
[UserAgent] Intent: search, Entities: {}
[AggregatorAgent] Final Recommendations: ['Nike Running Shoe - $50', 'Puma Speed - $55', ...]

=== TURN 2: User Query: 'Show cheaper than $55' ===
[UserAgent] Intent: filter_price, Entities: {'max_price': 55}
[AggregatorAgent] Final Recommendations: ['Nike Running Shoe - $50', ...]

=== TURN 3: User Query: 'Only Amazon results' ===
[UserAgent] Intent: filter_store, Entities: {'store_name': 'Amazon'}
[AggregatorAgent] Final Recommendations: ['Adidas Runner - $40', ...]
```

---

## Development

* Python 3.8+
* No external dependencies beyond `crewai` (if you use the provided `Agent` stub)

To extend:

* Add new stores in `products.json`
* Modify `utils.py` to add new filters
* Enhance `agents.py` with new agent roles


