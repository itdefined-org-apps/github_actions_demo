import os
import datetime

# Print all environment variables for debugging
print("🔍 Debugging: Environment Variables")
for key, value in os.environ.items():
    print(f"{key} = {value}")

# Read input correctly
name = os.getenv("INPUT_NAME", "Developer")  # ✅ Corrected input handling

# Print greeting
print(f"Hello, {name}!")

# Get current timestamp
current_time = datetime.datetime.utcnow().isoformat()
print(f"Current Time: {current_time}")