from typing import List
from typing import Optional

from groq import Groq

from config.settings import settings
from providers.base_provider import LLMProvider


class GroqProvider(LLMProvider):
    """
    Enterprise Groq Provider

    Primary:
        qwen/qwen3-32b

    Fallback:
        qwen/qwen3-14b

    Fallback:
        qwen/qwen3-8b
    """

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.models: List[str] = [
            settings.DEFAULT_MODEL,
            settings.FALLBACK_MODEL_1,
            settings.FALLBACK_MODEL_2
        ]

    def _clean_response(
        self,
        content: Optional[str]
    ) -> str:
        """
        Remove Qwen reasoning traces.

        Example:

        <think>
        reasoning...
        </think>

        SELECT ...
        """

        if not content:
            return ""

        content = content.strip()

        if "</think>" in content:
            content = content.split("</think>")[-1].strip()

        content = content.replace("<think>", "")
        content = content.replace("</think>", "")

        return content.strip()

    def generate(
        self,
        prompt: str,
        temperature: float = 0.0
    ) -> str:

        last_exception = None

        for model in self.models:

            try:

                response = self.client.chat.completions.create(
                    model=model,
                    temperature=temperature,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an enterprise Oracle SQL generation engine. "
                                "Do not reveal chain of thought. "
                                "Do not output reasoning. "
                                "Do not output analysis. "
                                "Return only the final answer."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                content = response.choices[0].message.content

                return self._clean_response(content)

            except Exception as ex:
                last_exception = ex
                continue

        raise RuntimeError(
            f"All Groq models failed. Last error: {last_exception}"
        )

    def health_check(self) -> bool:
        """
        Verify Groq connectivity.
        """

        try:

            result = self.generate(
                "Reply with exactly: QWEN3_READY"
            )

            return "QWEN3_READY" in result

        except Exception:
            return False