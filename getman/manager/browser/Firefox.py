import os

from getman.manager.browser.base import BrowserBase


class Firefox(BrowserBase):

    def get_cookies_by_url(self, url: str) -> dict:

        profile_path = os.path.join(self.app_data, "Mozilla", "Firefox", "Profiles")

        # List all directories (profiles) in the Firefox profiles folder
        profiles = os.listdir(profile_path)

        # Find the appropriate profile based on your criteria
        desired_profile = None
        for profile in profiles:
            if profile.endswith(".default-release"):
                desired_profile = profile
                break
        if desired_profile is not None:
            profile_path = os.path.join(profile_path, desired_profile)
            print("Found Firefox profile path:", profile_path)
        else:
            print("No default-release profile found.")

        cookies_db = os.path.join(profile_path, 'cookies.sqlite')
        print(cookies_db)
        cookies_dict = {}
        try:
            # Connect to the Firefox cookies database
            conn = self.connect_sql_lite3(cookies_db)
            cursor = conn.cursor()

            # Get cookies from the database for the specified host
            cursor.execute("SELECT name, value FROM moz_cookies WHERE host LIKE ?", ('%' + url + '%',))
            cookies = cursor.fetchall()
            for cookie in cookies:
                cookie_name = cookie[0]
                cookie_value = cookie[1]

                # Use the cookie name as the key in the dictionary
                cookies_dict[cookie_name] = cookie_value

            # Close the database connection
            conn.close()
        except Exception as e:
            print(f"Error accessing Firefox cookies: {e}")
            return {}

        return cookies_dict
