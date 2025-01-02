import json
from typing import Optional, Dict

from example_compliance_engine.compliance_engine import validator
from example_compliance_engine.compliance_engine.evaluate_compliance import check_compliance

if __name__ == "__main__":
    print("Example Compliance Engine")

    Payload_no_compliance = {
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

    Payload_compliance = {
        "username": "test_user",
        "password": "test_passwrod",
        "it_contact": "it_contact",
        "vulnerabilidades": {
            "high": {
            },
            "critical": {
            },
            "low": {
            }
        }
    }

    exception_app = {"chess"}

    summary: Optional[Dict] = validator.handler(request=Payload_no_compliance)
    print(f"""
    {"-"*100}
    COMPLIANCE: {check_compliance(summary=summary)}
    PAYLOAD: 
    {json.dumps(summary, indent=10)}
    {"-" * 100}
    """)