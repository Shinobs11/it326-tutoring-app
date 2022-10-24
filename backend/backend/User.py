from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self):
        print("NULL")
    @abstractmethod
    def foo(self):
        pass