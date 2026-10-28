import requests


def fetch_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]["data"][0]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["country"]  
        return user_name, user_country
    
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try :
        user_name, user_country = fetch_api()
        print(f"User Name: {user_name}")
        print(f"User Country: {user_country}")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()