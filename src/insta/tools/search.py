import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader

load_dotenv(find_dotenv())

class SearchTools(object):
    @tool("search_internet")
    def search_internet(query:str)->str:
        """Use this tools to search the internet for information. 
        This tool return top 5 results from Google search engine."""
        
        return SearchTools.search(query)
    
    
    @tool("search_instagram")
    def search_instagram(query:str)->str:
        """Use this tools to search Instagram.
        This tool return top 5 results from Instagram pages."""
        
        return SearchTools.search(f"site:instagram.com{query}")
    
    
    @tool("open_page")
    def open_page(url:str)->str:
        """Use this tools to open a page.
        This tool return the page content.
        """
        
        documents=WebBaseLoader(url).load()
        filtered_documents=[]
        for document in documents:
            if document.metadata["source"] == url:
                filtered_documents.append(document.page_content)
        
        return "\n".join(filtered_documents)        
        
        
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
        for result in response :
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

        return f"Search results for '{query}':\n\n" + "\n".join(string)
