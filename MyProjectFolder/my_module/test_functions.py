from functions import *

def test_yes_or_no():
    assert bool(yes_or_no('Yes, I do want know the weather')) is True
    assert bool(yes_or_no('OK, I do want know the weather')) is True
    assert bool(yes_or_no('yea, I do want know the weather')) is True 
    assert bool(yes_or_no('No, I do not want to know the weather'))is False

    
def test_get_weather_data():
    city = 'boston'
    assert type(get_weather_data(city)) == tuple
    assert bool(get_weather_data(city)) is True

    
def test_get_more_info():
    city = 'boston'
    info = 'humidity'
    
    # Setting information we need for launching a search request
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    appid = '2c15c021fbcefcd864584aa09bf3404c'
    complete_url = base_url + 'q=' + city + '&appid=' + appid
    weather_data = requests.get(complete_url)
    weather_data = weather_data.json()
    assert get_more_info(weather_data, info) == print(weather_data['main']['humidity'])
    