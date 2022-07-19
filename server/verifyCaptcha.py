import requests


"""
For more information: https://developers.google.com/recaptcha/docs/verify
"""
def verifyCaptcha(captchaToken):
    try:
        url = "https://www.google.com/recaptcha/api/siteverify"
        body = {
            "response": captchaToken,
            "secret": "6LcL0PUgAAAAABfygP8FblS7g97R96_zWdmS5aut",
        }

        x = requests.post(url, data=body)

        if x.status_code != 200:
            return False
        
        resp = x.json()

        return resp['success']
    except:
        return False
