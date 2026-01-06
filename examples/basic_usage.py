"""Basic usage examples for langchain-xbaza."""

from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain_xbaza import (
    XbazaJobsTool,
    XbazaUsersTool,
    XbazaBusinessTool,
    XbazaPropertyTool,
    XbazaServicesTool,
    XbazaAnalyticsTool,
)


def example_jobs_search():
    """Example: Search for jobs."""
    tool = XbazaJobsTool()
    result = tool.run(category="IT", city="Minsk", limit=5)
    print(result)


def example_users_search():
    """Example: Search for professionals."""
    tool = XbazaUsersTool()
    result = tool.run(query="React developer", limit=5)
    print(result)


def example_agent_usage():
    """Example: Using tools with LangChain agent."""
    # Initialize tools
    tools = [
        XbazaJobsTool(),
        XbazaUsersTool(),
        XbazaBusinessTool(),
    ]
    
    # Create agent (requires OpenAI API key)
    # llm = OpenAI(temperature=0)
    # agent = initialize_agent(
    #     tools,
    #     llm,
    #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True
    # )
    
    # Use agent
    # result = agent.run("Find me IT jobs in Minsk with salary above 2000 BYN")
    # print(result)
    
    print("Agent example requires OpenAI API key. Uncomment code to use.")


def example_all_tools():
    """Example: Using all available tools."""
    tools = [
        XbazaJobsTool(),
        XbazaUsersTool(),
        XbazaBusinessTool(),
        XbazaPropertyTool(),
        XbazaServicesTool(),
        XbazaAnalyticsTool(),
    ]
    
    print("Available tools:")
    for tool in tools:
        print(f"  - {tool.name}: {tool.description[:50]}...")


if __name__ == "__main__":
    print("=== Basic Usage Examples ===\n")
    
    print("1. Jobs Search:")
    example_jobs_search()
    print("\n" + "="*50 + "\n")
    
    print("2. Users Search:")
    example_users_search()
    print("\n" + "="*50 + "\n")
    
    print("3. All Tools:")
    example_all_tools()
    print("\n" + "="*50 + "\n")
    
    print("4. Agent Usage:")
    example_agent_usage()

