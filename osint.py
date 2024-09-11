import aiohttp
import asyncio

websites = {
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "GitHub": "https://github.com/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    
    # Indian Social Media & Forums
    "Koo": "https://www.kooapp.com/profile/{}",
    "ShareChat": "https://sharechat.com/profile/{}",
    "Hike": "https://hike.in/{}",
    "Moj": "https://mojapp.in/u/{}",
    "Chingari": "https://chingari.io/{}",
    
    # Indian Shopping Sites
    "Flipkart": "https://www.flipkart.com/seller/{}",
    "Amazon India": "https://www.amazon.in/gp/profile/amzn1.account.{}",
    "Myntra": "https://www.myntra.com/profile/{}",
    "Snapdeal": "https://www.snapdeal.com/profile/{}",
    "Ajio": "https://www.ajio.com/u/{}",
    "Paytm Mall": "https://paytmmall.com/user/{}",
    
    # Indian News and Blogging Sites
    "Times of India Blogs": "https://timesofindia.indiatimes.com/blogs/{}",
    "Medium India": "https://medium.com/@{}",
    "WordPress India": "https://{}.wordpress.com/",
    "Blogger India": "https://{}.blogspot.com/",
    "Sulekha": "https://{}-sulekha.com/",
    
    # Indian Job Portals
    "Naukri": "https://resume.naukri.com/{}",
    "Monster India": "https://www.monsterindia.com/seeker/profile/{}",
    "Shine": "https://www.shine.com/profile/{}",
    "Indeed India": "https://www.indeed.co.in/cmp/{}",
    
    # Indian Education Platforms
    "Byju's": "https://byjus.com/profile/{}",
    "Unacademy": "https://unacademy.com/@{}",
    "Vedantu": "https://www.vedantu.com/profile/{}",
    "Toppr": "https://www.toppr.com/profile/{}",
    "Gradeup": "https://gradeup.co/@{}",
    
    # Indian Banking & Finance
    "Paytm": "https://paytm.com/@{}",
    "PhonePe": "https://www.phonepe.com/@{}",
    "BHIM": "https://www.bhimupi.org.in/users/{}",
    "Google Pay India": "https://gpay.app.goo.gl/{}",
    "FreeCharge": "https://www.freecharge.in/user/{}",
    "Mobikwik": "https://www.mobikwik.com/user/{}",
    "HDFC Bank": "https://netbanking.hdfcbank.com/netbanking/{}",
    "ICICI Bank": "https://www.icicibank.com/personal-banking/{}",
    "Axis Bank": "https://www.axisbank.com/profile/{}",
    
    # Indian Entertainment Platforms
    "Hotstar": "https://www.hotstar.com/in/users/{}",
    "Zee5": "https://www.zee5.com/profile/{}",
    "SonyLiv": "https://www.sonyliv.com/profile/{}",
    "Voot": "https://www.voot.com/profile/{}",
    "MX Player": "https://www.mxplayer.in/user/{}",
    "JioSaavn": "https://www.jiosaavn.com/user/{}",
    "Gaana": "https://gaana.com/user/{}",
    "Wynk Music": "https://wynk.in/music/profile/{}",
    
    # Indian Real Estate & Rentals
    "MagicBricks": "https://www.magicbricks.com/user/{}",
    "99acres": "https://www.99acres.com/profile/{}",
    "Housing.com": "https://housing.com/profile/{}",
    "NoBroker": "https://www.nobroker.in/profile/{}",
    
    # Indian Travel & Food
    "Zomato": "https://www.zomato.com/{}",
    "Swiggy": "https://www.swiggy.com/profile/{}",
    "Yatra": "https://www.yatra.com/profile/{}",
    "MakeMyTrip": "https://www.makemytrip.com/profile/{}",
    "Ola Cabs": "https://www.olacabs.com/profile/{}",
    "Uber India": "https://www.uber.com/in/profile/{}",
    "IRCTC": "https://www.irctc.co.in/nget/profile/{}"
}

single website
async def check_website(session, site_name, url):
    try:
        async with session.get(url, timeout=5) as response:  # Add a timeout of 5 seconds
            if response.status == 200:
                return f"{site_name}: verified"
            else:
                return f"{site_name}: not verified"
    except:
        return f"{site_name}: not verified"

# Asynchronous function to check all websites
async def check_all_websites(username):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for site_name, url_template in indian_websites.items():
            url = url_template.format(username)
            tasks.append(check_website(session, site_name, url))
        results = await asyncio.gather(*tasks)
        return results

# Main function
def main():
    print("Welcome to saisuhas12 GitHub Osint !!!!")
    print("\nPick any one option:")
    print("1 - Username")
    print("2 - Gmail")
    print("3 - Phone Number")
    print("4 - Exit")

    choice = input("Input: ")

    if choice == "1":
        username = input("\nGive username: ")
        print("Loading your data, please wait..........\n")
        results = asyncio.run(check_all_websites(username))
        for result in results:
            print(result)
    elif choice == "2":
        print("Gmail option not yet implemented.")
    elif choice == "3":
        print("Phone number option not yet implemented.")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
