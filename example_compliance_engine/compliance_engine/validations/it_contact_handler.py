from example_compliance_engine.compliance_engine.chain_handler import ChainHandler


class ItContactHandler(ChainHandler):

    def handler(self,  request):
        try:
            it_contact = request.get("it_contact", None)
            assert isinstance(it_contact, str), "the it_contact must be a str"
            print(f"it_contact: {it_contact} is valid")

        except Exception as e:
            print("problems with it_contact validation")
            raise e
        finally:
            if self._next_handler: self._next_handler.handler(request)
