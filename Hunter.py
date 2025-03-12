import requests

API_KEY = '28f7a9ba8fb4a030d901e289073569e5fed49f47' # i don't care take it if u want
BASE_URL = 'https://api.hunter.io/v2/'

def get_email_verification(email):
    url = f"{BASE_URL}email-verifier?email={email}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_domain_search(domain):
    url = f"{BASE_URL}domain-search?domain={domain}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_email_finder(domain, first_name, last_name):
    url = f"{BASE_URL}email-finder?domain={domain}&first_name={first_name}&last_name={last_name}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_company_enrichment(domain):
    url = f"{BASE_URL}companies/find?domain={domain}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_person_enrichment(email):
    url = f"{BASE_URL}people/find?email={email}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_combined_enrichment(email):
    url = f"{BASE_URL}combined/find?email={email}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

def main_menu():
    while True:
        print("\nHunter API Menu")
        print("1. Verify email")
        print("2. Domain search")
        print("3. Find email")
        print("4. Company enrichment")
        print("5. Person enrichment")
        print("6. Combined enrichment")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            email = input("Enter email to verify: ")
            result = get_email_verification(email)
            print(result)
        elif choice == '2':
            domain = input("Enter domain to search: ")
            result = get_domain_search(domain)
            print(result)
        elif choice == '3':
            domain = input("Enter domain: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = get_email_finder(domain, first_name, last_name)
            print(result)
        elif choice == '4':
            domain = input("Enter domain for enrichment: ")
            result = get_company_enrichment(domain)
            print(result)
        elif choice == '5':
            email = input("Enter email for enrichment: ")
            result = get_person_enrichment(email)
            print(result)
        elif choice == '6':
            email = input("Enter email for combined enrichment: ")
            result = get_combined_enrichment(email)
            print(result)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
