from abc import ABC, abstractmethod

#component
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        raise NotImplementedError()

#leaf
class File(FileSystemComponent):
        def __init__(self, name:str)-> None:
             self.name = name

        def show_details(self)->None:
             print(f"File: {self.name}")

#composite
class Directory(FileSystemComponent):
    def __init__(self, name:str)->None:
          self.name = name
          self.components = []
    
    def add(self, component: FileSystemComponent)->None:
         self.components.append(component)

    def remove(self, component: FileSystemComponent)->None:
         self.components.remove(component)

    def show_details(self)->None:
         print(f"Directory:{self.name}")
         for component in self.components:
              component.show_details()

if __name__ == "__main__":
     file1 = File("arquivo_1.txt")
     file2 = File("arquivo_2.py")
     file3 = File("arquivo_3.pptx")
     dir_apres = Directory("Apresentações")
     dir_relat = Directory("Relatórios")
     dir_cod = Directory("Códigos")
     
     dir_apres.add(dir_relat)
     dir_relat.add(file1)
     dir_apres.add(file3)
     dir_cod.add(file2)

     root = Directory("root")
     root.add(dir_apres)
     root.add(dir_cod)

     root.show_details()