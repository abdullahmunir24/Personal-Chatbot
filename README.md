# Personal-Chatbot

Introduction

Welcome to the AI Chatbot Personal Assistant project repository! This project aims to create a versatile AI chatbot using Python that can assist users with various tasks, including website and app opening, Instagram login, engaging in conversations, answering questions, and providing real-time weather and news updates through API integration.

Project Overview

The AI chatbot personal assistant is designed to be a versatile and helpful tool that can assist users in a variety of ways. It combines natural language processing (NLP) and API integration to provide a range of functionalities.

## Installation

To install the personal assistant, clone the repository and install the required dependencies:

```
git clone https://github.com/abdullah-almutairi/personal-assistant.git
cd personal-assistant
pip install -r requirements.txt
```

## Usage

To use the personal assistant, simply run the `main.py` file:

```
python main.py
```

The personal assistant will then start listening for your commands. You can give commands by speaking into the microphone or by typing them into the console.

## Features

The personal assistant has a variety of features, including:

* **Conversations: The chatbot can engage in text-based conversations with users, making it a friendly and interactive personal assistant. It utilizes the OpenAI API key for this purpose.
* **Open Applications: The personal assistant can open applications on your computer. For example, you can instruct it to "Open Notes" to access the Notes application.
* **Open Web Applications: The personal assistant can open websites on your computer. For instance, you can command it to "Open YouTube" to launch the YouTube application.
* **Search the Web: The personal assistant can search the web for information. For example, you can inquire, "What is the weather in San Francisco?" to obtain the weather forecast for San Francisco.
* **Get the Weather: The personal assistant can provide weather forecasts for any location. You can ask, "Tell me the weather for San Francisco?" to retrieve the weather information for San Francisco. Additionally, you can say, "Give me the weather forecast for Austin?" and it will prompt you to specify the number of days you'd like the forecast for. Once you provide the number of days, it will present you with the weather forecast for Austin. This feature relies on the weather API key.
* **Read the News: The personal assistant can read the news from various countries. For example, you can request, "Give me the latest news." Afterward, it will offer you the option to choose the number of headlines and the specific country for which you'd like to receive the news.
Answering Questions: The chatbot can answer general knowledge questions by harnessing its NLP capabilities. It utilizes the news API key for this purpose.
* **Instagram Login: It can automate the login process for Instagram, simplifying user access to their accounts.

## Code Explanation

The code for the personal assistant is divided into several files:

* `api.py`: This file contains the code for interacting with the OpenAI API.
* `apps.py`: This file contains the code for opening applications.
* `webapps.py`: This file contains the main code for opening web applications.
* `instagram.py`: This file contains the code for logging into Instagram.
* `main.py`: This file contains the main code for the personal assistant.
* `weather.py`: This file contains the main code for providing real-time weather updates.
* `news.py`: This file contains the main code for providing real-time news updates.



Contact

If you have any questions or need assistance with the project, feel free to reach out to me:

Abdullah Munir
GitHub: abdullahmunir24
Email: abdullahmunir2004@gmail.com

Thank you for your interest in my AI Chatbot Personal Assistant project! I hope you find it useful.
