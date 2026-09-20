# autenticacao_python

# 1. Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Instalar dependencias
pip install fastapi "uvicorn[standard]" \
            "python-jose[cryptography]" \
            "passlib[bcrypt]" python-multipart

# 3. Congelar versoes
pip freeze > requirements.txt

# 4. Subir o servidor (arquivo main.py ainda vazio)
uvicorn main:app --reload
