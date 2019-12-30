import requests


# create a simple function to pass query parameters to github api
def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "  # github api convention as it expects a ' ' after each query parameter
    for language in languages:
        query += f"language:{language} "  # github api convention as it expects a ' ' after each query parameter
    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    github_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(github_api_repo_search_url, params=parameters)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An unexpected error occurred. Status code was: {status_code}")
    else:
        response_json = response.json()["items"]
        return response_json


if __name__ == '__main__':
    languages_list = ["Python", "Javascript", "C++"]
    results = repos_with_most_stars(languages=languages_list)
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        print(f"{name} is {language} repo with {stars} stars")
