from .loader import PromptLoader
from .renderer import PromptRenderer


class PromptManager:
    """
    Main interface for working with prompts.
    """

    def __init__(self):
        self.loader = PromptLoader()
        self.renderer = PromptRenderer()

    def render(
        self,
        template_name: str,
        **variables,
    ) -> str:
        """
        Load and render a prompt template.
        """

        template = self.loader.load(template_name)

        return self.renderer.render(
            template,
            **variables,
        )