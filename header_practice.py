
import httpx

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Accept": "application/json",
    "User-Agent": "MyPythonClient/1.0"
}

try:
    response = httpx.get(
        url,
        headers=headers,
        timeout=15
    )

    print("Status Code:", response.status_code)
    print("Response Format:", response.headers.get("content-type"))

    data = response.json()

    print("Total Posts:", len(data))

    print("\nFirst Post:")
    print(data[0])

except httpx.RequestError as error:
    print("Connection Error:", error)

except httpx.HTTPStatusError as error:
    print("HTTP Error:", error)
response = httpx.get(
    url,
    headers=headers,
    timeout=15
)
print("\nRequest Headers:")

for key, value in response.request.headers.items():
    print(f"{key}: {value}")
    