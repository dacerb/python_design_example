from .chain_handler import ChainHandler


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


class VulnerabilityCritical(ChainHandler):

    def handler(self,  request):
        try:
            critical_vulnerability = request.get("vulnerabilidades", {}).get("critical", {})
            if len(critical_vulnerability):
                print(f"critical_vulnerability: {len(critical_vulnerability)} is invalid")

        except Exception as e:
            print("problems with critical_vulnerability validation")
            raise e
        finally:
            if self._next_handler: self._next_handler.handler(request)


class VulnerabilityHigh(ChainHandler):

    def handler(self,  request):
        try:
            high_vulnerability = request.get("vulnerabilidades", {}).get("high", {})
            if len(high_vulnerability):
                print(f"high_vulnerability: {len(high_vulnerability)} is invalid")

        except Exception as e:
            print("problems with high_vulnerability validation")
            raise e
        finally:
            if self._next_handler: self._next_handler.handler(request)


class VulnerabilityLow(ChainHandler):

    def handler(self,  request):
        try:
            low_vulnerability = request.get("vulnerabilidades", {}).get("low", {})
            if len(low_vulnerability):
                print(f"low_vulnerability: {len(low_vulnerability)} is invalid")

        except Exception as e:
            print("problems with low_vulnerability validation")
            raise e
        finally:
            if self._next_handler: self._next_handler.handler(request)