from typing import Annotated, TypedDict
from tools.search import SearchTools
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
from langchain_groq.chat_models import ChatGroq
import operator


class GraphState(TypedDict):
    topic_of_the_week:str
    instagram_description:str
    messages: Annotated[list[AnyMessage], operator.add]
    
def reasoner(state:GraphState):
    tools=[SearchTools.search_instagram, SearchTools.search_internet, SearchTools.open_page]
    
    llm=ChatGroq(
        model="llama-3.2-3b-preview",
        temperature=0
    )
    
    messages=state["messages"]
    
    topic_of_the_week=state["topic_of_the_week"]
    instagram_description=state["instagram_description"]
    
    system_message=SystemMessage(content="""
    You are the Instagram Market Researcher.
    your goal is Analyze industry trends, competitor activities, and popular hashtags on Instagram. 
    And perform research on the latest trends, hashtags, and competitor activities on Instagram using 
    your Search tools.
    Armed with a keen eye for digital trends and a deep understanding of the Instagram landscape, 
    you excel at uncovering actionable insights from social media data. Your 
    analytical skills are unmatched, providing a solid foundation for strategic decisions 
    in content creation. You are great at identifying the latest trends and the 
    best hashtags for a given campaign.""")
    
    llm_with_tools=llm.bind_tools(tools)
    
    response = llm_with_tools.invoke(
        
    )
