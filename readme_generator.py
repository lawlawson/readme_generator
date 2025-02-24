from InquirerPy import prompt
from rich.console import Console
from rich.text import Text

console = Console()

questions = [
    {"type": "input", "name": "title", "message": "Enter the project title:"},
    {"type": "input", "name": "description", "message": "Enter the project description:"},
    {"type": "input", "name": "installation", "message": "Enter installation instructions:"},
    {"type": "input", "name": "usage", "message": "Enter usage instructions:"},
    {"type": "list", "name": "license", "message": "Select a license:", "choices": [
        "MIT License",
        "Apache License 2.0",
        "GNU General Public License (GPL v3)",
        "GNU Lesser General Public License (LGPL v3)",
        "Mozilla Public License 2.0",
        "Creative Commons (CC0, CC BY, etc.)",
        "Unlicense"
    ]},
    {"type": "input", "name": "author", "message": "Enter author/contact information:"}
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

console.print(Text("\n[bold green]README.md successfully created![/bold green]"))
