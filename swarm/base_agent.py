import abc

class BaseAgent(abc.ABC):
    def __init__(self, name):
        self.name = name
    
    @abc.abstractmethod
    def run(self, data):
        pass

print("🤖 [SWARM] Motor de agentes inicializado. Arquitectura distribuida lista.")
