import abc


class DbInterface(abc.ABC):
    @abc.abstractmethod
    def init(self, with_demo: bool = False) -> None:
        pass

    @abc.abstractmethod
    def connect(self) -> None:
        pass

    @abc.abstractmethod
    def disconnect(self) -> None:
        pass
