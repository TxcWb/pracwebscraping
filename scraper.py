import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

def scrape_books(base_url):
    current_url = base_url
    all_books = []
    
    while current_url:
        print(f"Scraping {current_url}...")
        try:
            response = requests.get(current_url)
            response.raise_for_status()
            # The site doesn't specify charset in headers, but it is UTF-8
            response.encoding = 'utf-8'
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all product pods
        pods = soup.find_all('article', class_='product_pod')
        
        for pod in pods:
            # Title is in the 'a' tag inside 'h3'
            title = pod.h3.a['title']
            
            # Price is in a 'p' tag with class 'price_color'
            price = pod.find('p', class_='price_color').text
            
            # Availability is in a 'p' tag with class 'instock availability'
            availability = pod.find('p', class_='instock availability').text.strip()
            
            all_books.append({
                'title': title,
                'price': price,
                'availability': availability
            })
            
        # Look for the 'next' page link
        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = next_button.a['href']
            # Resolve relative URL
            current_url = urljoin(current_url, next_url)
            # Be polite to the server
            time.sleep(0.5)
        else:
            current_url = None
            
    return all_books

def save_to_csv(books, filename='books.csv'):
    if not books:
        print("No books to save.")
        return
        
    keys = books[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(books)
    print(f"Saved {len(books)} books to {filename}")

if __name__ == "__main__":
    start_url = "https://books.toscrape.com/index.html"
    book_list = scrape_books(start_url)
    if book_list:
        print(f"Total books found: {len(book_list)}")
        save_to_csv(book_list)
