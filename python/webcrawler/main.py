import requests
import time
from bs4 import BeautifulSoup

start_ip = (192, 0, 0, 0)
end_ip = (193, 254, 254, 254)

for a in range(start_ip[0], end_ip[0] + 1):
    for b in range(start_ip[1], end_ip[1] + 1):
        for c in range(start_ip[2], end_ip[2] + 1):
            for d in range(start_ip[3], end_ip[3] + 1):
                ip_address = f"{a}.{b}.{c}.{d}"
                url = f"http://{ip_address}"
                try:
                    response = requests.get(url, verify=False, timeout=2)
                    if response.status_code == 200: 
                        soup = BeautifulSoup(response.text, 'html.parser')
                        title = soup.title.string.strip() if soup.title else 'Kein Titel gefunden'
                        headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
                        headings_text = [heading.get_text().strip() for heading in headings]
                        print(f"URL: {url}")
                        print(f"Titel: {title}")
                        print("Überschriften:")
                        for heading in headings_text:
                            print(heading)
                        print()


                    else:
                        response = requests.post(url, verify=False, timeout=2)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            title = soup.title.string.strip() if soup.title else 'Kein Titel gefunden'
                            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'a'])
                            headings_text = [heading.get_text().strip() for heading in headings]
                            print(f"URL: {url}")
                            print(f"Titel: {title}")
                            print("Überschriften:")
                            for heading in headings_text:
                                print(heading)
                            print()


                except requests.exceptions.RequestException as e:
                    print(f"URL {url} is not accessible.")
                    continue
                except requests.exceptions.Timeout as e:
                    print(f"Timeout occurred for URL {url}. Moving to the next IP.")
                    continue
                
            
