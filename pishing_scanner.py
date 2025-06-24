import urllib.parse

# List of suspicious URL shorteners
shorteners = ['bit.ly', 'tinyurl.com', 'rb.gy', 'goo.gl']

# List of suspicious TLDs (blacklisted extensions)
blacklist = ['gq', 'tk', 'ml', 'ga', 'cf']

def analyze_url(url):
    # Parse the URL
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    scheme = parsed.scheme
    path = parsed.path

    print("\n=== URL Analysis ===")
    print(f"Full URL: {url}")
    print(f"Protocol: {scheme}")
    print(f"Domain: {domain}")
    print(f"Path: {path}")

    # Check if the domain is a known shortener
    if domain in shorteners:
        print("⚠️ This is a shortened URL (possibly malicious)")

    # Check for subdomains (possible obfuscation)
    parts = domain.split('.')
    if len(parts) > 2:
        print("⚠️ Contains a subdomain (may be deceptive)")

    # Check if TLD is blacklisted
    ext = parts[-1]
    if ext in blacklist:
        print(f"❌ The domain extension ({ext}) is suspicious and often used in phishing")

    print("✅ Initial analysis completed.\n")

# Run the tool
url = input("🔗 Enter the URL to analyze: ")
analyze_url(url)