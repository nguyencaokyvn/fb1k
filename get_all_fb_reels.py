import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_all_fb_reels(url):
    """
    Scrapes all Facebook Reels links from a given URL using Selenium.
    """
    print(f"Starting scraper for: {url}")
    print("Initializing Chrome driver...")
    
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Run in headless mode if you don't want to see the browser
    options.add_argument("--disable-notifications")
    options.add_argument("--mute-audio")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        time.sleep(5) # Wait for initial load

        # Close pop-up login if it appears (best effort)
        try:
            close_button = driver.find_element(By.XPATH, "//div[@aria-label='Close']")
            close_button.click()
            print("Closed login popup.")
        except:
            pass

        print("Scrolling to load all reels...")
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_attempts = 0
        max_scroll_attempts_without_change = 5
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3) # Wait for content to load
            
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                scroll_attempts += 1
                if scroll_attempts >= max_scroll_attempts_without_change:
                    print("Reached bottom of page or no new content loading.")
                    break
            else:
                scroll_attempts = 0
                last_height = new_height
                
            # Optional: Print current count of links found so far to show progress
            links_count = len(driver.find_elements(By.XPATH, "//a[contains(@href, '/reel/')]"))
            print(f"Scrolled... Found {links_count} potential reel links so far.")

        print("Finished scrolling. Extracting links...")
        
        # Find all anchor tags with '/reel/' in href
        elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/reel/')]")
        
        links = set()
        for element in elements:
            href = element.get_attribute('href')
            if href:
                # Clean up the URL (remove query parameters)
                clean_link = href.split('?')[0]
                links.add(clean_link)

        if links:
            # Extract channel name/ID from URL for filename
            # Example: https://www.facebook.com/ReelsUSA/reels -> ReelsUSA
            # Example: https://www.facebook.com/profile.php?id=1000... -> profile_id
            
            import os
            from urllib.parse import urlparse, parse_qs

            parsed_url = urlparse(url)
            path_parts = parsed_url.path.strip('/').split('/')
            
            channel_name = "unknown_channel"
            
            if 'profile.php' in url:
                query_params = parse_qs(parsed_url.query)
                if 'id' in query_params:
                    channel_name = query_params['id'][0]
            else:
                # Usually the first part of the path is the channel name if not profile.php
                if len(path_parts) > 0:
                    channel_name = path_parts[0]

            # Sanitize filename
            channel_name = "".join([c for c in channel_name if c.isalnum() or c in ('-', '_')])
            
            output_dir = os.path.join("downloads", "reels_links")
            os.makedirs(output_dir, exist_ok=True)
            
            filename = f"reels_links_{channel_name}.txt"
            output_file = os.path.join(output_dir, filename)

            with open(output_file, 'w') as f:
                for link in links:
                    f.write(link + '\n')
            print(f"Successfully saved {len(links)} unique links to {output_file}")
        else:
            print("No reel links found.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 get_all_fb_reels.py <FACEBOOK_REELS_URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    get_all_fb_reels(url)
