import requests
import threading
from queue import Queue

# Dictionary of Indian websites and user profile URL formats
websites = {
    'Instagram': 'https://www.instagram.com/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'Flipkart': 'https://www.flipkart.com/user/{}',
    'Snapdeal': 'https://www.snapdeal.com/profile/{}',
    'Naukri': 'https://www.naukri.com/mnjuser/profile?id={}',
    'Justdial': 'https://www.justdial.com/profile/{}',
    'Rediff': 'https://www.rediff.com/profile/{}',
    'Twitter': 'https://twitter.com/{}',  # Twitter profile (India users)
    'Facebook': 'https://www.facebook.com/{}',  # Facebook profile
    'Quora': 'https://www.quora.com/profile/{}',  # Quora profile
    'GitHub': 'https://github.com/{}',  # GitHub user profile
    'Pinterest': 'https://in.pinterest.com/{}',  # Pinterest India
    'BharatMatrimony': 'https://profile.bharatmatrimony.com/{}',  # Matrimonial site
    'TikTok': 'https://www.tiktok.com/@{}',  # TikTok (user profile)
    'SoundCloud': 'https://soundcloud.com/{}',  # Music streaming profiles
    'Paytm': 'https://paytm.com/@{}',  # Paytm Wallet or business pages
    'IndiaMart': 'https://www.indiamart.com/proddetail/{}',  # Business/product profiles
    'Olx': 'https://www.olx.in/profile/{}',  # OLX India user profile
    'Gaana': 'https://gaana.com/artist/{}',  # Music service Gaana
    'Zomato': 'https://www.zomato.com/{}',  # Zomato (user or restaurant profiles)
    'Swiggy': 'https://www.swiggy.com/user/{}',  # Swiggy profiles (could be food business)
    'TimesJobs': 'https://www.timesjobs.com/candidate/{}/profile',  # TimesJobs
    'Glassdoor': 'https://www.glassdoor.co.in/Profile/{}',  # Glassdoor (Indian company reviews or people)
    'Vimeo': 'https://vimeo.com/{}',  # Video streaming
    'Behance': 'https://www.behance.net/{}',  # Behance portfolio
    'Flickr': 'https://www.flickr.com/photos/{}',  # Photography profile
}


# Lock for thread-safe printing
print_lock = threading.Lock()

# Queue for multithreaded processing
queue = Queue()

# Function to check if a profile exists on a website
def check_profile_existence(website_name, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with print_lock:
                print(f"[+] {website_name}: Profile found at {url}")
        else:
            with print_lock:
                print(f"[-] {website_name}: Profile not found")
    except requests.ConnectionError:
        with print_lock:
            print(f"[!] {website_name}: Could not connect to the website")

# Worker thread for processing the queue
def worker():
    while not queue.empty():
        website_name, username_url = queue.get()
        check_profile_existence(website_name, username_url)
        queue.task_done()

# Main function to run the OSINT tool
def osint_tool():
    # Get the username input from the user
    username = input("Enter the username to scan: ")
    
    print(f"\nScanning for the username '{username}' on Indian websites...\n")

    # Fill the queue with website checks
    for website_name, url_template in websites.items():
        profile_url = url_template.format(username)
        queue.put((website_name, profile_url))
    
    # Create and start threads for faster checking
    thread_count = 10  # Adjust thread count for faster processing
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish processing
    queue.join()
    
    print("\nScan complete.")

# Run the OSINT tool
if __name__ == "__main__":
    osint_tool()
