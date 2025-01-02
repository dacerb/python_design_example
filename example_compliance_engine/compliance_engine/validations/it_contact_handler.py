from typing import Optional, Dict, AnyStr

from example_compliance_engine.compliance_engine.chain_handler import ChainHandler

class ItContactHandler(ChainHandler):
    def handler(self,  request):
        key_class: Optional[AnyStr] = self.__class__.__name__
        summary: Optional[Dict] = {}
        try:
            it_contact = request.get("it_contact", None)

            assert isinstance(it_contact, str), "the it_contact must be a str"
            summary[key_class]: AnyStr = f"it_contact: {it_contact} is valid"

        except Exception as e:
            print("problems with it_contact validation")
            raise e

        if self._next_handler:
            result_summary = self._next_handler.handler(request)
            summary.update(result_summary)

        return summary