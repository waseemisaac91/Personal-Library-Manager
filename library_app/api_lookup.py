"""
api_lookup.py
Waseem
"""

import requests 

def lookup_book(title):
url = "https://openlibrary.org/search.json"
    params = {"title": title, "limit": 1}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        print("⚠️  Lookup timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("⚠️  No internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Lookup failed: {e}")
        return None
    except ValueError:
        print("⚠️  Invalid response from server.")
        return None
    docs = data.get("docs", [])
    if not docs:
        return None
    first = docs[0]
    authors = first.get("author_name", [])
    author = authors[0] if authors else "Unknown"
    years = first.get("first_publish_year")
    return {"author": author, "year": years if isinstance(years, int) else None}
     
