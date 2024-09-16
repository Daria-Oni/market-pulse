# Market Pulse - 24 Hour Hackathon Project

**Market Pulse** is a web scraping and data clustering tool developed during a 24-hour hackathon. The project was designed to automatically extract, process, and analyze market-related web data and provide insights by clustering results based on predefined criteria.

## Features

- **Web Scraping**: Fetches URLs, extracts relevant data from web pages, and tracks the status of links.
- **Data Clustering**: Automatically groups data into clusters for easier analysis using Python-based clustering algorithms.
- **Data Visualization**: Generates plots for visual insights based on the scraped and clustered data.
- **Automation**: Automates the entire process from scraping to output generation in CSV format.

## Files

- `automaticclusters.py`: Handles automatic clustering of extracted data.
- `extraction.py`: Core module for data extraction and processing from web sources.
- `fetch_urls.py`: Fetches URLs to scrape from.
- `links_status.csv`: Stores the status of URLs during the scraping process.
- `output.csv`: Final output of the processed and clustered data.
- `plots.py`: Script for generating visual plots of the data.
- `scraping.py`: Main script for scraping the web pages.
- `test_scrape.py`: Test script for validating the scraping functionality.

## Project Goal

The goal of **Market Pulse** was to create a tool capable of gathering and analyzing market data efficiently from web pages on the big website, providing insights through clustering and visualizations, all within the time constraints of a 24-hour hackathon.
