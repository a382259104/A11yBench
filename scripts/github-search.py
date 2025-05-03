import requests
import json

def search_github_issues(keyword):

    """
    Searches GitHub issues for a given keyword and saves the results to a JSON file.
    """
    
    # Only 5 pages
    for i in range(1, 5):
        url = f"https://api.github.com/search/issues?q={keyword}+body:*\
            &per_page=100&page={i}"
        key_word_response = requests.get(url)
        
        output_file = f"{keyword}_page_{i}.json"
        if key_word_response.status_code == 200:
            with open(output_file, "w") as file:
                json.dump(key_word_response.json(), file, indent=4)
            print(f"Results saved to {output_file}")
        else:
            print(f"Failed to fetch issues: {key_word_response.status_code}, {key_word_response.text}")



keyword = "accessibility" 
search_github_issues(keyword)
print("Done with accessibility")
