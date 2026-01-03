import requests
import logging

def get_metadata(video_id):
    # Σωστό URL με f-string και χωρίς διπλά slashes
    url = f'www.channel8.gr{video_id}'
    
    # Προσθήκη User-Agent για να φαίνεται σαν κανονικός περιηγητής
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Έλεγχος αν η απάντηση είναι επιτυχής (HTTP 200)
        response.raise_for_status()
        
        # Έλεγχος αν το περιεχόμενο είναι όντως JSON
        return response.json()
        
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error: {e}")
    except requests.exceptions.JSONDecodeError:
        logging.error(f"Σφάλμα: Ο διακομιστής δεν επέστρεψε JSON. Απάντηση: {response.text[:100]}")
    except Exception as e:
        logging.error(f"Request error: {e}")
    
    return None

    else:
        video_id = sys.argv[1]
        get_channel8_streams(video_id)
