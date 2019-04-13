import requests

def create_query(languages, min_stars = 50000):
    query = f"stars:>{ min_stars } "
    for language in languages:
        query += f"language:{ language } "
    return query

def repos_with_most_stars(languages, sort = "stars", order = "desc"):
    gh_api_url = "https://api.github.com/search/repositories"
    q = create_query(languages)
    params = { "q": q, "sort": sort, "order": order }
    response = requests.get(gh_api_url, params)
    response_status_code = response.status_code
    if response_status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if response_status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: { response_status_code }.")
    response_json = response.json()["items"]
    return response_json

if __name__ == "__main__":
    languages = ["Python", "JavaScript"]
    results = repos_with_most_stars(languages)

    for result in results:
        name = result["name"]
        language = result["language"]
        stargazers_count = result["stargazers_count"]
        print(f"-> { name } is a { language } repo with { stargazers_count } stars.")
