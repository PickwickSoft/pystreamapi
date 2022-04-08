from typing import List

from pystreamapi.lazy.process import Process


class ProcessQueue:

    def __init__(self):
        self.__queue: List[Process] = []

    def append(self, proc: Process, index=-1):
        self.__queue.insert(index, proc)

    def execute_all(self):
        for proc in self.__queue:
            proc.exec()

    def get_queue(self) -> List[Process]:
        return self.__queue
