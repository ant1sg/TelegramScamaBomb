import requests
import urllib.parse
import time
import random
import string
import argparse

# Get the bot id and chat id from the command line arguments
parser = argparse.ArgumentParser(description="Send fake login details to a Telegram bot.")
parser.add_argument("-b", "--bot_id", required=True, help="The bot ID for the Telegram bot.")
parser.add_argument("-c", "--chat_id", required=True, help="The chat ID to send messages to.")
args = parser.parse_args()


# Define the URL and parameters
bot_id = args.bot_id
chat_id = args.chat_id

url = f"https://api.telegram.org/bot{bot_id}/sendMessage"

def generate_fake_email():
    first_names = [
        "Marie", "Jean", "Pierre", "Nathalie", "Jacques", "Sophie", "Michel", "Isabelle",
        "François", "Catherine", "Henri", "Monique", "Philippe", "Claire", "Louis", "Christine",
        "Rene", "Laure", "Paul", "Lucie", "Marc", "Julie", "Bernard", "Sandrine", "Andre", 
        "Valerie", "Yves", "elise", "Alain", "Emilie", "Robert", "Helene", "Gerard", "Martine", 
        "Gilles", "Anne", "Serge", "Amandine", "Didier", "Colette", "Pascal", "Brigitte", 
        "Roger", "Nicolas", "Christian", "Aurelie", "Patrick", "Florence", "Luc", "Beatrice", 
        "Stephane", "Chantal", "Antoine", "Odile", "Laurent", "Veronique", "Julien", "Sylvie", 
        "Daniel", "Dominique", "Thierry", "Josiane", "Victor", "Annie", "Jean-Paul", "Cecile", 
        "Gerald", "Françoise", "Damien", "emilie", "Arnaud", "Solange", "Raymond", "Jeanne", 
        "Claude", "Suzanne", "Xavier", "Patricia", "Hugo", "Fanny", "Olivier", "Amelie", 
        "Jerôme", "Charlotte", "Georges", "Mireille", "Fabien", "Margaux", "Bertrand", "Elsa", 
        "Maurice", "Melanie", "Christian", "Pascale", "eric", "Caroline", "Gilbert", "Aline", 
        "Leon", "Therese"
    ]
    last_names = [
        "Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", 
        "Leroy", "Moreau", "Simon", "Laurent", "Lefebvre", "Michel", "Garcia", "David", 
        "Bertrand", "Roux", "Vincent", "Fournier", "Morel", "Girard", "Andre", "Lefevre", 
        "Mercier", "Dupont", "Lambert", "Bonnet", "Francois", "Martinez", "Legrand", 
        "Garnier", "Faure", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", "Roussel", 
        "Nicolas", "Perrin", "Morin", "Mathieu", "Clement", "Gauthier", "Dumont", "Lopez", 
        "Fontaine", "Chevalier", "Robin", "Masson", "Sanchez", "Gerard", "Nguyen", "Boyer", 
        "Denis", "Lemoine", "Meyer", "Renaud", "Jacob", "Barbier", "Guillaume", "Roger", 
        "Schmitt", "Colin", "Vidal", "Caron", "Picard", "Renard", "Huet", "Gonzalez", 
        "Gautier", "Adam", "Pires", "Marechal", "Bertin", "Leclerc", "Benoit", "Brunet", 
        "Gaillard", "Paris", "Leblanc", "Baron", "Marchand", "Aubert", "Poulain", "Girault", 
        "Charpentier", "Bailly", "Da Silva", "Rolland", "Lecomte", "Leger", "Marin", 
        "Duval", "Roy", "Gros", "Blanchard", "Philippe", "Dupond", "Rey", "Perrot"
    ]

    domains = ["gmail.com", "hotmail.com", "hotmail.fr", "orange.fr", "outlook.com"]

   
    random_first_name = random.choice(first_names).lower()
    random_last_name = random.choice(last_names).lower()
    random_domain = random.choice(domains)
    
    random_user = f"{random_first_name}.{random_last_name}"
    return f"{random_user}@{random_domain}"

def generate_fake_password():
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "111111",
        "123123", "abc123", "password1", "1234", "iloveyou", "1q2w3e4r", "admin", "letmein", 
        "welcome", "monkey", "123", "qwertyuiop", "princess", "654321", "superman", "asdfgh", 
        "qazwsx", "password123", "sunshine", "dragon", "football", "000000", "trustno1", 
        "123qwe", "lovely", "baseball", "master", "shadow", "michael", "666666", "123321", 
        "batman", "passw0rd", "starwars", "hello", "freedom", "whatever", "q1w2e3r4", 
        "letmein1", "zaq12wsx", "mypass", "123abc", "access", "secret", "charlie", "qwerty123", 
        "liverpool", "cheese", "princess1", "ranger", "william", "magnum", "london", "robert", 
        "qazxsw", "love", "password!", "pokemon", "pass123", "hannah", "ashley", "123654", 
        "loveme", "flower", "buster", "harley", "summer", "amanda", "biteme", "cookie", 
        "internet", "pepper", "carlos", "jordan", "ginger", "michelle", "hunter", "jessica", 
        "tigger", "1989", "maverick", "computer", "andrew", "merlin", "justin", "trust", 
        "bailey", "zxcvbnm", "buster", "thomas", "pepper", "dallas", "jennifer", "silver"
    ]
    
    length = random.randint(8, 24)
    if random.choice([True, False]):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 24)))
    else:
        return random.choice(common_passwords)
    
# Initialize the counter
counter = 0


while True:
    try:
        # Generate fake email and password
        fake_email = generate_fake_email()
        fake_password = generate_fake_password()
        
        # Create the message string
        message = f"Nouvelle connexion :\n📧 : {fake_email} \n 🔑 : {fake_password}"
        encoded_message = urllib.parse.quote(message)
        
        # Make the GET request
        response = requests.get(url, params={"chat_id": chat_id, "text": encoded_message})
        
        # Increment the counter
        counter += 1
        
        # Parse the JSON response
        response_json = response.json()
        ok_value = response_json.get("ok", "N/A")
        


        # Wait for a random amount of time between 60 and 300 seconds to emulate human behavior
        sleep_time = random.randint(60, 300)
        
        # Print the counter, status code, and the value of ok
        print(f"Count: {counter}, Status Code: {response.status_code}, OK: {ok_value}, Email: {fake_email}, Password: {fake_password}, Sleep Time: {sleep_time}")
        time.sleep(sleep_time)

        # Check if the response status code is 429
        if response.status_code == 429:
            print("Received status code 429, waiting for an extra 5 minutes...")
            time.sleep(300)

        
    except Exception as e:
        print(f"An error occurred: {e}")
    
