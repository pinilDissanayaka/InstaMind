import os
import requests
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class SearchTools(object):
    def search(query:str, limit=5):
        url="https://google.serper.dev/search"
        payload = json.dumps({
        "q": query,
        "num": limit
        })
        
        headers = {
        'X-API-KEY': os.getenv("X-API-KEY"),
        'Content-Type': 'application/json'
        }
        
        
        response = requests.request("POST", url, headers=headers, data=payload).json()["organic"]
        
        string = []
        for result in response:
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

        return f"Search results for '{query}':\n\n" + "\n".join(string)