import requests
import logging

def get_data(video_id):
    # Σωστό URL με f-string και πλήρες πρωτόκολλο https
    url = f'www.channel8.gr{video_id}'
    
    # Προσθήκη Headers για αποφυγή μπλοκαρίσματος
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Έλεγχος αν η σελίδα απάντησε με επιτυχία (Status 200)
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                logging.error(f"Error: Το URL {url} δεν επέστρεψε έγκυρο JSON.")
                return None
        else:
            logging.error(f"HTTP Error {response.status_code} για το URL: {url}")
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"Σφάλμα σύνδεσης: {e}")
        return None

# Αν το script σου καλεί μια συνάρτηση main ή άλλη λογική, πρόσθεσέ τη από κάτω.
