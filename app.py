import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

def check_api_keys():
    """ Check if necessary API keys are available in Streamlit secrets. """
    required_keys = ['OPENAI_API_KEY', 'OPENWEATHERMAPAPIKEY']
    missing_keys = [key for key in required_keys if key not in st.secrets]
    if missing_keys:
        st.error(f'Missing API keys in secrets configuration: {", ".join(missing_keys)}')
        st.stop()

def initialize_weather_agent():
    """ Initialize the weather agent with specified LLM and tools. """
    llm = OpenAI(temperature=0, api_key=st.secrets['OPENAI_API_KEY'])
    tools = load_tools(['openweathermap-api'], llm, api_key=st.secrets['OPENWEATHERMAPAPIKEY'])
    return initialize_agent(
        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

def run_weather_app(weather_agent):
    """ Run the Streamlit app for weather forecasting. """
    st.title('Weather Forecast')
    city = st.text_input('Enter a city name:', '')

    if st.button('Get Weather'):
        if city:
            query = f"What's the weather in {city} in the next 3 hours?"
            report = weather_agent.run(query)
            st.write(report)  
        else:
            st.error("Please enter a city name to check the weather.")

if __name__ == '__main__':
    check_api_keys()
    weather_agent = initialize_weather_agent()
    run_weather_app(weather_agent)
