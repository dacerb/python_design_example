from abc import ABC, abstractmethod
from typing import Self, Optional, AnyStr

from dataclasses import dataclass


@dataclass
class ChainHandler(ABC):
    _next_handler: Optional[Self] = None
    summary_body = None
    def set_next(self, handler: Self):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handler(self,  request):...


@dataclass
class HandlerSummaryProtocol(ABC):
    detail: Optional[AnyStr] = ""
    compliance: Optional[bool] = None

    @property
    def to_json(self):
        return self.__dict__


class HandlerSummaryVulnerabilityProtocol(HandlerSummaryProtocol):
    qty: int
    vulnerability_list: list = []