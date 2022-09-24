installs setup.py in development mode
pip install --editable .

Run all tests including pylint/black/isort/mypy
pytest --pylint --black --isort --mypy --cache-clear -v


.vscode\settings.json
{
    "python.formatting.provider": "black",
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "python.analysis.indexing": true,
}
