
from dataclasses import dataclass
from .validations import (
    VulnerabilityLow,
    VulnerabilityHigh,
    VulnerabilityCritical,
    ItContactHandler,
    PasswordHandler,
    UsernameHandler
)

@dataclass
class ValidatorChainBuilder:
    _head = None
    _current = None

    def add_handler(self, handler):
        if self._head is None:
            self._head = handler
            self._current = handler
        else:
            self._current = self._current.set_next(handler)
        return self

    def build(self):
        return self._head


builder_validator_chain = ValidatorChainBuilder()
validator = (
    builder_validator_chain
    .add_handler(UsernameHandler())
    .add_handler(PasswordHandler())
    .add_handler(ItContactHandler())
    .add_handler(VulnerabilityCritical())
    .add_handler(VulnerabilityHigh())
    .add_handler(VulnerabilityLow())
    .build()
)