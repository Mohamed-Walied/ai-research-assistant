class PromptRenderer:
    """
    Renders prompt templates.
    """

    def render(
        self,
        template: str,
        **variables,
    ) -> str:
        """
        Replace placeholders with variables.
        """

        return template.format(**variables)