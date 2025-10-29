import json
from typing import Optional, Dict, Any

import requests


def display_weather_json(city: str, api_key: str, units: str = "metric", lang: str = "en") -> Optional[Dict[str, Any]]:
	"""
	Fetch and print the weather JSON for a given city using OpenWeatherMap API.

	Prints a nicely indented JSON representation of the API response.

	Args:
		city: City name (e.g. "London")
		api_key: OpenWeatherMap API key
		units: Units of measurement ("metric", "imperial" or "standard")
		lang: Language for the response (e.g. "en")

	Returns:
		The parsed JSON dict on success, or None on failure.
	"""
	if not city:
		print("Error: city must not be empty")
		return None
	if not api_key:
		print("Error: api_key must not be empty")
		return None

	url = "https://api.openweathermap.org/data/2.5/weather"
	params = {"q": city, "appid": api_key, "units": units, "lang": lang}

	try:
		resp = requests.get(url, params=params, timeout=10)
		resp.raise_for_status()
	except requests.exceptions.HTTPError as e:
		# Try to show a helpful message from the API if present
		try:
			err = resp.json()
			message = err.get("message") or err
		except Exception:
			message = str(e)
		print(f"HTTP error: {message}")
		return None
	except requests.exceptions.RequestException as e:
		print(f"Network error: {e}")
		return None

	try:
		data = resp.json()
	except json.JSONDecodeError:
		print("Error: Failed to decode JSON from response")
		return None

	# Pretty-print the JSON response
	print(json.dumps(data, indent=2, ensure_ascii=False))
	return data


if __name__ == "__main__":
	try:
		city = input("City name: ").strip()
		api_key = input("OpenWeatherMap API key: ").strip()
		display_weather_json(city, api_key)
	except KeyboardInterrupt:
		print("\nCancelled by user")
