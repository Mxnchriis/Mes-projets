from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():

    def __init__(self, tri: tri) -> None:
        self._tri = tri


    def tri(self) -> None:

        return self._tri
    
    def tri(self, tri: tri) -> None:

        self._tri = tri
    
    def do_some_business_logic(self) -> None:

        print("Context: Sorting data using the tri (not sure how it'll do it)")
        result = self._tri.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

class tri(ABC):

    @abstractmethod
    def do_algorithm(self, data: List[str]) -> List[str]:
        pass

class TriCroissant(tri):

    def do_algorithm(self, data: List[str]) -> List[str]:
        return sorted(data)
    
class TriD_Corissant(tri):

    def do_algorithm(self, data: List[str]) -> List[str]:
        return reversed(sorted(data))
    
class TriParLongueur(tri):

    def do_algorithm(self, data: List[str]) -> List[str]:
        return sorted(data, key=len)
    
if __name__ == "__main__":
    context = Context(TriCroissant())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()

    print("\nClient: Strategy is set to reverse sorting.")
    context.tri(TriD_Corissant())
    context.do_some_business_logic()

    print("\nClient: Strategy is set to length sorting.")
    context.tri(TriParLongueur())
    context.do_some_business_logic()