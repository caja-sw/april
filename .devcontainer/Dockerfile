FROM mcr.microsoft.com/devcontainers/python:3-trixie
USER vscode
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN echo 'alias dev="uv sync && uv run python manage.py migrate && uv run python manage.py runserver"' | tee -a ~/.bashrc ~/.zshrc
RUN echo 'alias mig="uv sync && uv run python manage.py makemigrations"' | tee -a ~/.bashrc ~/.zshrc
RUN echo 'alias res="rm -f db.sqlite3"' | tee -a ~/.bashrc ~/.zshrc
