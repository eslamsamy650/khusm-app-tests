import requests

def fetch_otp(phone_number, lang="en"):
    url = "https://khusm-api.mediconsulteg.com/api/Auth/GetOtpMember"
    params = {
        "phone": phone_number,
        "lang": lang
    }
    try:
        response = requests.get(url, params=params)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        response.raise_for_status()
        
        otp = response.json().get("otp")
        return otp
    except Exception as e:
        print(f"Failed to fetch OTP: {e}")
        return None

