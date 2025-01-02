import json
from typing import Optional, Dict

from example_compliance_engine.compliance_engine import validator
from example_compliance_engine.compliance_engine.evaluate_compliance import check_compliance

if __name__ == "__main__":
    print("Example Compliance Engine")

    payload_no_compliance = {
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

    payload_compliance_one_vulnerability_critical = {
        "username": "test_user",
        "password": "test_passwrod",
        "it_contact": "it_contact",
        "vulnerabilidades": {
            "high": {
                "chess": "1"
            },
            "critical": {
            },
            "low": {
            }
        },
        "exceptions_app_rule": {"high": {"chess": {"version": 1}}}
    }

    payload_compliance_four_vulnerability_critical = {
        "username": "test_user",
        "password": "test_passwrod",
        "it_contact": "it_contact",
        "vulnerabilidades": {
            "high": {
                "chess": "1",
                "pokemon": 10,
                "office": 13,
                "kmspico": "x23"
            },
            "critical": {
            },
            "low": {
            }
        },
        "exceptions_app_rule": {"high": {"chess": {"version": 1}, "office": {"version": 100}}}
    }

    payload_compliance = {
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

    summary: Optional[Dict] = validator.handler(request=payload_compliance_four_vulnerability_critical)
    print(f"""
    {"-"*100}
    COMPLIANCE: {check_compliance(summary=summary)}
    PAYLOAD:
    {json.dumps(summary, indent=10)}
    {"-" * 100}
    """)