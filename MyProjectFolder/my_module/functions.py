"""

This module includes functions that required to use in ProjectNotebook. The ProjectNotebook function as a chatbot that was designed to provide current weather data for over 200,000 cities based on the OpenWeather API. The function yes_or_no is employed to detect yes or no in user inputs. The function get_weather_data is employed to request weather data from OpenWeather API. The function get_more_info functions to provide more information of weather to user. 

"""

# Importing required modules
# Making it available for functions to use later
import string
import random 
import json
import requests
import numpy as np


# A function used to detcet yes or no in user inputs
def yes_or_no(user_response):
    """Detect yes or no in user inputs. 
       
    Parameters
    -------
    user_response: string
        The input of user response in data to summarize

    Returns
    -------
    bool
        True if yes, False otherwise. 

    References
    -------
    ..[1] significantly update code, but reference to course assignment A3 and A4
   
    """
    # Because we need covert user inputs into lowercases
    # We use lower() method to approach
    user_response = user_response.lower()
    
    # Because of removing all punctuations in user inputs
    # We use replace method to remove all punctuation in the string
    for punc in string.punctuation:
        user_response = user_response.replace(punc, '')
        
    # Because of to split up the characters of the string
    # We use split()method, and store result in response 
    response = user_response.split()
    
    # To detect specific words in response, we use a for loop
    for words in response:
        
        # To check if input includes word 'yes'
        if words == 'yes':
            return True
        
        # To check if input includes word 'ok'
        if words == 'ok':
            return True 
        
        # To check if input includes word 'yea'
        if words == 'yea':
            return True
        
    # If user input do not includes above three possible synonyms for yes
    return False 


# A function used to request weather data from OpenWeather API
def get_weather_data(city):
    """Requesting weather data from OpenWeather API.
      
    Parameters
    -------
    city: string
        The input of city name in data to summarize and search in API

    Returns
    -------
    weather_data: tuple
        The returned weather data from API in python format  
   
    Bool: 
        True if pass try, False goes into except
        
    References
    -------
    ..[1] OpenWeather API website(https://openweathermap.org/current_)
      [2] learn from the website to covert json data to python data
          (https://realpython.com/python-json/)
             
    """
    # Run the following code
    try:
        # Obtaining base-url from OpenWeather API
        # Where we get weather data from this web address
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    
        # Generating my unique API keys from OpenWeather
        appid = '2c15c021fbcefcd864584aa09bf3404c'
    
        # Setting information we need for launching a search request
        # store in complete_url
        complete_url = base_url + 'q=' + city + '&appid=' + appid 
    
        # Using get() method in requests module to get data
        # Store in weather_data
        weather_data = requests.get(complete_url)
    
        # Because the avaliable weather data is in json formation
        # We covert it into python format data and store in weather_data 
        weather_data = weather_data.json()
        
        # Print following value if user wants to know the weather
        print(weather_data['weather'][0]['main'])
        
        # Need a value to check if it passes try
        return weather_data, True 
    
    # Run the following code when there is an exception
    # If the specific weather data is not avalible in the API
    except:
        string1 = '\nSorry! Your search did not match any weather data in our database.'
        string2 = 'Hope I can help you next time.'
        print(string1+string2)
        
        return weather_data, False

    
# A function used to detect user inputs 
# Print more information of weather data from OpenWeather API
def get_more_info(weather_data, info):
    """Detecting user inputs and printing more weather data from OpenWeather API. 
      
    Parameters
    -------
    weather_data: tuple
        The returned weather data from API in python format 
    
    infor: string
        The input of user in data to summarize and search in API

    Returns
    -------
    None 
    """   
    # Check if user input is humidity
    # Then print information from API
    if info == 'humidity':
        print(weather_data['main']['humidity'])   
        
    # Check user input is temperature and then print information  
    # Then print information from API
    if info == 'temperature':
        print(weather_data['main']['temp'])
        
    # Check user input pressure and then print information 
    # Then print information from API
    if info == 'pressure':
        print(weather_data['main']['pressure']) 
    
    # Check user input visibility and then print information
    # Then print information from API
    if info == 'visibility':
        print(weather_data['weather']['visibility'])