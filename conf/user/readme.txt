Para que alguns serviços configurados possam funcionar no ambiente de cada
cada desenvolvedor é necessário que informações pessoais não sejam
sincronizadas.

Crie um arquivo setup.py na pasta user e adicione o seguinte conteudo:

working_paramters = {
    "project_key": "6710fa297eff32b07de4",
    "user_key": "{{ chave de usuario }}",
    "task": "{{ numero da tarefa }}"
}

Atualize o numero da tarefa de acordo com a tarefa que estiver executando.