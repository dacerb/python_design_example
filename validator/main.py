from chain_builder import validator


Payload = {
    "username": "test_user",
    "password": "test_passwrod",
    "it_contact": "it_contact",
    "vulnerabilidades": {
        "high": {
            "winchot": "v1",
            "office": "2023"
        },
        "critical": {
            "firefox": "99"
        },
        "low": {
            "chess": "x1"
        }
    }
}


if __name__ == "__main__":
    validator.handler(request=Payload)