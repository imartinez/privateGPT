from llama_index.llms.ollama import Ollama
from pydantic import Field


class CustomOllama(Ollama):
    """Custom Ollama class to fill in "keep_alive" when sending requests."""

    keep_alive: str = Field(
        default="5m",
        description="String that describes the time the model should stay in (V)RAM after last request.",
    )

    def __init__(self, *args, **kwargs) -> None:
        # fetch keep_alive from kwargs or use 5m if not found.
        keep_alive = kwargs.pop("keep_alive", "5m")
        super().__init__(*args, **kwargs)
        self.keep_alive = keep_alive

    def chat(self, *args, **kwargs):
        kwargs["keep_alive"] = self.keep_alive
        return super().chat(*args, **kwargs)

    def stream_chat(self, *args, **kwargs):
        kwargs["keep_alive"] = self.keep_alive
        return super().stream_chat(*args, **kwargs)

    def complete(self, *args, **kwargs):
        kwargs["keep_alive"] = self.keep_alive
        return super().complete(*args, **kwargs)

    def stream_complete(self, *args, **kwargs):
        kwargs["keep_alive"] = self.keep_alive
        return super().stream_complete(*args, **kwargs)
