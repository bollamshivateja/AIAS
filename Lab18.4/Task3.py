import requests
from typing import Optional, Dict, Any

def get_formatted_weather(city: str, api_key: str, units: str = "metric", lang: str = "en") -> Optional[str]:
    """
    Fetch weather data and return it in a formatted, user-friendly string.
    
    Args:
        city (str): Name of the city to get weather for
        api_key (str): OpenWeatherMap API key
        units (str, optional): Units of measurement. Defaults to "metric"
        lang (str, optional): Language for the response. Defaults to "en"
    
    Returns:
        Optional[str]: Formatted weather information if successful, None if failed
    """
    if not city or not api_key:
        print("Error: City name and API key are required.")
        return None

    try:
        # Make API request
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": units, "lang": lang}
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        # Parse the response
        data = response.json()
        
        # Extract specific fields
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        # Format the output
        weather_info = f"""
• City: {city.title()}
• Temperature: {temperature:.1f}°{'C' if units == 'metric' else 'F'}
• Humidity: {humidity}%
• Weather: {description.capitalize()}"""
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError as e:
        print(f"Error: Missing data in API response - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

def main():
    try:
        # Get user input
        city = input("City name: ").strip()
        if not city:
            raise ValueError("City name cannot be empty")
            
        api_key = input("OpenWeatherMap API key: ").strip()
        if not api_key:
            raise ValueError("API key cannot be empty")
        
        # Get and display weather information
        weather_info = get_formatted_weather(city, api_key)
        if weather_info:
            print(weather_info)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
