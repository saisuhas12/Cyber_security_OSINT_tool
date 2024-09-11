import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define website patterns for username, email, and phone number
username_websites = {
    "Blogger": "https://www.blogger.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Firefox Add-ons": "https://addons.mozilla.org/en-US/firefox/user/{}",
    "Google Sites": "https://sites.google.com/site/{}",
    "GitHub": "https://github.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Medium": "https://medium.com/@{}",
    "SlideShare": "https://www.slideshare.net/{}",
    "Issuu": "https://issuu.com/{}",
    "Weebly": "https://www.weebly.com/{}",
    "IMDb": "https://www.imdb.com/user/{}",
    "MediaFire": "https://www.mediafire.com/{}",
    "Hatena": "https://profile.hatena.ne.jp/{}",
    "Archive": "https://archive.org/details/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Gravatar": "https://gravatar.com/{}",
    "Change.org": "https://www.change.org/u/{}",
    "Sedo": "https://sedo.com/search/searchresult.php?domain={}",
    "4shared": "https://www.4shared.com/u/{}",
    "AOL": "https://www.aol.com/profile/{}",
    "TED": "https://www.ted.com/profiles/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "SourceForge": "https://sourceforge.net/u/{}/profile/",
    "Angelfire": "https://www.angelfire.lycos.com/{}",
    "Instructables": "https://www.instructables.com/member/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "The Verge": "https://www.theverge.com/users/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Bloglovin": "https://www.bloglovin.com/bloggers/{}",
    "Disqus": "https://disqus.com/by/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "Academia": "https://independent.academia.edu/{}",
    "Kickstarter": "https://www.kickstarter.com/profile/{}",
    "BuzzFeed": "https://www.buzzfeed.com/{}",
    "WikiHow": "https://www.wikihow.com/User:{}",
    "Dreamstime": "https://www.dreamstime.com/{}/info",
    "Box": "https://account.box.com/profile/{}",
    "Parallels": "https://forum.parallels.com/members/{}",
    "IBM": "https://www.ibm.com/account/profile/us?page=profile&id={}",
    "Rotten Tomatoes": "https://www.rottentomatoes.com/user/id/{}",
    "TrustPilot": "https://www.trustpilot.com/users/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Imgur": "https://imgur.com/user/{}",
    "Coursera": "https://www.coursera.org/user/{}",
    "Etsy": "https://www.etsy.com/people/{}",
    "Scoop.it": "https://www.scoop.it/u/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "Evernote": "https://www.evernote.com/pub/{}",
    "Answers.com": "https://www.answers.com/u/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "About.me": "https://about.me/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "IndieGoGo": "https://www.indiegogo.com/individuals/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "MixCloud": "https://www.mixcloud.com/{}",
    "Trello": "https://trello.com/{}",
    "Lenovo Forums": "https://forums.lenovo.com/t5/user/viewprofilepage/user-id/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Xfinity": "https://www.xfinity.com/profile/{}",
    "Discogs": "https://www.discogs.com/user/{}",
    "Technology Review": "https://www.technologyreview.com/author/{}/",
    "Reddit": "https://www.reddit.com/user/{}",
    "HubPages": "https://discover.hubpages.com/@{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Salesforce": "https://trailblazer.me/id/{}"
}

email_websites = {
    "Gravatar": "https://en.gravatar.com/{}",
    "GitHub Email": "https://github.com/search?q={}+in%3Aemail",
    "LinkedIn Email": "https://www.linkedin.com/pub/dir/?email={}",
    
    # Indian Social Media Platforms
    "Koo": "https://www.kooapp.com/profile/{}",
    "ShareChat": "https://sharechat.com/profile/{}",
    "Moj": "https://mojapp.in/u/{}",
    "Chingari": "https://chingari.io/profile/{}",

    # Indian E-commerce Platforms
    "Flipkart": "https://www.flipkart.com/seller/{}",
    "Amazon India": "https://www.amazon.in/gp/profile/amzn1.account.{}",
    "Myntra": "https://www.myntra.com/profile/{}",
    "Snapdeal": "https://www.snapdeal.com/profile/{}",
    "Ajio": "https://www.ajio.com/u/{}",
    "Paytm Mall": "https://paytmmall.com/user/{}",

    # Indian Job Portals
    "Naukri": "https://resume.naukri.com/{}",
    "Monster India": "https://www.monsterindia.com/seeker/profile/{}",
    "Shine": "https://www.shine.com/profile/{}",
    "Indeed India": "https://www.indeed.co.in/cmp/{}",
    "FreshersWorld": "https://www.freshersworld.com/profile/{}",

    # Indian Educational Platforms
    "Byju's": "https://byjus.com/profile/{}",
    "Unacademy": "https://unacademy.com/@{}",
    "Vedantu": "https://www.vedantu.com/profile/{}",
    "Toppr": "https://www.toppr.com/profile/{}",
    "Gradeup": "https://gradeup.co/@{}",
    "Testbook": "https://testbook.com/profile/{}",

    # Indian Banking & Financial Platforms
    "Paytm": "https://paytm.com/@{}",
    "PhonePe": "https://www.phonepe.com/@{}",
    "BHIM": "https://www.bhimupi.org.in/users/{}",
    "Google Pay India": "https://gpay.app.goo.gl/{}",
    "FreeCharge": "https://www.freecharge.in/user/{}",
    "Mobikwik": "https://www.mobikwik.com/user/{}",
    
    # Indian News and Blogging Platforms
    "Times of India Blogs": "https://timesofindia.indiatimes.com/blogs/{}",
    "Medium India": "https://medium.com/@{}",
    "WordPress India": "https://{}.wordpress.com/",
    "Blogger India": "https://{}.blogspot.com/",
    "Sulekha": "https://{}-sulekha.com/",

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

    # Indian Travel & Food Platforms
    "Zomato": "https://www.zomato.com/{}",
    "Swiggy": "https://www.swiggy.com/profile/{}",
    "Yatra": "https://www.yatra.com/profile/{}",
    "MakeMyTrip": "https://www.makemytrip.com/profile/{}",
    "Ola Cabs": "https://www.olacabs.com/profile/{}",
    "Uber India": "https://www.uber.com/in/profile/{}",

}

phone_websites = {
    "TrueCaller": "https://www.truecaller.com/search/in/{}",
    "PhonePe": "https://www.phonepe.com/{}",
    "Paytm": "https://paytm.com/@{}",

    # Indian Telecom Services
    "Jio": "https://www.jio.com/en-in/{}.html",
    "Airtel": "https://www.airtel.in/my-account/{}",
    "Vodafone Idea": "https://www.myvi.in/vitc/{}",
    "BSNL": "https://portal.bsnl.in/phone/{}",
    "MTNL": "https://mtnl.in/phone/{}",

    # Indian Financial Services
    "Google Pay": "https://pay.google.com/{}",
    "Freecharge": "https://www.freecharge.in/{}",
    "Mobikwik": "https://www.mobikwik.com/user/{}",
    "BharatPe": "https://www.bharatpe.com/{}",
    "Razorpay": "https://razorpay.com/{}",
    "ICICI Bank": "https://www.icicibank.com/personal-banking/{}",
    "HDFC Bank": "https://netbanking.hdfcbank.com/{}",
    "SBI": "https://onlinesbi.com/{}",
    "Kotak Bank": "https://www.kotak.com/{}",
    "Axis Bank": "https://www.axisbank.com/profile/{}",

    # Indian Shopping and E-commerce
    "Flipkart": "https://www.flipkart.com/user/{}",
    "Amazon India": "https://www.amazon.in/profile/{}",
    "Snapdeal": "https://www.snapdeal.com/profile/{}",
    "Myntra": "https://www.myntra.com/user/{}",
    "Ajio": "https://www.ajio.com/u/{}",
    "ShopClues": "https://www.shopclues.com/profile/{}",
    "BigBasket": "https://www.bigbasket.com/u/{}",
    "Grofers": "https://www.grofers.com/u/{}",
    "Tata CLiQ": "https://www.tatacliq.com/profile/{}",

    # Indian Social Media Platforms
    "Koo": "https://www.kooapp.com/profile/{}",
    "ShareChat": "https://sharechat.com/profile/{}",
    "Moj": "https://mojapp.in/u/{}",
    "Chingari": "https://chingari.io/profile/{}",

    # Indian Food & Delivery Platforms
    "Zomato": "https://www.zomato.com/{}",
    "Swiggy": "https://www.swiggy.com/profile/{}",
    "Dominos India": "https://www.dominos.co.in/profile/{}",
    "Dunzo": "https://www.dunzo.com/profile/{}",
    "FreshMenu": "https://www.freshmenu.com/user/{}",

    # Indian Travel Platforms
    "IRCTC": "https://www.irctc.co.in/profile/{}",
    "Yatra": "https://www.yatra.com/profile/{}",
    "MakeMyTrip": "https://www.makemytrip.com/profile/{}",
    "Ola Cabs": "https://www.olacabs.com/profile/{}",
    "Uber India": "https://www.uber.com/in/profile/{}",
    "RedBus": "https://www.redbus.in/profile/{}",

    # Indian News Platforms
    "Times of India": "https://timesofindia.indiatimes.com/user/{}",
    "Hindustan Times": "https://www.hindustantimes.com/user/{}",
    "NDTV": "https://www.ndtv.com/profile/{}",
    "India Today": "https://www.indiatoday.in/user/{}",
    "The Hindu": "https://www.thehindu.com/profile/{}",
    "ABP News": "https://www.abplive.com/profile/{}",

    # Indian Educational Platforms
    "Byju's": "https://byjus.com/profile/{}",
    "Unacademy": "https://unacademy.com/@{}",
    "Vedantu": "https://www.vedantu.com/profile/{}",
    "Toppr": "https://www.toppr.com/profile/{}",
    "Gradeup": "https://gradeup.co/@{}",
    "Testbook": "https://testbook.com/profile/{}",
    
    # Real Estate Platforms
    "99acres": "https://www.99acres.com/profile/{}",
    "MagicBricks": "https://www.magicbricks.com/user/{}",
    "Housing.com": "https://housing.com/profile/{}",
    "NoBroker": "https://www.nobroker.in/profile/{}",

    # Indian Government Services
    "Aadhaar": "https://uidai.gov.in/{}",
    "DigiLocker": "https://www.digilocker.gov.in/profile/{}",
    "UMANG": "https://web.umang.gov.in/web/{}",
    "EPFO": "https://unifiedportal-epfo.epfindia.gov.in/{}",
    "GSTIN": "https://services.gst.gov.in/services/searchtp/{}"
}

def check_url(site, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return (site, "verified")
        else:
            return (site, "not verified")
    except requests.exceptions.RequestException:
        return (site, "not verified")

def osint_search(input_type, input_value):
    if input_type == '1':
        websites = username_websites
    elif input_type == '2':
        websites = email_websites
    elif input_type == '3':
        websites = phone_websites
    else:
        print("Invalid input type.")
        return

    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers based on your system
        futures = [executor.submit(check_url, site, url.format(input_value)) for site, url in websites.items()]

        for future in as_completed(futures):
            site, result = future.result()
            print(f"{site}: {result}")

if __name__ == "__main__":
    print("Welcome to Sai Suhas GitHub OSINT!")
    print("\nPick any one option:")
    print("1 - username")
    print("2 - email")
    print("3 - phone number")
    print("4 - exit")

    input_type = input("Choose an option (1/2/3/4): ")

    if input_type == '4':
        print("Exiting...")
    else:
        input_value = input("Enter the value (username/email/phone number): ")
        print("Loading your data, please wait...")

        osint_search(input_type, input_value)
