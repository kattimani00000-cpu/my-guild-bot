import requests
import time

# నీ వివరాలు
guild_id = "3021295212"
password = "నీ_గెస్ట్_పాస్‌వర్డ్" # ఇక్కడ నీ 8 అంకెల పాస్‌వర్డ్ పెట్టు

def add_glory():
    # ఇది గిల్డ్ గ్లోరీ పెంచడానికి రిక్వెస్ట్ పంపుతుంది
    url = f"https://freefire-api.com/glory?id={guild_id}&pass={password}"
    try:
        response = requests.get(url)
        print("Glory Point Added! ✅")
    except:
        print("Error! ❌")

while True:
    add_glory()
    time.sleep(10) # ప్రతి 10 సెకన్లకు ఒక రిక్వెస్ట్
  
