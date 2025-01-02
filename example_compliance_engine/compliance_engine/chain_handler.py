from abc import ABC, abstractmethod
from typing import Self, Optional

from dataclasses import dataclass


@dataclass
class ChainHandler(ABC):
    _next_handler: Optional[Self] = None

    def set_next(self, handler: Self):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handler(self,  request):...