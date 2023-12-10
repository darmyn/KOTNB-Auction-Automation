from bs4 import BeautifulSoup

def get_total_listings(page_content):
    try:
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find the div with class 'listings-header-count'
        listings_div = soup.find('div', class_='listings-header-count')

        # Check if the div is found
        if listings_div:
            # Extract the text content from the span tag
            listings_text = listings_div.span.text

            # Extract the number from the text (assuming the number is always at the beginning of the text)
            number_of_listings = int(listings_text.split()[0])

            print(f"Number of listings: {number_of_listings}")
        else:
            print("Error: 'listings-header-count' div not found")

    except Exception as e:
        print(f"An error occurred: {e}")
    
def get_product_details(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
def get_num_pages(page_content):
    soup = BeautifulSoup(page_content, "html.parser")