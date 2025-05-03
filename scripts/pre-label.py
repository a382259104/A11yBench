from openai import OpenAI
from dotenv import load_dotenv
import json
import os


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prompt = """
Classify this GitHub issue into ONE of these WCAG violation categories:

1. color-contrast - Text/background contrast ratio below 4.5:1 (e.g., "button text too light")
2. missing-alt-text - Images/icons without alt text (e.g., "<img src='logo.png'>")
3. keyboard-navigation - Non-keyboard-operable elements (e.g., "can't tab to dropdown")
4. aria-misuse - Incorrect ARIA roles/states (e.g., "role='button' missing aria-pressed")
5. focus-management - Missing focus indicators or broken focus order (e.g., "focus invisible on buttons")
6. semantic-html - Misused HTML tags (e.g., "<div onclick> instead of <button>")
7. mobile-responsive - Touch targets <44px or viewport issues (e.g., "checkbox too small on mobile")
8. motion-risk - Auto-playing motion without controls (e.g., "carousel auto-advances too fast")
9. language-errors - Missing lang attributes (e.g., "<html> missing lang='en'")
10. skip-link - Missing "Skip to Content" links (e.g., "no way to skip navigation")
11. pdf-accessibility - Untagged PDFs (e.g., "PDF has no headings")
12. captions-audio - Missing captions/transcripts (e.g., "video has no subtitles")
13. other - General accessibility issues not covered above
14. none - if the issue is not related to accessibility, or body is empty
15. pointer-issues - hovering/scrolling/clicking issues (e.g., "hover menu not working")

Respond ONLY with the label name. Example: "missing-alt-text"

ISSUE TITLE: {title}
ISSUE BODY: {body}
"""
 
        
# Load your GitHub issues
with open(f'./accessibility-issues/accessibility_page_4.json') as f:
    issues = json.load(f)
    issues = issues['items']
    
result = {}
count = 1


for issue in issues:
    
    # Specify the model and input   
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt.format(title=issue['title'], body=issue['body']),
    )
    
    pre_labled_issue = response.output[0].content[0].text
    
    issue['predicted_label'] = pre_labled_issue
    print(f"Added issue label: {issue['predicted_label']}, count: {count}")
    result[count] = {
        'title': issue['title'],
        'body': issue['body'],
        'html_url': issue['html_url'],
        'created_at': issue['created_at'],
        'updated_at': issue['updated_at'],
        'state': issue['state'],
        'labels': issue['labels'],
        'predicted_label': issue['predicted_label']
    }
    count += 1
    


# Save pre-labeled data
with open(f'prelabeled_issues_4.json', 'w') as f:
    json.dump(result, f)

print("Done with pre-labeling")
