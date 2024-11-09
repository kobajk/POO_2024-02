from abc import ABC, abstractmethod
class AbstractOperation(ABC):
    @abstractmethod
    def request(self):
        pass

class RealOperation(AbstractOperation):
    def request(self):
        print("RealOperation: Processando request....")

class NullOperation(AbstractOperation):
    def request(self):
        print("NullOperation:Processando nada!!!")

class OperationFactory:
    def get_operation(self, type):
        if type == 'active':
            return RealOperation()
        elif type == 'null':
            return NullOperation()
        else:
            raise ValueError()

if __name__ == "__main__":
    factory = OperationFactory()
    operation = factory.get_operation("active")
    operation.request()