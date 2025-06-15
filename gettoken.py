def gettoken():
    import json
    import requests
    BearerToken = ""

    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m" 

    with open('/data/options.json') as options_file:
       json_settings = json.load(options_file)
    # API URL
    url = f'https://{json_settings['API_Server']}/oauth/token'
    # Prepare request payload
    payload = {
        "areaCode": "solark",
        "client_id": "csp-web",
        "grant_type": "password",
        "password": json_settings['solark_pass'],
        "source": "solark",
        "username": json_settings['solark_user']
    }
    # Headers
    headers = {"Content-Type": "application/json"}    
    try:
        # Send POST request with timeout (10s)
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        # Parse response
        parsed_login_json = response.json()

        # Check login status
        if parsed_login_json.get('msg') == "Success":
            print("SolArk Login: " + ConsoleColor.OKGREEN + parsed_login_json['msg'] + ConsoleColor.ENDC)
            BearerToken = parsed_login_json['data']['access_token']
            return BearerToken
        else:
            print("SolArk Login: " + ConsoleColor.FAIL + parsed_login_json['msg'] + ConsoleColor.ENDC)
            return BearerToken

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to SolArk API." + ConsoleColor.ENDC)
        return BearerToken

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to SolArk API. {e}" + ConsoleColor.ENDC)
        return BearerToken

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse SolArk API response." + ConsoleColor.ENDC)
        return BearerToken
