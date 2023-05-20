from abc import ABC, abstractmethod


class _Field(ABC):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @value.setter
    @abstractmethod
    def value(self, value):
        raise NotImplementedError


class BaseRecordStorage(ABC):
    @abstractmethod
    def add_record(self, record):
        raise NotImplementedError

    @abstractmethod
    def del_record(self, name=None):
        raise NotImplementedError

    @abstractmethod
    def show_records(self):
        raise NotImplementedError

    @abstractmethod
    def search(self, query):
        raise NotImplementedError
