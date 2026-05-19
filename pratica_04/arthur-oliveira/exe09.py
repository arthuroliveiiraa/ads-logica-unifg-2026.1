tarefas = []

tarefas.append("estudar Python")
tarefas.append("resolver exercícios")
tarefas.append("revisar código")
tarefas.append("enviar atividade")

tarefas.append("assistir videoaula")

print("Tarefas cadastradas:")
for tarefa in tarefas:
    print(f"  - {tarefa}")

print(f"Total: {len(tarefas)} tarefas")