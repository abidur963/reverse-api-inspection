
from app.service_wrapper import JSONPlaceholderService


# Create the API service object
api = JSONPlaceholderService()

try:
    # Retrieve all posts
    posts = api.get_posts()

    print("================================")
    print("   API SERVICE WRAPPER TEST")
    print("================================")

    print("Total Posts:", len(posts))

    if posts:
        print("\nFirst Post:")
        print("ID:", posts[0]["id"])
        print("Title:", posts[0]["title"])

    # Retrieve one specific post
    print("\nRetrieving Post ID 5...")

    post = api.get_post(5)

    if post:
        print("Post ID:", post["id"])
        print("Post Title:", post["title"])

    print("\nAPI Wrapper Test: SUCCESS")

finally:
    # Close the HTTPX client
    api.close()
