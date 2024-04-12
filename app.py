import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# Initialize LLM and tools outside the Streamlit app function to avoid reinitializing on each interaction
llm = OpenAI(temperature=0, api_key=st.secrets["OPENAIAPIKEY"])  # Direct use of Streamlit secret for OpenAI key
tools = load_tools(["openweathermap-api"], llm, api_key=st.secrets["OPENWEATHERMAPAPIKEY"])  # Add API key directly to the tool if needed

weather_agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Streamlit app starts here
def run_weather_app():
    st.title('Weather Forecast')

    city = st.text_input('Enter a city name:', '')

    if st.button('Get Weather'):
        if city:
            query = f"What's the weather in {city} in the next 3 hours?"

            # Getting the weather report
            report = weather_agent.run(query)

            # Displaying the report in a paragraph format
            st.write(report)  
        else:
            st.error("Please enter a city name to check the weather.")

# This is the main app function call
if __name__ == '__main__':
    run_weather_app()
