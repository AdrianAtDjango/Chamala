<h1>🟣🔴🟡🟢 Chamalá - O Seu Sistema de Chamados!</h1>
Chamalá é um sistema simples de gerenciamento de chamados desenvolvido com Django. Ele permite que usuários criem, acompanhem e administrem chamados de suporte de maneira eficiente e organizada.

<h2>📦 Funcionalidades</h2>
<ul>
  <li>Cadastro e autenticação de usuários</li>
  <li>Criação e edição de chamados</li>
  <li>Definição de status e prioridade dos chamados</li>
  <li>Sistema de níveis de acesso (usuário/admin)</li>
  <li>Listagem e filtro de chamados</li>
  <li>Marcar chamados como favoritos</li>
  <li>Interface de administração Django customizada</li>
</ul>

<h2>⚙️ Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.13+</li>
  <li>Django</li>
  <li>SQLite (como banco de dados padrão)</li>
  <li>HTML/CSS (com Django templates)</li>
</ul>

<h2>🚀 Como executar o projeto</h2>
<ol>
  <li>Clone o repositório:</li>
  
    git clone https://github.com/seu-usuario/chamala.git
    cd chamala/suporte
    
  <li>Crie e ative um ambiente virtual:</li>
  
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

  <li>Aplique as migrações:</li>
  
    python manage.py migrate
    # faz as migrações das models

  <li>Execute o servidor de desenvolvimento:</li>

    python manage.py runserver
    # roda o servidor da aplicação

  <li>Acesse o sistema:</li>
    <ul>
      <li>Interface de uso: http://127.0.0.1:8000</li>
      <li>Admin Django: http://127.0.0.1:8000/admin</li>
    </ul>
</ol>

<h2>🗃️ Estrutura do Projeto</h2>

    suporte/
    ├── chamados/         # Aplicação principal
    │   ├── admin.py
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   └── urls.py
    ├── db.sqlite3        # Banco de dados local
    └── manage.py         # Comando de gerenciamento do Django`

<h2>📌 Notas</h2>
<ul>
  <li>O projeto já inclui o banco de dados db.sqlite3. Você pode apagá-lo e recriar se quiser começar do zero.</li>
  <li>Caso deseje customizar os níveis de usuário, veja o campo nivelUser no model User.</li>
</ul>
