import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_linkedin():
    solution = capsolver.solve({
    "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://iframe.arkoselabs.com",
        "websitePublicKey": "3117BF26-4762-4F5A-8ED9-A85E69209A46",
        "funcaptchaApiJSSubdomain": "https://client-api.arkoselabs.com",
        "data": "{\"blob\":\"Obtain this value, it's required and it's different each time.\"}"
    })
    return solution

def main():
    
    print("Solving linkedin captcha")
    solution = solve_funcaptcha_linkedin()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
