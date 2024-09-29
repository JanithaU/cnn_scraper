import requests
from bs4 import BeautifulSoup
# Function to scrape CNN homepage and extract article titles
def scrape_cnn():
    url = "https://www.cnn.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    # Send request to CNN homepage
    response = requests.get(url, headers=headers)
    
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")
    
    # Find all articles (modify based on CNN’s structure)
    articles = soup.find_all('h3', class_="cd__headline")  # Headline class might differ

    # Open a file to write the extracted headlines
    with open("cnn_headlines.txt", "w") as file:
        for article in articles:
            headline = article.get_text(strip=True)
            file.write(headline + "\n")

    print("Headlines saved to cnn_headlines.txt")

# Run the function
scrape_cnn()
