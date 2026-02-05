# Utilization only responsible for external JSON data fetchting
# Import libraries
from typing import List, Dict
import requests

# Fetch JSON with timeout and error raising
def fetch_json(url: str, timeout: int = 20) -> List[Dict]:
    """Fetch JSON payload from a HTTP endpoint."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data from {url}: {e}")
