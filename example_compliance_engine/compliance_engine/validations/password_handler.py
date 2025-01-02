from example_compliance_engine.compliance_engine.chain_handler import ChainHandler


class PasswordHandler(ChainHandler):

    def handler(self,  request):
        try:
            password = request.get("password", None)
            assert isinstance(password, str), "the password must be a str"
            print(f"password: {password} is valid")

        except Exception as e:
            print("problems with password validation")
            raise e
        finally:
            if self._next_handler: self._next_handler.handler(request)
