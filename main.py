from playwright.sync_api import sync_playwright
import re
import time
from openai import OpenAI

class SocialMediaScraper:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.client = OpenAI()  # Initialize OpenAI client

    def start_browser(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close_browser(self):
        if self.browser:
            self.browser.close()

    def find_instagram_from_youtube(self, youtube_username):
        try:
            print(f"Searching YouTube channel @{youtube_username} for Instagram links...")
            self.page.goto(f"https://www.youtube.com/@{youtube_username}/videos")
            self.page.wait_for_load_state('networkidle')  # Wait for the page to fully load
            print("Scanning YouTube about page...")
            
            links = self.page.query_selector_all("a[href*='instagram.com']")
            if not links:
                print("No Instagram links found in YouTube about page")
                return None
            
            for link in links:
                href = link.get_attribute("href")
                if href:
                    instagram_username = re.search(r"instagram\.com/([^/]+)", href)
                    if instagram_username:
                        print(f"Found Instagram link: {href}")
                        return instagram_username.group(1)
        except Exception as e:
            print(f"Error finding Instagram from YouTube: {e}")
        return None

    def find_youtube_from_instagram(self, instagram_username):
        try:
            print(f"Searching Instagram profile @{instagram_username} for YouTube links...")
            self.page.goto(f"https://www.instagram.com/{instagram_username}")
            self.page.wait_for_load_state('networkidle')  # Wait for the page to fully load
            print("Scanning Instagram bio...")
            
            links = self.page.query_selector_all("a[href*='youtube.com']")
            if not links:
                print("No YouTube links found in Instagram bio")
                return None
            
            for link in links:
                href = link.get_attribute("href")
                if href:
                    youtube_username = re.search(r"youtube\.com/(@?[^/]+)", href)
                    if youtube_username:
                        print(f"Found YouTube link: {href}")
                        return youtube_username.group(1)
        except Exception as e:
            print(f"Error finding YouTube from Instagram: {e}")
        return None

    def scrape_youtube_posts(self, youtube_username):
        try:
            print(f"\nFetching recent YouTube videos for @{youtube_username}...")
            self.page.goto(f"https://www.youtube.com/@{youtube_username}/videos")
            self.page.wait_for_load_state('networkidle')  # Wait for the page to fully load

            videos = []
            # Get channel description from meta tag
            channel_description = self.page.query_selector('meta[property="og:description"]')
            channel_desc = channel_description.get_attribute("content") if channel_description else "No description available"
            print(f"Channel description: {channel_desc}")

            video_elements = self.page.query_selector_all("#video-title")[:2]  # Get first 2 videos using ID selector
            
            if not video_elements:
                print("No videos found on channel")
                return []
            
            print(f"Found {len(video_elements)} recent videos")
            for video in video_elements:
                title = video.inner_text()
                href = video.get_attribute("href")
                if title and href:
                    videos.append({
                        "title": title,
                        "url": f"https://www.youtube.com{href}",
                        "channel_description": channel_desc
                    })
            return videos
        except Exception as e:
            print(f"Error scraping YouTube posts: {e}")
            return []

    def scrape_instagram_posts(self, instagram_username):
        try:
            print(f"\nFetching recent Instagram posts for @{instagram_username}...")
            self.page.goto(f"https://www.instagram.com/{instagram_username}")
            self.page.wait_for_load_state('networkidle')  # Wait for the page to fully load

            posts = []
            post_elements = self.page.query_selector_all("article a")[:2]
            
            if not post_elements:
                print("No posts found on profile")
                return []
            
            print(f"Found {len(post_elements)} recent posts")
            for post in post_elements:
                href = post.get_attribute("href")
                if href:
                    posts.append({
                        "url": f"https://www.instagram.com{href}"
                    })
            return posts
        except Exception as e:
            print(f"Error scraping Instagram posts: {e}")
            return []

    def scrape_twitter_posts(self, twitter_username):
        try:
            print(f"\nFetching recent Twitter posts for @{twitter_username}...")
            self.page.goto(f"https://twitter.com/{twitter_username}")
            self.page.wait_for_load_state('networkidle')  # Wait for the page to fully load

            tweets = []
            tweet_elements = self.page.query_selector_all("article div[lang]")[:2]  # Get first 2 tweets
            
            if not tweet_elements:
                print("No tweets found on profile")
                return []
            
            print(f"Found {len(tweet_elements)} recent tweets")
            for tweet in tweet_elements:
                text = tweet.inner_text()
                if text:
                    tweets.append({
                        "text": text
                    })
            return tweets
        except Exception as e:
            print(f"Error scraping Twitter posts: {e}")
            return []

    def open_social_media_tabs(self, username):
        try:
            print(f"Opening YouTube page for @{username}...")
            youtube_posts = self.scrape_youtube_posts(username)
            
            print("\nSwitching to Instagram...")
            self.page.goto(f"https://www.instagram.com/{username}")
            instagram_posts = self.scrape_instagram_posts(username)
            
            print("\nSwitching to Twitter...")
            self.page.goto(f"https://twitter.com/{username}")
            twitter_posts = self.scrape_twitter_posts(username)
            
            return youtube_posts, [], []  # Return empty lists for Instagram and Twitter
        except Exception as e:
            print(f"Error navigating social media: {e}")
            return [], [], []

    def generate_professional_dm(self, youtube_username, instagram_posts, youtube_posts, twitter_posts):
        try:
            # Prepare content summary
            content_summary = "Recent content includes:\n"
            content_summary += "YouTube Videos:\n" + "\n".join([f"- {post['title']}" for post in youtube_posts]) + "\n"
            content_summary += "Instagram Posts:\n" + "\n".join([f"- {post['url']}" for post in instagram_posts]) + "\n"
            content_summary += "Twitter Posts:\n" + "\n".join([f"- {post['text']}" for post in twitter_posts]) + "\n"

            # Generate DM with content context
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Create a short, professional DM from Vihaan asking the YouTuber @{youtube_username} to create a community on Nas.io. Dont start with hope you are well, start with I am a fan... Make it relevant to their content if possible. {content_summary}"}
                ]
            )
            message = completion.choices[0].message.content
            print("\nGenerated DM:")
            print("-" * 50)
            print(message)
            print("-" * 50)
        except Exception as e:
            print(f"Error generating DM: {e}")

def main():
    print("Initializing Scraper...")
    time.sleep(0.5)
    scraper = SocialMediaScraper()
    scraper.start_browser()
    print("Browser started successfully")

    try:
        username = input("Enter username (without @): ")
        print("\n" + "="*50)
        print("Starting YouTube scraping...")
        print("="*50 + "\n")
        
        # Get posts from YouTube only
        youtube_posts, _, _ = scraper.open_social_media_tabs(username)
        for post in youtube_posts:
            print(post)

        # Comment out DM generation for now
        scraper.generate_professional_dm(username, [], youtube_posts, [])

    except Exception as e:
        print(f"\nAn error occurred during execution: {e}")
    
    input("Press Enter to close the script and browser...")

if __name__ == "__main__":
    main()
