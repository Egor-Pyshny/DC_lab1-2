from abc import ABC, abstractmethod


class RepositoryBase(ABC):
    @abstractmethod
    def get_all(self):
        """return all elements"""

    @abstractmethod
    def get(self, id):
        """return 1 element bu id"""

    @abstractmethod
    def create(self, item):
        """create element"""

    @abstractmethod
    def update(self, item):
        """update element"""

    @abstractmethod
    def delete(self, id):
        """delete element"""
