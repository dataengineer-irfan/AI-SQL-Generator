from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        temperature: float = 0.0
    ) -> str:
        """
        Generate a response from an LLM.
        """
        raise NotImplementedError