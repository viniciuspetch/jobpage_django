O que foi desenvolvido:
- One-page para a coleta de candidaturas para uma vaga de emprego
- Páginas de login e administração para listar os candidatos
- Sistema manual de e-mail, que notifica quantos candidatos se inscreveram no dia
- Bot de Telegram que retorna o número de candidatos no dia, e o e-mai dos três últimos

O que foi utilizado:
- HTML5, CSS e Bootstrap para o front-end
- Django, PostgreSQL para o back-end
- Docker para a conteinerização do PostgreSQl e pgAdmin
- Biblioteca python-telegram-bot para o desenvolvimento do bot

Como rodar:
- Fazer o download do Django e desse repositório
- Instalar a biblioteca 'python-telegram-bot': https://python-telegram-bot.org/
- Instalar e configurar para o seu banco de dados da sua escolha
    - Caso o SQLite seja utilizado, é necessário apenas resetar as configurações de DB do Django para as padrões, e em seguida rodar makemigrations e migrate.
    - Caso o PostgreSQL seja utilizado, necessário apenas atualizar/utilizar as configurações em settings.py. Por padrão, foi utilizado um banco de dados nomeado 'postgres', com usuário 'postgres' e senha 'pass', no IP 192.168.1.33:5432.

Comandos:
- Mandar e-mail: python manage.py scheduled_email
- Inicializar o telegram bot: python manage.py vagasrits

# Página principal
O site consiste de três páginas, sendo apenas uma feita para ser visualizada pelos candidatos. Foi utilizado o framework Django e seguido o modelo de organização do mesmo. Como camada de "modelo", foi utilizado o sistema de Models do framework, definindo então no arquivo models.py o modelo Candidate, responsável por guardar as informações dos candidatos.

Na camada de "visão" foram implementados as páginas de candidatura e a do administrador. Para a página principal foi utilizado apenas uma rota para a requisição da página e o método POST. Ao receber o POST, os dados recebidos são validados, e caso não estejam corretos a página principal é retornada com os devidos alertas de erro ao usuário.

No front-end, o Django monta as páginas utilizando templates e ModelForm. Assim, é possível realizar algumas alterações na página de maneira simples, e graças ao ModelForm é possível reutilizar o Model criado para os candidatos para então gerar automaticamente os campos do formulário a ser preenchido. Para auxiliar na montagem da página, foi utilizado o bootstrap, tanto em questão da organização dos elementos quanto em elementos visuais.

# Sistema de e-mail
O fato do desenvolvimento ter sido feito no Windows dificultou a automação do envio de e-mails, sendo implementada apenas a etapa manual, que consiste da implementação de um management command e uma função interna para o envio de e-mails. Como não houve acesso à um servidor de e-mails propriamente dito, o Django foi configurado para que todo e-mail enviado fosse mostrado no terminal do servidor.

A função implementada (que pode ser chamada pelo comando 'python manage.py scheduled_email), envia um e-mail para o e-mail user@gmail.com notificando de quantos usuários se cadastraram no dia.

# Bot Telegram
Foi desenvolvido um bot para o Telegram, acoplado ao app responsável pelo site, que responde com a quantidade de candidatos inscritos até o momento, e o e-mail dos três últimos. Do lado do servidor, o bot pode ser chamado pelo comando 'python manage.py vagasrits'. Do lado do usuário, o bot pode ser utilizado mandando a mensagem /VagasRits para @ritsvagasbot.