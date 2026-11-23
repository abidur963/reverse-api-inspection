
import json
from pathlib import Path

from app.service_wrapper import JSONPlaceholderService


def extract_posts():

    api = JSONPlaceholderService()

    try:
        print("====================================")
        print("       DATA EXTRACTION TEST")
        print("====================================")

        # Step 1: Retrieve posts from API
        posts = api.get_posts()

        if not posts:
            print("Extraction failed: No data received.")
            return

        print("API Connection: SUCCESS")
        print("Total Records Received:", len(posts))

        # Step 2: Extract required fields
        extracted_data = []

        for post in posts:
            record = {
                "id": post.get("id"),
                "userId": post.get("userId"),
                "title": post.get("title"),
                "body": post.get("body")
            }

            extracted_data.append(record)

        # Step 3: Validate extracted records
        valid_records = []

        for record in extracted_data:
            if all(record.values()):
                valid_records.append(record)

        print("Valid Records:", len(valid_records))

        # Step 4: Save data into JSON file
        output_file = Path("extracted_posts.json")

        with output_file.open("w", encoding="utf-8") as file:
            json.dump(
                valid_records,
                file,
                indent=4,
                ensure_ascii=False
            )

        # Step 5: Display extraction summary
        print("\nFirst Extracted Record:")

        print(json.dumps(valid_records[0], indent=4))

        print("\nSaved File:", output_file)
        print("Extracted Records:", len(valid_records))

        print("\nDATA EXTRACTION: SUCCESS")

    except (TypeError, ValueError, KeyError) as error:
        print("Data Processing Error:", error)

    finally:
        api.close()


if __name__ == "__main__":
    extract_posts()
