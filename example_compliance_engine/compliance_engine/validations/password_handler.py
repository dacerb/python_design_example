from typing import Optional, Dict, AnyStr

from example_compliance_engine.compliance_engine.chain_handler import ChainHandler


class PasswordHandler(ChainHandler):
    def handler(self,  request):
        key_class: Optional[AnyStr] = self.__class__.__name__
        summary: Optional[Dict] = {}
        try:
            password = request.get("password", None)

            assert isinstance(password, str), "the password must be a str"
            summary[key_class]: AnyStr =  f"password: {password} is valid"

        except Exception as e:
            print("problems with password validation")
            raise e

        if self._next_handler:
            result_summary = self._next_handler.handler(request)
            summary.update(result_summary)

            return summary