import os

# read token from environment variable
token = os.getenv("MY_API_TOKEN")

if not token:
    raise RuntimeError("No API token found. Make sure it's set in the workflow.")

# use it wherever needed
print(f"Using token (masked): {token[:4]}****")  # never print full token in logs
