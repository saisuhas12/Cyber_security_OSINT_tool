import requests

# List of websites to check
websites = {
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Tumblr": "https://{}.tumblr.com/",
    "Vimeo": "https://vimeo.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Medium": "https://medium.com/@{}",
    "Dribbble": "https://dribbble.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "GitLab": "https://gitlab.com/{}",
    "AngelList": "https://angel.co/{}",
    "Behance": "https://www.behance.net/{}",
    "Blogger": "https://{}.blogspot.com/",
    "WordPress": "https://{}.wordpress.com/",
    "SlideShare": "https://www.slideshare.net/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "LastFM": "https://www.last.fm/user/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "WeHeartIt": "https://weheartit.com/{}",
    "Patreon": "https://www.patreon.com/{}",
    "BitBucket": "https://bitbucket.org/{}",
    "500px": "https://500px.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Venmo": "https://venmo.com/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Strava": "https://www.strava.com/athletes/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "KooApp": "https://www.kooapp.com/profile/{}",
    "Dev.to": "https://dev.to/{}",
    "Notion": "https://www.notion.so/{}",
    "Bitly": "https://bit.ly/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "CodeChef": "https://www.codechef.com/users/{}",
    "TopCoder": "https://www.topcoder.com/members/{}",
    "LeetCode": "https://leetcode.com/{}",
    "HackerNews": "https://news.ycombinator.com/user?id={}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Upwork": "https://www.upwork.com/freelancers/~{}",
    "Trello": "https://trello.com/{}",
    "Zoho": "https://{}.zoho.com/",
    "Gravatar": "https://en.gravatar.com/{}",
    "Kickstarter": "https://www.kickstarter.com/profile/{}",
    "CrowdRise": "https://www.crowdrise.com/{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "Angel.co": "https://angel.co/{}",
    "Coursera": "https://www.coursera.org/user/{}",
    "Skillshare": "https://www.skillshare.com/user/{}",
    "Codecademy": "https://www.codecademy.com/profiles/{}",
    "Pluralsight": "https://app.pluralsight.com/profile/{}",
    "LiveJournal": "https://{}.livejournal.com/",
    "Meetup": "https://www.meetup.com/members/{}",
    "Kinja": "https://{}.kinja.com/",
    "VK": "https://vk.com/{}",
    "OK.ru": "https://ok.ru/{}",
    "Taringa": "https://www.taringa.net/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "Weibo": "https://www.weibo.com/{}",
    "Zomato": "https://www.zomato.com/{}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{}",
    "Mastodon": "https://{}/@{}",
    "Ello": "https://ello.co/{}",
    "Vero": "https://www.vero.co/{}",
    "Rumble": "https://rumble.com/user/{}",
    "Parler": "https://parler.com/profile/{}",
    "Gab": "https://gab.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "OnlyFans": "https://onlyfans.com/{}",
    "Discord": "https://discord.com/users/{}",
    "Telegram": "https://t.me/{}",
    "WhatsApp": "https://wa.me/{}",
    "Zoom": "https://zoom.us/u/{}",
    "Microsoft": "https://account.microsoft.com/profile/?username={}",
    "Apple": "https://appleid.apple.com/account#!&page=signin&username={}",
    "Netflix": "https://www.netflix.com/{}",
    "Amazon": "https://www.amazon.com/gp/profile/amzn1.account.{}",
    "eBay": "https://www.ebay.com/usr/{}",
    "AliExpress": "https://www.aliexpress.com/store/{}",
    "Walmart": "https://www.walmart.com/cp/{}",
    "Flipkart": "https://www.flipkart.com/seller/{}",
    "PayPal": "https://www.paypal.me/{}",
    "BitChute": "https://www.bitchute.com/channel/{}",
    "Peertube": "https://{}/videos/watch/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "Anilist": "https://anilist.co/user/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "IMDB": "https://www.imdb.com/user/ur{}",
    "Discogs": "https://www.discogs.com/user/{}"
}

# Function to check if a username, email, or phone exists on the given platforms
def check_username(username):
    print("Checking username availability...\n")
    verified_sites = []
    not_verified_sites = []

    for site, url in websites.items():
        try:
            response = requests.get(url.format(username))
            if response.status_code == 200:
                verified_sites.append(site)
            else:
                not_verified_sites.append(site)
        except Exception as e:
            print(f"Error checking {site}: {e}")
    
    print("\nResults for Username:")
    for site in verified_sites:
        print(f"{site}: verified (username exists)")
    for site in not_verified_sites:
        print(f"{site}: not verified (username not found)")

# Main menu to choose between options
def main_menu():
    print("\nWelcome to Sai Suhas' GitHub OSINT Tool!!!!\n")
    print("Pick any one option:")
    print("1 - Username")
    print("2 - Email")
    print("3 - Phone Number")
    print("4 - Exit")

    choice = input("\n(Input: 1): ")

    if choice == '1':
        username = input("\nEnter username: ")
        check_username(username)
    elif choice == '4':
        print("Exiting...")
        exit()
    else:
        print("Invalid input. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
