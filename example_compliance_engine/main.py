from example_compliance_engine.compliance_engine import validator

if __name__ == "__main__":
    print("Example Compliance Engine")
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
    validator.handler(request=Payload)