import json

# Function to load data from a JSON file
def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)
    
# Function to find pages a user might like based on common interests
def find_pages_you_might_like(user_id, data):
    # Dictionary to hold user interests
    user_pages = {}
    #populate the dictionary
    for user in data["users"]:
        user_pages[user["id"]] = set(user["liked_pages"])

    # if the user is not found
    if user_id not in user_pages:
        return []
        
    user_liked_pages = user_pages[user_id]
    page_suggestions = {}

    for other_user, pages in user_pages.items():
        if other_user != user_id:
            # Find common liked pages
            shared_pages = user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                page_suggestions[page] = page_suggestions.get(page, 0) + len(shared_pages)

    sorted_pages = sorted(page_suggestions.items(), key=lambda x: x[1], reverse=True)
    return [(page_id, score) for page_id, score in sorted_pages]

data = load_data("massive_data.json")
user_id = 1
page_recommendation = find_pages_you_might_like(user_id, data)
print(page_recommendation)