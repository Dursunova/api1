import requests


BASE_URL = "https://petstore.swagger.io/v2/pet/"


test_results = []

for pet_id in range(100):
    url = f"{BASE_URL}{pet_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                pet_data = response.json()
                if pet_data.get("id") == pet_id:
                    test_results.append(f"ID {pet_id}: PASS (200 - Pet found)")
                else:
                    test_results.append(f"ID {pet_id}: FAIL (200 - Incorrect pet data)")
            except ValueError:
                test_results.append(f"ID {pet_id}: FAIL (200 - Invalid JSON format)")
        elif response.status_code == 404:
            test_results.append(f"ID {pet_id}: PASS (404 - Pet not found)")
        else:
            test_results.append(f"ID {pet_id}: FAIL ({response.status_code} - Unexpected status code)")
    except requests.exceptions.RequestException as e:
        test_results.append(f"ID {pet_id}: FAIL (Request error - {e})")


with open("test_results.txt", "w") as file:
    for result in test_results:
        file.write(result + "\n")

print("Test results saved to test_results.txt.")

