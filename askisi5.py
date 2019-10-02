import requests
from bs4 import BeautifulSoup
from collections import Counter

# print(response.status_code)

def returnPopChar():
    url = input("Παρακαλώ δώστε το url της ιστοσελίδας: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # diagrafo script k style
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    counts = Counter(text)

    print(counts)
    print(counts.most_common(1)[0][0].encode('raw_unicode_escape'))

    return counts.most_common(1)[0][0]


returnPopChar()