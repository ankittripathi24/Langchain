import os


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape information from Linkedin profiles,
    Manually scrape the information from the LinkedIn profile
    """
    import requests

    api_key = os.getenv("PROXYCURL_API_KEY")
    headers = {"Authorization": "Bearer " + api_key}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    params = {
        "linkedin_profile_url": "https://linkedin.com/in/johnrmarty/",
        "facebook_profile_url": "https://facebook.com/johnrmarty/",
        "twitter_profile_url": "https://twitter.com/johnrmarty/",
        "fallback_to_cache": "on-error",
        "use_cache": "if-present",
        "skills": "include",
        "inferred_salary": "include",
        "personal_email": "include",
        "personal_contact_number": "include",
        "twitter_profile_id": "include",
        "facebook_profile_id": "include",
        "github_profile_id": "include",
        "extra": "include",
    }
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=headers
    )

    return response
