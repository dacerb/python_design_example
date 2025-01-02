from example_compliance_engine.compliance_engine.chain_handler import ChainHandler


class UsernameHandler(ChainHandler):

    def handler(self,  request):
        try:
            username = request.get("username", None)
            assert isinstance(username, str), "the username must be a str"
            print(f"username: {username} is valid")
        except Exception as e:
            print("problems with username validation")
            raise e
        finally:
            if self._next_handler: self._next_handler.handler(request)
