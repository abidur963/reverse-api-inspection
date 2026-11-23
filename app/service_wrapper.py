
import httpx


class JSONPlaceholderService:

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

        self.headers = {
            "Accept": "application/json",
            "User-Agent": "MyPythonClient/1.0"
        }

        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=15
        )

    def get_posts(self):
        """Retrieve all posts from the API."""

        try:
            response = self.client.get("/posts")

            response.raise_for_status()

            return response.json()

        except httpx.RequestError as error:
            print("Connection Error:", error)

        except httpx.HTTPStatusError as error:
            print("HTTP Error:", error)

        return []

    def get_post(self, post_id):
        """Retrieve one post using its ID."""

        try:
            response = self.client.get(f"/posts/{post_id}")

            response.raise_for_status()

            return response.json()

        except httpx.RequestError as error:
            print("Connection Error:", error)

        except httpx.HTTPStatusError as error:
            print("HTTP Error:", error)

        return None

    def close(self):
        """Close the HTTP client."""

        self.client.close()
