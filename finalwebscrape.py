


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use WebDriver Manager to handle ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

product_name = []
price = []
review = []
rating = []


for i in range(1, 11): 
    url = f"https://www.flipkart.com/beauty-and-grooming/body-face-skin-care/body-and-face-care/pr?sid=g9b%2Cema%2C5la&otracker=categorytree&page={i}"
    print(f"Scraping page {i}: {url}")
    
    driver.get(url)
    time.sleep(2) 

    # Find all product containers
    product_containers = driver.find_elements(By.CLASS_NAME, "cPHDOP")

    for container in product_containers:
        products = container.find_elements(By.CLASS_NAME, "slAVV4")

        for product in products:
            try:
                # Extract product name
                name = product.find_element(By.CLASS_NAME, "wjcEIp")
                new_name=name.text.split(",")[0].split("|")[0]
            except:
                new_name = "N/A"
            product_name.append(new_name)

            try:
                # Extract price
                price_value = product.find_element(By.CLASS_NAME, "Nx9bqj").text.strip()
                new_price_value = int(price_value.replace('₹', '').replace(',', ''))
            except:
                price_value = "N/A"
            price.append(new_price_value)

            try:
                # Extract review count
                review_value = product.find_element(By.CLASS_NAME, "XQDdHH").text.strip()
            except:
                review_value = "0"
            review.append(review_value)

            try:
                # Extract rating
                rating_value = product.find_element(By.CLASS_NAME, "Wphh3N").text.strip()
                new_rating_value = rating_value.replace('(', '').replace(')', '').replace(',', '')
            except:
                rating_value = "Not Rated"
            rating.append(new_rating_value)
print(product_name)
print(len(product_name))
print(price)
print(len(price))

print(rating)
print(len(rating))


print(review)
print(len(review))


# Close the driver
driver.quit()


data = {
    "Product Name": product_name,
    "Price": price,
    "Review Count": review,
    "Rating": rating
}

df = pd.DataFrame(data)
df.to_csv("flipkart_products_new.csv", index=False)

print("Data saved to flipkart_products_new.csv")
