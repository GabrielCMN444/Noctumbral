# Noctumbral

Noctumbral — Forensic Assistant in the Shadows.  

Uma ferramenta de análise forense digital inspirada em estética noir, projetada para investigação, organização e geração de relatórios de casos. Permite criar casos, adicionar evidências e notas, gerar relatórios automáticos e listar todos os casos de forma prática e intuitiva.

---

## Funcionalidades

- **Criar casos**: organize investigações em pastas separadas.
- **Adicionar evidências**: suporte a arquivos de qualquer tipo.
- **Adicionar notas**: registre observações importantes sobre suspeitos ou eventos.
- **Gerar relatórios**: crie relatórios Markdown automaticamente.
- **Listar casos existentes**: mantenha controle de todas as investigações.
- **Informações do Noctumbral**: saiba mais sobre a ferramenta e suas capacidades.

---

## Instalação

> Recomendado criar um ambiente virtual Python:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows



Instale dependências:

pip install -r requirements.txt
pip install -e .




Uso Básico

Criar um caso:

noctumbral new "nome-do-caso"


Adicionar evidência:

noctumbral add "nome-do-caso" "/caminho/para/evidencia.png"


Adicionar nota:

noctumbral add "nome-do-caso" --note "Observação relevante"


Gerar relatório:

noctumbral report "nome-do-caso"


Listar todos os casos:

noctumbral cases


Informações sobre a ferramenta:

noctumbral about




Estrutura de Pastas
noctumbral/
├── cases/           # Casos criados com evidências, notas e relatórios
├── core/            # Lógica principal da ferramenta
├── tests/           # Testes da aplicação
├── pyproject.toml   # Configuração do projeto Python
├── README.md        # Este arquivo
└── main.py          # Entry point da CLI





