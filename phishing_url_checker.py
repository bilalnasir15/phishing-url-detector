# phishing_url_checker.py

# List of blacklisted phishing domains (can be expanded)
blacklist = [
    "login-verify.com",
    "secure-update.net",
    "paypal-security-alert.net",
    "banking-access.net",
    "verify-account123.com"
]

# List of suspicious keywords often found in phishing URLs
suspicious_keywords = [
    "login", "verify", "secure", "update", "account",
    "paypal", "bank", "free", "gift", "offer", "password", "signin"
]

def check_blacklist(url):
    return any(domain in url for domain in blacklist)

def check_suspicious_keywords(url):
    return [word for word in suspicious_keywords if word in url]

def main():
    print("\n🔍 Phishing URL Detector")
    print("-----------------------------")
    url = input("Enter the URL to check: ").lower().strip()

    is_blacklisted = check_blacklist(url)
    found_keywords = check_suspicious_keywords(url)

    print("\n🔎 Analysis Result:")
    if is_blacklisted:
        print("🚫 ALERT: This URL is in the known phishing blacklist!")
    elif found_keywords:
        print(f"⚠️ WARNING: This URL contains suspicious keywords: {', '.join(found_keywords)}")
    else:
        print("✅ This URL seems safe, but always double-check before clicking.")

    print("\n🔐 Tip: Use 2FA and avoid clicking unknown or urgent links!")

if __name__ == "__main__":
    main()

