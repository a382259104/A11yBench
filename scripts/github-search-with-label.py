import requests
import json

def search_github_issues(keyword, output_file):
    url = f"https://api.github.com/search/issues?q={keyword}+label\
        +label:good-first-issue"
    key_word_response = requests.get(url)
    
    if key_word_response.status_code == 200:
        with open(output_file, "w") as file:
            json.dump(key_word_response.json(), file, indent=4)
        print(f"Results saved to {output_file}")
    else:
        print(f"Failed to fetch issues: {key_word_response.status_code}, {key_word_response.text}")

keyword = "accessibility"
output_path = "accessibility.json"  
search_github_issues(keyword, output_path)

keyword = "a11y"
output_path = "ally.json"
search_github_issues(keyword, output_path)