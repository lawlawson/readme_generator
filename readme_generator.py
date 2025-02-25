from InquirerPy import prompt # type: ignore
from rich.console import Console # type: ignore
from rich.text import Text # type: ignore

console = Console()

questions = [
    {"type": "input", "name": "title", "message": "Enter a Project Title:"},
    {"type": "input", "name": "description", "message": "Enter a Project Description:"},
    {"type": "input", "name": "installation", "message": "Enter installation instructions:"},
    {"type": "input", "name": "usage", "message": "Enter usage instructions:"},
    {"type": "list", "name": "license", "message": "Select a license from the list:", "choices": [
        "MIT License",
        "Apache License 2.0",
        "GNU General Public License (GPL v3)",
        "GNU Lesser General Public License (LGPL v3)",
        "Mozilla Public License 2.0",
        "Creative Commons (CC0, CC BY, etc.)",
        "Unlicense"
    ]},
    {"type": "input", "name": "author", "message": "Enter Contact/Author information:"}
]

console.print(Text("\n[bold cyan]Project README Generator[/bold cyan]"))
console.print("Answer the following questions to generate a README.md file:\n")

answers = prompt(questions)

readme_content = f"""# {answers['title']}

## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
This project is licensed under the {answers['license']}.

## Author
{answers['author']}
"""

with open("README.md", "w") as file:
    file.write(readme_content)

console.print(("\n[bold green]README.md successfully created![/bold green]"))
