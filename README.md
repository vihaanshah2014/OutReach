Social Media Outreach AI
====================

This project provides a Python-based scraper that extracts recent posts and links from YouTube, Instagram, and Twitter profiles. It also generates professional direct messages (DM) based on the scraped content to promote Nas.io.

Features
--------

*   **YouTube Scraping**: Extract recent video titles, URLs, and channel descriptions.
    
*   **Instagram Scraping**: Extract recent post URLs from a user's profile.
    
*   **Twitter Scraping**: Extract recent tweets from a user's profile.
    
*   **AI-Generated DMs**: Use OpenAI's API to craft professional, personalized messages based on a user's content.
    

Requirements
------------

### Python Packages

*   playwright
    
*   openai
    
*   re
    
*   time
    

### Setup

1.  pip install playwright openai
    
2.  playwright install
    
3.  Configure OpenAI API credentials in your environment or as needed. (set OPENAI_API_KEY=yourkey)
    

Usage
-----

### Running the Script

1.  source venv/bin/activate # Linux/MacOSvenv\\Scripts\\activate # Windows
    
2.  python main.py
    
3.  Enter the username (without the @) when prompted, and the script will:
    
    *   Scrape YouTube, Instagram, and Twitter posts.
        
    *   Generate a professional DM based on the user's content.
        

### Sample Usage

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   (venv) C:\Users\Dell\Documents\GitHub\OutReach>python main.py  Initializing Scraper...  Browser started successfully  Enter username (without @): NasDaily  ==================================================  Starting YouTube scraping...  ==================================================  Opening YouTube page for @NasDaily...  Fetching recent YouTube videos for @NasDaily...  Channel description: Nas means "people" in Arabic.  My mission?  To show you the most incredible people and places on planet Earth.  I wear the same T-shirt design because it reminds me to treasure life.  And I always scream when I make videos. Hope that's cool.  That’s 1 minute, see you tomorrow! ;)  Found 2 recent videos  Switching to Instagram...  Fetching recent Instagram posts for @NasDaily...  Found 2 recent posts  Switching to Twitter...  Fetching recent Twitter posts for @NasDaily...  Found 2 recent tweets  Generated DM:  --------------------------------------------------  Subject: Let's Connect!  Hi @NasDaily,  I am a fan of your amazing storytelling and the way you connect with your audience across various platforms. Your recent content has really inspired many, and I believe it would be even more impactful if you had a dedicated community space on Nas.io.  I would love to hop on a short 15-minute call to walk you through how Nas.io can help you engage your followers more deeply and foster meaningful interactions. Otherwise, feel free to check it out yourself—it's free and super easy to set up!  Looking forward to hearing from you!  Best,  Vihaan  --------------------------------------------------  Press Enter to close the script and browser...   `

Key Methods in the Script
-------------------------

### 1\. find\_instagram\_from\_youtube(youtube\_username)

Finds Instagram links in a YouTube channel's about page or videos.

### 2\. find\_youtube\_from\_instagram(instagram\_username)

Finds YouTube links in an Instagram profile's bio.

### 3\. scrape\_youtube\_posts(youtube\_username)

Scrapes recent video titles and URLs from a YouTube channel.

### 4\. scrape\_instagram\_posts(instagram\_username)

Scrapes recent post URLs from an Instagram profile.

### 5\. scrape\_twitter\_posts(twitter\_username)

Scrapes recent tweets from a Twitter profile.

### 6\. generate\_professional\_dm()

Uses OpenAI's GPT model to create a personalized message to promote Nas.io.

Contribution
------------

Feel free to open issues or create pull requests for new features or bug fixes. Suggestions are always welcome!
