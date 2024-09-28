import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import base64

def save_image(image_url, file_path):
    if image_url.startswith('data:image/'):
        img_data = base64.b64decode(image_url.split(',', 1)[1])
    else:
        img_data = requests.get(image_url).content
    # Overwrite the file if it exists
    with open(file_path, 'wb') as f:
        f.write(img_data)
    print(f'Saved {os.path.basename(file_path)}')

def scrapeImages(search_terms):
    folder = os.path.join('Model/Gemini', 'images')
    os.makedirs(folder, exist_ok=True)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    for index, term in enumerate(search_terms, start=1):
        url = f'https://www.google.com/search?q={quote(term)}&udm=2'
        try:
            soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
            img_elements = soup.find_all('img', class_='YQ4gaf')  # Look for images with class 'YQ4gaf'
            if img_elements:
                img_urls = [img['src'] for img in img_elements if img.get('src')]
                if img_urls:
                    save_image(img_urls[0], os.path.join(folder, f'{index}.jpg'))
                else:
                    print(f'No valid image URLs found for {term}')
            else:
                print(f'No images found with class YQ4gaf for {term}')
        except Exception as e:
            print(f'Failed to fetch images for {term}: {e}')

