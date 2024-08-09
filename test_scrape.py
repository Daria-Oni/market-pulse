import json
from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "api_key": "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",
        "model": "gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="Find some information about what does the company do, the name and a contact email.",
    source="https://scrapegraphai.com/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))
