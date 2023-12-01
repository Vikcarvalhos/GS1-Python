import random
import tkinter as tk

class Paciente:
    def __init__(self, nome):
        # Inicializa um objeto Paciente com um nome e valores aleatórios para frequência cardíaca e temperatura corporal
        self.nome = nome
        self.frequencia_cardiaca = random.randint(40, 110)
        self.temperatura_corporal = random.uniform(33, 39)

class SistemaMonitoramento:
    def __init__(self):
        # Inicializa o sistema de monitoramento
        self.lista_pacientes = []  # Lista para armazenar os pacientes
        self.criar_display()  # Chama o método para criar a interface gráfica

    def criar_display(self):
        # Cria a interface gráfica usando Tkinter
        root = tk.Tk()
        labels = {}  # Dicionário para armazenar os labels dos pacientes

        paciente_entry = tk.Entry(root)  # Campo de entrada para adicionar pacientes
        paciente_entry.pack()

        def add_patient():
            # Função para adicionar pacientes à lista e exibir na interface
            nome_paciente = paciente_entry.get()
            paciente = Paciente(nome_paciente)
            self.lista_pacientes.append(paciente)
            # Cria um label para o paciente e o exibe na interface
            labels[paciente.nome] = tk.Label(root, text=f"{paciente.nome}: Frequência cardíaca {paciente.frequencia_cardiaca}, Temperatura {paciente.temperatura_corporal:.1f}")
            labels[paciente.nome].pack()

        def remove_patient():
            # Função para remover pacientes da lista e da interface
            nome_paciente = paciente_entry.get()
            paciente = next((p for p in self.lista_pacientes if p.nome == nome_paciente), None)
            if paciente:
                self.lista_pacientes.remove(paciente)
                # Remove o label do paciente da interface
                labels[paciente.nome].destroy()
                del labels[paciente.nome]

        add_button = tk.Button(root, text="Adicionar", command=add_patient)  # Botão para adicionar pacientes
        add_button.pack()

        remove_button = tk.Button(root, text="Remover", command=remove_patient)  # Botão para remover pacientes
        remove_button.pack()

        def get_priority(paciente):
            # Função para determinar a prioridade com base na diferença entre a temperatura atual e a temperatura ideal (37 graus)
            return abs(paciente.temperatura_corporal - 37)

        def atualizar_display():
            # Função para atualizar dinamicamente as informações dos pacientes na interface
            for paciente in self.lista_pacientes:
                # Atualiza os valores de frequência cardíaca e temperatura para cada paciente
                paciente.frequencia_cardiaca = random.randint(40, 110)
                paciente.temperatura_corporal = random.uniform(33, 39)

                # Verifica as condições de saúde do paciente e exibe mensagens no console se forem detectadas
                if paciente.frequencia_cardiaca > 100:
                    print(f"Taquicardia detectada para o paciente {paciente.nome}")
                elif paciente.frequencia_cardiaca < 50:
                    print(f"Braquicardia detectada para o paciente {paciente.nome}")

                if paciente.temperatura_corporal > 37.5:
                    print(f"Febre detectada para o paciente {paciente.nome}")
                elif paciente.temperatura_corporal < 35:
                    print(f"Hipotermia detectada para o paciente {paciente.nome}")

            # Ordena a lista de pacientes com base na prioridade calculada e atualiza os labels na interface
            self.lista_pacientes = sorted(self.lista_pacientes, key=get_priority, reverse=True)

            for i, paciente in enumerate(self.lista_pacientes):
                # Atualiza o label do paciente na interface com suas informações atualizadas e prioridade
                labels[paciente.nome]['text'] = f"{paciente.nome}: Frequência cardíaca {paciente.frequencia_cardiaca}, Temperatura {paciente.temperatura_corporal:.1f}, Prioridade {i+1}"

            root.after(10000, atualizar_display)  # Chama a função atualizar_display após 10 segundos

        atualizar_display()  # Inicia o processo de atualização dinâmica
        root.mainloop()  # Inicia a interface gráfica

sistema = SistemaMonitoramento()  # Cria uma instância do Sistema de Monitoramento
