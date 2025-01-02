from typing import Optional, Dict, AnyStr

from example_compliance_engine.compliance_engine.chain_handler import ChainHandler


class UsernameHandler(ChainHandler):
    def handler(self,  request):
        key_class: Optional[AnyStr] = self.__class__.__name__
        summary: Optional[Dict] = {}
        try:
            username = request.get("username", None)

            assert isinstance(username, str), "the username must be a str"
            summary[key_class]: AnyStr = f"username: {username} is valid"

        except Exception as e:
            print("problems with username validation")
            raise e

        if self._next_handler:
            result_summary = self._next_handler.handler(request)
            summary.update(result_summary)

        return summary