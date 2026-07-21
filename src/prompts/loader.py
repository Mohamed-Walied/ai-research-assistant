from pathlib import Path


class PromptLoader:
    """
    Loads prompt templates from the templates directory.
    """

    def __init__(self):
        self.template_dir = Path(__file__).parent / "templates"

    def load(self, template_name: str) -> str:
        """
        Load a template file.

        Example:
            load("summary")

        Looks for:
            templates/summary.md
        """

        file_path = self.template_dir / f"{template_name}.md"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Prompt template '{template_name}' not found."
            )

        return file_path.read_text(encoding="utf-8")