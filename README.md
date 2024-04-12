# weather-forecasting-app-streamlit-langchain-gpt

This repository contains a simple weather forecasting application built with Streamlit, LangChain, and GPT models from OpenAI. It uses real-time weather data fetched using the OpenWeatherMap API and generates human-like responses to weather queries for any specified city.

## Features
- Fetch and display weather data for any city.
- Uses OpenAI's powerful language models for natural language processing.
- Built with Streamlit for an interactive user interface.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.6 or later.
- API keys for OpenAI and OpenWeatherMap.

## Installation
Clone the repository

```
git clone https://github.com/yourusername/weather-forecasting-app-streamlit-langchain-gpt.git
```
```
cd weather-forecasting-app-streamlit-langchain-gpt
```

## Install dependencies
Install the required Python libraries using pip:

```
pip install -r requirements.txt
```
## Configuration
- Set up API Keys
- You need to set up your API keys for OpenAI and OpenWeatherMap in your Streamlit secrets. The secrets.toml file should not be pushed to your repository for security reasons. Add the following content to your secrets.toml file in your local Streamlit configuration or through the Streamlit sharing interface if deployed:

```
# secrets.toml
OPENAIAPIKEY = "your-openai-api-key"
OPENWEATHERMAPAPIKEY = "your-openweathermap-api-key"
```
Modify ```requirements.txt``` if Necessary

Make sure requirements.txt contains the following lines:

```
streamlit
langchain
openai
requests
```

Running the Application
To run the application locally, execute the following command in the terminal:

```
streamlit run weather-forecasting-app-streamlit-langchain-gpt.py
```

The Streamlit interface will open in your default web browser, where you can interact with the application.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your features or fixes.
