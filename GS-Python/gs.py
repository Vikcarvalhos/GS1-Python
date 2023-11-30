import random
import tkinter as tk

class Paciente:
    def __init__(self, nome):
        self.nome = nome
        self.frequencia_cardiaca = random.randint(40, 110)
        self.temperatura_corporal = random.uniform(33, 39)

class SistemaMonitoramento:
    def __init__(self):
        self.lista_pacientes = []
        self.criar_display()

    def criar_display(self):
        root = tk.Tk()
        labels = {}

        paciente_entry = tk.Entry(root)
        paciente_entry.pack()

        def add_patient():
            nome_paciente = paciente_entry.get()
            paciente = Paciente(nome_paciente)
            self.lista_pacientes.append(paciente)
            labels[paciente.nome] = tk.Label(root, text=f"{paciente.nome}: Frequência cardíaca {paciente.frequencia_cardiaca}, Temperatura {paciente.temperatura_corporal:.1f}")
            labels[paciente.nome].pack()

        def remove_patient():
            nome_paciente = paciente_entry.get()
            paciente = next((p for p in self.lista_pacientes if p.nome == nome_paciente), None)
            if paciente:
                self.lista_pacientes.remove(paciente)
                labels[paciente.nome].destroy()
                del labels[paciente.nome]

        add_button = tk.Button(root, text="Adicionar", command=add_patient)
        add_button.pack()

        remove_button = tk.Button(root, text="Remover", command=remove_patient)
        remove_button.pack()

        def get_priority(paciente):
            return abs(paciente.temperatura_corporal - 37)

        def atualizar_display():
            for paciente in self.lista_pacientes:
                paciente.frequencia_cardiaca = random.randint(40, 110)
                paciente.temperatura_corporal = random.uniform(33, 39)

                if paciente.frequencia_cardiaca > 100:
                    print(f"Taquicardia detectada para o paciente {paciente.nome}")
                elif paciente.frequencia_cardiaca < 50:
                    print(f"Braquicardia detectada para o paciente {paciente.nome}")

                if paciente.temperatura_corporal > 37.5:
                    print(f"Febre detectada para o paciente {paciente.nome}")
                elif paciente.temperatura_corporal < 35:
                    print(f"Hipotermia detectada para o paciente {paciente.nome}")

            self.lista_pacientes = sorted(self.lista_pacientes, key=get_priority, reverse=True)

            for i, paciente in enumerate(self.lista_pacientes):
                labels[paciente.nome]['text'] = f"{paciente.nome}: Frequência cardíaca {paciente.frequencia_cardiaca}, Temperatura {paciente.temperatura_corporal:.1f}, Prioridade {i+1}"

            root.after(10000, atualizar_display)

        atualizar_display()
        root.mainloop()

sistema = SistemaMonitoramento()
sistema.gerenciar_pacientes()
sistema.criar_display()
sistema.monitorar_pacientes()