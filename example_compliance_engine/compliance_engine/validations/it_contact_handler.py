from typing import Optional, Dict, AnyStr

from example_compliance_engine.compliance_engine.chain_handler import ChainHandler, HandlerSummaryProtocol

class ItContactHandler(ChainHandler):
    def handler(self, request):

        self.summary_body: HandlerSummaryProtocol = HandlerSummaryProtocol()
        key_class: Optional[AnyStr] = self.__class__.__name__
        summary: Optional[Dict] = {}

        try:
            self.process(request)

        except Exception as e:
            print(f"problems with {key_class} validation")
            raise e

        finally:
            summary[key_class]: dict = self.summary_body.to_json

        if self._next_handler:
            result_summary = self._next_handler.handler(request)
            summary.update(result_summary)

        return summary

    def process(self, request) -> None:
        it_contact = request.get("it_contact", None)
        assert isinstance(it_contact, str), "the it_contact must be a str"

        self.summary_body.compliance = True
        self.summary_body.detail = f"it_contact: {it_contact} is valid"