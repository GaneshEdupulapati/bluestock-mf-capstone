import requests

amfi_codes = [
    125497,
    119551,
    120503,
    118632,
    120841
]

for code in amfi_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("=" * 60)
        print("AMFI Code :", code)
        print("Scheme    :", data["meta"]["scheme_name"])
        print("Latest NAV:", data["data"][0]["nav"])
        print("Date      :", data["data"][0]["date"])
    else:
        print(f"Failed to fetch data for {code}")