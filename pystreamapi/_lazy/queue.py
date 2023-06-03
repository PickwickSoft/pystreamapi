from typing import List

from pystreamapi._lazy.process import Process


class ProcessQueue:
    """A Queue for processes"""

    def __init__(self):
        self.__queue: List[Process] = []

    def append(self, proc: Process):
        """
        Add a new Process to the queue
        :param proc:
        """
        self.__queue.append(proc)

    def execute_all(self):
        """Run all processes from the queue"""
        for proc in self.__queue:
            proc.exec()

    def get_queue(self) -> List[Process]:
        """Get a list of the processes"""
        return self.__queue
