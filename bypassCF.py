import requests
import random
import string
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_random_email():
    """Generate a random email address"""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "protonmail.com"]
    username_length = random.randint(6, 12)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_password():
    """Generate a random password"""
    password_length = random.randint(8, 14)
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))

# Cloudflare bypass with cookies
cookies = {
    'PHPSESSID': '1b4054b4f6f9c361522256ce41dd0ecc',
    'dom3ic8zudi28v8lr6fgphwffqoz0j6c': '27fdb812-e97f-4fb0-8bfb-aefb343c5441%3A2%3A1',
    'pp_main_a800eb180e5f4a3e152d2bd730a3f449': '1',
    'sb_main_483eb9ed75939f83526152aec230c76c': '1',
    'sb_count_483eb9ed75939f83526152aec230c76c': '3',
    'pp_sub_a800eb180e5f4a3e152d2bd730a3f449': '2',
    'cf_clearance': 'cobY.PYcTcyMldpEztMHhh3GYE.VBr78EGXbt0pb.eA-1743838458-1.2.1.1-j9xUMhsvr288wA9_nkhhVMnMQwoEAVhthyAXXb81ZNk.ckrldLCtEa7QG7qvhPnWoLHBmRBRzIf6.wTwDd9.GxN8AyVWRKSJ9VA9yP9Qq6.Z_iFDmf1tPVWNOUZQfDoEGZKzIt1MBA7QwRD2nFar2csFw7ijRfoK_M1dHte1Mpl7OMGAW81XeslExzTXsAc7Zhi5TQ0pSAS_I8KG5CjMdTlmuyjy0NWtfNRw8.A0PtVxhXO2ZXuLeKdjLvLsFK9.8l4GQpSdGn6oO5XgPwO8ijcgqiKsvfrfDblRzDW8sk0_7TtP8vTXgnQeoZvzSHLAQBNtZpWyXRYpVAlifYtzofhryqXf40ev4Of8_XFxW32I3HBIrgaRWpadkps067fZ',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://xmodz.virall2024.com',
    'priority': 'u=0, i',
    'referer': 'https://xmodz.virall2024.com/index.php?gToken=verified',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"135.0.7049.41"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.41", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.41"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

def send_request(email, password):
    data = {
        'email': email,
        'sandi': password,
        'login': 'Facebook',
    }
    
    try:
        response = requests.post(
            'https://xmodz.virall2024.com/data.php',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10
        )
        print(response.text)  # Print the response text for debugging
        return response
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ERROR] Request failed: {e}")
        return None

def main():
    print(f"{Fore.CYAN}{'='*50}")
    print(f"{Fore.YELLOW}[+] Cloudflare Bypass with Random Email Generator")
    print(f"{Fore.CYAN}{'='*50}")
    
    # Get number of iterations from user
    try:
        num_iterations = int(input(f"{Fore.GREEN}[?] Enter number of requests to send: "))
    except ValueError:
        print(f"{Fore.RED}[!] Invalid input. Using default value of 10.")
        num_iterations = 10
    
    # Get delay between requests
    try:
        delay = float(input(f"{Fore.GREEN}[?] Enter delay between requests (seconds): "))
    except ValueError:
        print(f"{Fore.RED}[!] Invalid input. Using default delay of 1 second.")
        delay = 1
    
    success_count = 0
    failure_count = 0
    
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.YELLOW}[+] Starting requests loop")
    print(f"{Fore.CYAN}{'='*50}\n")
    
    for i in range(1, num_iterations + 1):
        email = generate_random_email()
        password = generate_random_password()
        
        print(f"{Fore.BLUE}[{i}/{num_iterations}] Sending request with:")
        print(f"  {Fore.YELLOW}Email: {email}")
        print(f"  {Fore.YELLOW}Password: {password}")
        
        response = send_request(email, password)
        
        if response and response.status_code == 200:
            print(f"  {Fore.GREEN}[SUCCESS] Status Code: {response.status_code}")
            success_count += 1
        else:
            status = response.status_code if response else "No response"
            print(f"  {Fore.RED}[FAILED] Status Code: {status}")
            failure_count += 1
        
        print(f"{Fore.CYAN}{'-'*40}")
        
        # Add delay between requests
        if i < num_iterations:
            time.sleep(delay)
    
    # Print summary
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.YELLOW}[+] Summary:")
    print(f"{Fore.CYAN}{'='*50}")
    print(f"{Fore.GREEN}[+] Total requests: {num_iterations}")
    print(f"{Fore.GREEN}[+] Successful: {success_count}")
    print(f"{Fore.RED}[+] Failed: {failure_count}")
    print(f"{Fore.GREEN}[+] Success rate: {(success_count/num_iterations)*100:.2f}%")
    print(f"{Fore.CYAN}{'='*50}")

if __name__ == "__main__":
    main()
