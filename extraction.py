from scrapegraphai.graphs import SmartScraperGraph
import nest_asyncio
import json

nest_asyncio.apply()  # Apply nest_asyncio to resolve any issues with asyncio event loop

# Configuration dictionary for the graph
graph_config = {
    "llm": {
        "model": "ollama/llama3",  # Specify the model for the llm
        "temperature": 0,  # Set temperature parameter for llm
        "format": "json",  # Specify the output format as JSON for Ollama
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specify the model for embeddings
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "verbose": True,  # Enable verbose mode for debugging purposes
}

# Function to fetch and extract content from a URL using SmartScraperGraph
def fetch_content(url):
    smart_scraper_graph = SmartScraperGraph(
        prompt="Extract the main content from the page.",
        source=url,
        config=graph_config
    )
    result = smart_scraper_graph.run()
    return result.get("main_content", "")

# Fetch content from all valid URLs
for url in valid_links:
    content = fetch_content(url)
    print(f"Content from {url}:\n{content}\n")

# Output all valid links for manual inspection
print("\nAll valid links with extracted content:")
for link in valid_links:
    print(link)
