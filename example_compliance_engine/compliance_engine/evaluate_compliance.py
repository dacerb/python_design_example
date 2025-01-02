


def check_compliance(summary):
    return all(handler.get("compliance", False) for handler in summary.values())