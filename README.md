# Web-Scraping-project
Flipkart Product Scraper using Selenium

This project is a web scraper built with Python and Selenium to extract product information (names, prices, reviews, and ratings) from the Beauty and Grooming section on Flipkart. The scraped data is saved in a CSV file for further analysis.

Features
Extracts product name, price, review count, and rating from multiple pages.
Handles pagination to scrape products from multiple pages (default: 10 pages).
Error handling ensures that missing data or invalid containers do not crash the scraper.
Headless browser mode improves performance by running the scraper without opening a browser window.
Saves the scraped data into a CSV file (flipkart_products_new.csv).
Technologies Used
Python 3.8+
Selenium for web scraping
webdriver-manager to manage ChromeDriver
Pandas for data handling

