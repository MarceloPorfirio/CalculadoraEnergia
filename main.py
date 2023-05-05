import tkinter as tk

# criar a janela da calculadora
janela = tk.Tk()
janela.title("Calculadora de Gastos de Energia Elétrica")
janela.geometry("400x250")

# criar a lista de aparelhos e seus respectivos consumos de energia em watts
aparelhos = {
    "Chuveiro": 7500,
    "Ar condicionado": 2000,
    "Geladeira": 150,
    "Televisão": 120,
    "Lâmpada": 60
}

def calcular_custo():
    # Obter os valores inseridos pelo usuário
    aparelho_selecionado = aparelho.get()
    tempo_uso = tempo.get()
    preco_energia_valor = preco_energia.get()

    # Verificar se o tempo de uso foi inserido
    if tempo_uso == '':
        resultado.configure(text="Por favor, informe o tempo de uso")
        return
    
    # Converter os valores para números
    tempo_uso = int(tempo_uso)
    preco_energia_valor = float(preco_energia_valor)

    # Fazer o cálculo do custo efetivo
    consumo_aparelho = aparelhos[aparelho_selecionado]
    consumo_total = consumo_aparelho * tempo_uso
    custo_efetivo = consumo_total * preco_energia_valor / 1000

    # Exibir o resultado na tela
    resultado.configure(text="Custo Efetivo: R$ {:.2f}".format(custo_efetivo))


# criar função para calcular o custo efetivo de energia elétrica de um aparelho
def calcular_custo_efetivo(tempo_uso, preco_energia, consumo_aparelho):
    calcular_custo()
    # converter tempo de uso de horas para minutos
    tempo_uso = int(tempo_uso) * 60
    # calcular a quantidade de energia consumida pelo aparelho em kWh
    energia_consumida = (consumo_aparelho * tempo_uso) / 1000
    # calcular o custo efetivo em reais
    custo_efetivo = energia_consumida * preco_energia
    return round(custo_efetivo, 2)

# criar função para atualizar o resultado do custo efetivo na tela da calculadora
def atualizar_resultado(*args):
    # obter o aparelho selecionado e o tempo de uso informado pelo usuário
    aparelho_selecionado = aparelho.get()
    tempo_uso = tempo.get()
    # calcular o custo efetivo de energia elétrica
    custo_efetivo = calcular_custo_efetivo(tempo_uso, preco_energia, aparelhos[aparelho_selecionado])
    # atualizar o resultado na tela da calculadora
    resultado.config(text="Custo Efetivo: R$ {} em {} horas.".format(custo_efetivo,tempo_uso))


# criar os widgets da interface gráfica da calculadora
aparelho_label = tk.Label(janela, text="Selecione o aparelho:")
aparelho_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
aparelho = tk.StringVar(janela)
aparelho.set(list(aparelhos.keys())[0])
aparelho_menu = tk.OptionMenu(janela, aparelho, *aparelhos.keys(), command=atualizar_resultado)
aparelho_menu.grid(row=0, column=1, padx=10, pady=10)
tempo_label = tk.Label(janela, text="Informe o tempo de uso (horas):")
tempo_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
tempo = tk.Entry(janela)
tempo.grid(row=1, column=1, padx=10, pady=10)
tempo.bind("<KeyRelease>", atualizar_resultado)
preco_label = tk.Label(janela, text="Informe o preço da energia (R$/kWh):")
preco_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
preco_energia = tk.Entry(janela)
preco_energia.insert(0, "0.8")
preco_energia.grid(row=2, column=1, padx=10, pady=10)
preco_energia.bind("<KeyRelease>", atualizar_resultado)
resultado = tk.Label(janela, text="Custo Efetivo: R$ 0.00")
resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


janela.mainloop()