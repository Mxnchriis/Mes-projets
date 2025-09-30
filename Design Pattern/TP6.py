from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Command():

    def __init__(self, command: command) -> None:
        self._command = command


    def command(self) -> None:

        return self._command
    
    def command(self, command: command) -> None:

        self._command = command
    
    def do_some_business_logic(self) -> None:

        print("Command: Sorting data using the command (not sure how it'll do it)")
        result = self._command.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

class command(ABC):

    @abstractmethod
    def do_algorithm(self, data: List[str]) -> List[str]:
        pass

class PlayCommand(command):

    def do_algorithm(self, data: List[str]) -> List[str]:
        return sorted(data)
    
class PauseCommand(command):

    def do_algorithm(self, data: List[str]) -> List[str]:
        return reversed(sorted(data))
    
class StopCommand(command):

    def do_algorithm(self, data: List[str]) -> List[str]:
        return sorted(data, key=len)
    
if __name__ == "__main__":
    Command = Command(PlayCommand())
    print("Client: Strategy is set to normal sorting.")
    Command.do_some_business_logic()

    print("\nClient: Strategy is set to reverse sorting.")
    Command.command(PauseCommand())
    Command.do_some_business_logic()

    print("\nClient: Strategy is set to length sorting.")
    Command.command(StopCommand())
    Command.do_some_business_logic()