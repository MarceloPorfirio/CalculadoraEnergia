import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dicionário com a potência em watts de cada aparelho doméstico
aparelhos = {
    'Geladeira': 150,
    'Televisão': 100,
    'Lâmpada': 60,
    'Ar Condicionado': 2000,
    'Ferro de Passar': 1000,
    'Chuveiro Elétrico': 7500
}

# Configurações de tarifas elétricas
preco_kwh = 0.50 # preço por kWh
horas_mes = 720 # horas de uso por mês

# Função para calcular o consumo e custo de energia
def calcular_consumo():
    aparelho = combo.get()
    potencia = aparelhos[aparelho]
    tempo = float(tempo_entry.get())
    preco_kwh = float(kwh_entry.get()) # preço por kWh definido pelo usuário
    consumo = potencia * tempo / 1000 # consumo em kWh
    custo = consumo * preco_kwh * horas_mes / 100 # custo em R$ por mês
    resultado_label.config(text='Consumo: {:.2f} kWh\nCusto: R$ {:.2f}'.format(consumo, custo))

# Função para adicionar um novo aparelho à lista
def adicionar_aparelho():
    nome = novo_nome_entry.get()
    potencia = int(nova_potencia_entry.get())
    aparelhos[nome] = potencia
    combo.config(values=list(aparelhos.keys()))

# def adicionar_aparelho():
#     aparelho = adicionar_entry.get()
#     if aparelho:
#         if aparelho not in aparelhos:
#             aparelhos[aparelho] = calcular_gasto
#             atualizar_opcoes_combobox()
#             messagebox.showinfo('Adição', f'O aparelho "{aparelho}" foi adicionado.')
#             adicionar_entry.delete(0, END)
#         else:
#             messagebox.showwarning('Aviso', f'O aparelho "{aparelho}" já existe.')
#     else:
#         messagebox.showwarning('Aviso', 'Digite um nome para o aparelho.')

# Função para atualizar o combobox
# def atualizar_opcoes_combobox():
#     opcoes = list(aparelhos.keys())
#     aparelhos['values'] = opcoes
#     excluir_combobox['values'] = opcoes
    
#     # remove as chaves que não existem mais no dicionário aparelhos
#     for i, item in enumerate(excluir_combobox['values']):
#         if item not in aparelhos:
#             excluir_combobox['values'] = excluir_combobox['values'][:i] + excluir_combobox['values'][i+1:]


# Função para excluir aparelhos
# def excluir_aparelho():
#     aparelho_selecionado = excluir_combobox.get()
#     if aparelho_selecionado in aparelhos:
#         del aparelhos[aparelho_selecionado]
#         atualizar_opcoes_combobox()
#         messagebox.showinfo('Exclusão', f'O aparelho "{aparelho_selecionado}" foi excluído.')
#     else:
#         messagebox.showerror('Erro', f'O aparelho "{aparelho_selecionado}" não foi encontrado.')

# Configurações da janela
janela = tk.Tk()
janela.title('Calculadora de Energia Elétrica')
janela.geometry('400x400')

# Criar widgets
titulo_label = ttk.Label(janela, text='Selecione o aparelho doméstico e insira o tempo de uso:')
titulo_label.pack(padx=10, pady=10)

combo = ttk.Combobox(janela, values=list(aparelhos.keys()), width=20)
combo.pack(padx=10, pady=10)

tempo_label = ttk.Label(janela, text='Tempo de uso (horas):')
tempo_label.pack(padx=10, pady=5)

tempo_entry = ttk.Entry(janela)
tempo_entry.pack(padx=10, pady=5)

kwh_label = ttk.Label(janela, text='Preço do kWh (R$):')
kwh_label.pack(padx=10, pady=5)

kwh_entry = ttk.Entry(janela)
kwh_entry.pack(padx=10, pady=5)

calcular_button = ttk.Button(janela, text='Calcular', command=calcular_consumo)
calcular_button.pack(padx=10, pady=10)

resultado_label = ttk.Label(janela, text='')
resultado_label.pack(padx=10, pady=10)

# Adicionar novo aparelho
novo_aparelho_label = ttk.Label(janela, text='Adicionar novo aparelho:')
novo_aparelho_label.pack(padx=10, pady=10)

novo_nome_label = ttk.Label(janela, text='Nome:')
novo_nome_label.pack(padx=10, pady=5)

novo_nome_entry = ttk.Entry(janela)
novo_nome_entry.pack(padx=10, pady=5)

nova_potencia_label = ttk.Label(janela, text='Potência (W):')
nova_potencia_label.pack(padx=10, pady=5)

nova_potencia_entry = ttk.Entry(janela)
nova_potencia_entry.pack(padx=10, pady=5)

adicionar_button = ttk.Button(janela, text='Adicionar', command=adicionar_aparelho)
adicionar_button.pack(padx=10, pady=10)

# Excluir aparelho
# excluir_aparelho_label = ttk.Label(janela, text='Excluir aparelho:')
# excluir_aparelho_label.pack(padx=10, pady=10)

# excluir_combobox = ttk.Combobox(janela, values=list(aparelhos.keys()), state='readonly')
# excluir_combobox.pack(padx=10, pady=5)

# excluir_button = ttk.Button(janela, text='Excluir', command=excluir_aparelho)
# excluir_button.pack(padx=10, pady=10)


janela.mainloop()

