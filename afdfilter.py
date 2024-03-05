from tkinter import *
from tkinter import filedialog, messagebox, PhotoImage
from tkcalendar import DateEntry
import customtkinter


customtkinter.set_appearance_mode("dark")


#janela
janela = customtkinter.CTk()
janela.title("AFDFilter")
janela.iconbitmap("filtro.ico")
janela.geometry("600x400")
janela.maxsize(width=605, height=405)
janela.resizable(width=False, height=False)


img_fundo = PhotoImage(file="filtro.png")
customtkinter.CTkLabel(janela,text="", image=img_fundo).place(x=245, y=7, w=100, h=90)



def afd():
    global arquivo2
    arquivo = filedialog.askopenfilename(initialdir="/Desktop", title="AFDFilter",filetypes=((" Arquivos de texto", " *.txt "),("", "")))
    arquivo2 = arquivo
    anexo.insert(0, arquivo2)



def arquivo_afd():
    arquivo3 = anexo.get()
    pis = numero_pis.get()
    

    if not arquivo3:
        messagebox.showerror(title="AFDFilter", message="Arquivo não encontrado.")
    elif not pis:
        messagebox.showerror(title="AFDFilter", message="O campo PIS/CPF está vazio, por favor preencha.")
    else:
        with open(arquivo2, 'r') as arquivos:
            linhas = arquivos.readlines()

            # Verificar se o Pis/CPF está em alguma linha do arquivo
            encontrou_pis = any(pis in linha for linha in linhas)
            
            nome_arquivo_destino = f'AFDFilter_{pis}.txt'


            if encontrou_pis:
                nome_arquivo_destino = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Arquivos de Texto", "*.txt")],
                                            title="Salvar como",
                                            initialfile=nome_arquivo_destino)   

                # Criar arquivo filtrado apenas se o Pis/CPF foi encontrado
                with open(nome_arquivo_destino, 'w') as arquivo_filter:
                    for linha in linhas:
                        if pis in linha:
                            arquivo_filter.write(linha)

                messagebox.showinfo(title="AFDFilter", message=f"Arquivo filtrado para: AFDFilter_{pis}.txt")
            else:
                messagebox.showerror(title="AFDFilter", message=f"PIS/CPF: {pis} não encontrado no arquivo.")



def arquivo_afd_data():

    arquivo3 = anexo.get()

    if not arquivo3:
        messagebox.showerror(title="AFDFilter", message="Arquivo não encontrado.")
    else:
        with open(arquivo2, 'r') as arquivo:
            linhas = arquivo.readlines()

            
            data_selecionada_i = data_inicial.get_date()
            data_formatada_i = data_selecionada_i.strftime("%d%m%Y")  
            print("Data Inicial como string:", data_formatada_i)

            data_selecionada_f = data_final.get_date()
            data_formatada_f = data_selecionada_f.strftime("%d%m%Y")  
            print("Data Final como string:", data_formatada_f)

            primeira_ocorrencia_termo1 = None
            ultima_ocorrencia_termo2 = None

            for i, linha in enumerate(linhas, start=1):
                posicao = linha[10:18]
                

                if data_formatada_i in posicao and primeira_ocorrencia_termo1 is None:
                    primeira_ocorrencia_termo1 = i

                if data_formatada_f in posicao:
                    ultima_ocorrencia_termo2 = i

            if primeira_ocorrencia_termo1 is not None:
                print(f"A primeira ocorrência de '{data_formatada_i}' está na linha {primeira_ocorrencia_termo1}.")
                
            else:
                messagebox.showerror(title="AFDFilter", message=f"Data inicial: {data_inicial.get()} não encontrada no arquivo.")
                return

            if ultima_ocorrencia_termo2 is not None:
                print(f"A última ocorrência de '{data_formatada_f}' está na linha {ultima_ocorrencia_termo2}.")
            else:
                messagebox.showerror(title="AFDFilter", message=f"Data final: {data_final.get()} não encontrada no arquivo.")

            # Nome do arquivo de origem
            nome_arquivo_origem = arquivo2

            # Intervalo desejado
            inicio_intervalo = int(primeira_ocorrencia_termo1)
            fim_intervalo = int(ultima_ocorrencia_termo2)

            # Nome do arquivo de destino
            nome_arquivo_destino = f"AFDFilter_{data_formatada_i}_{data_formatada_f}.txt"

        with open(nome_arquivo_origem, 'r') as arquivo_origem:
            linhas_origem = arquivo_origem.readlines()
            linhas_intervalo = linhas_origem[inicio_intervalo - 1:fim_intervalo]

            # Manter as 2 primeiras e as 2 últimas linhas
            linhas_cabecalho = linhas_origem[:1]
            linhas_rodape = linhas_origem[-2:]
            
            linhas_final = linhas_cabecalho + linhas_intervalo + linhas_rodape

            nome_arquivo_destino = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                 filetypes=[("Arquivos de Texto", "*.txt")],
                                                                 title="Salvar como",
                                                                 initialfile=nome_arquivo_destino)            

            with open(nome_arquivo_destino, 'w') as arquivo_destino:
                arquivo_destino.writelines(linhas_final)

            messagebox.showinfo(title="AFDFilter", message=f"Arquivo filtrado para: AFDFilter_{data_formatada_i}_{data_formatada_f}.txt")
        print(f"Intervalo de linhas [{inicio_intervalo}:{fim_intervalo}] salvo em '{nome_arquivo_destino}'.")


def arquivo_afd_data_671():

    arquivo3 = anexo.get()

    if not arquivo3:
        messagebox.showerror(title="AFDFilter", message="Arquivo não encontrado.")
    else:
        with open(arquivo2, 'r') as arquivo:
            linhas = arquivo.readlines()

            data_selecionada_i = data_inicial.get_date()
            data_formatada_i = data_selecionada_i.strftime("%Y-%m-%d")  
            print("Data Inicial como string:", data_formatada_i)

            data_selecionada_f = data_final.get_date()
            data_formatada_f = data_selecionada_f.strftime("%Y-%m-%d")  
            print("Data Final como string:", data_formatada_f)

            primeira_ocorrencia_termo1 = None
            ultima_ocorrencia_termo2 = None

            for i, linha in enumerate(linhas, start=1):
                posicao = linha[10:20]


                if data_formatada_i in posicao and primeira_ocorrencia_termo1 is None:
                    primeira_ocorrencia_termo1 = i

                if data_formatada_f in posicao:
                    ultima_ocorrencia_termo2 = i

            if primeira_ocorrencia_termo1 is not None:
                print(f"A primeira ocorrência de '{data_formatada_i}' está na linha {primeira_ocorrencia_termo1}.")
            else:
                messagebox.showerror(title="AFDFilter", message=f"Data inicial: {data_inicial.get()} não encontrada no arquivo.")
                return

            if ultima_ocorrencia_termo2 is not None:
                print(f"A última ocorrência de '{data_formatada_f}' está na linha {ultima_ocorrencia_termo2}.")
            else:
                messagebox.showerror(title="AFDFilter", message=f"Data final: {data_final.get()} não encontrada no arquivo.")

            # Nome do arquivo de origem
            nome_arquivo_origem = arquivo2

            # Intervalo desejado
            inicio_intervalo = int(primeira_ocorrencia_termo1)
            fim_intervalo = int(ultima_ocorrencia_termo2)

            # Nome do arquivo de destino
            nome_arquivo_destino = f"AFDFilter_{data_formatada_i}_{data_formatada_f}.txt"


        with open(nome_arquivo_origem, 'r') as arquivo_origem:
            linhas_origem = arquivo_origem.readlines()
            linhas_intervalo = linhas_origem[inicio_intervalo - 1:fim_intervalo]

            # Manter as 2 primeiras e as 2 últimas linhas
            linhas_cabecalho = linhas_origem[:1]
            linhas_rodape = linhas_origem[-2:]
            
            linhas_final = linhas_cabecalho + linhas_intervalo + linhas_rodape
            
            nome_arquivo_destino = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                 filetypes=[("Arquivos de Texto", "*.txt")],
                                                                 title="Salvar como",
                                                                 initialfile=nome_arquivo_destino)

            with open(nome_arquivo_destino, 'w') as arquivo_destino:
                arquivo_destino.writelines(linhas_final)

            messagebox.showinfo(title="AFDFilter", message=f"Arquivo filtrado para: AFDFilter_{data_formatada_i}_{data_formatada_f}.txt")
            print(f"Intervalo de linhas [{inicio_intervalo}:{fim_intervalo}] salvo em '{nome_arquivo_destino}'.")


def verificar_afd(nome_arquivo_destino="AFDFilter_NSR.txt", diferenca_maxima=1):
    
    arquivo3 = anexo.get()
    
    if not arquivo3:
        messagebox.showerror(title="AFDFilter", message="Arquivo não encontrado.")
    else:
        with open(arquivo2, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhas_com_erro = []

            for i in range(1, len(linhas) - 2):  # Desconsiderar as 2 últimas linhas
                linha_atual = linhas[i][:9].rstrip()
                linha_anterior = linhas[i - 1][:9].rstrip()

                if len(linhas[i]) >= 9 and len(linhas[i - 1]) >= 9:
                    if linha_atual.isdigit() and linha_anterior.isdigit():
                        diferenca = int(linha_atual) - int(linha_anterior)

                        if diferenca > diferenca_maxima:
                            linhas_com_erro.append(f"Linha {i + 1}: {linhas[i].strip()}")

                if linha_atual < linha_anterior:
                    linhas_com_erro.append(f"Linha {i + 1}: {linhas[i].strip()}")

        nome_arquivo_destino = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                 filetypes=[("Arquivos de Texto", "*.txt")],
                                                                 title="Salvar como",
                                                                 initialfile="AFDFilter_NSR.txt")

        if nome_arquivo_destino:  # Escrever as linhas com erro no arquivo de destino
            with open(nome_arquivo_destino, 'w') as arquivo_destino:
                arquivo_destino.writelines('\n'.join(linhas_com_erro))
                arquivo_destino.writelines('\n'f"Número de linhas com erro no NSR: {len(linhas_com_erro)}")
                messagebox.showinfo(title="AFDFilter", message=f"Análise do AFD salva no arquivo: AFDFilter_NSR.txt")       
        

def limpar():
    anexo.delete(0, END)
    numero_pis.delete(0, END)
    data_inicial.delete(0, END)
    data_final.delete(0, END)

def limpar_pis():
    numero_pis.delete(0, END)


#AFD
global anexo
anexo = customtkinter.CTkEntry(janela, placeholder_text='Selecione o AFD', fg_color="#343638", border_color="#565B5E")
anexo.place(relx=0.2, rely=0.2, w=450, h=45)
#imagem/button
imagem = PhotoImage(file="clips.svg").subsample(17,17)
nome_afd = customtkinter.CTkButton(janela,text="",fg_color="#343638", corner_radius=5, border_color="#565B5E", border_width=2, image=imagem, command=afd)
nome_afd.place(x=429, y=80, w=64, h=45)

#Pis
global pis
numero_pis = customtkinter.CTkEntry(janela, placeholder_text='Digite o PIS/CPF', fg_color="#343638", border_color="#565B5E")
numero_pis.place(x=120, y=130, w=450, h=45)
imagem2 = PhotoImage(file="lixeira.svg").subsample(15,15)
limpar_pis = customtkinter.CTkButton(janela,text="",fg_color="#343638", corner_radius=5, border_color="#565B5E", border_width=2, image=imagem2, command=limpar_pis)
limpar_pis.place(x=429, y=130, w=64, h=45)


# Data Inicial
global data_i
customtkinter.CTkLabel(janela, text="Data Inicial:", text_color= 'white', font= ('Arial', 14))\
    .place(relx=0.2, rely=0.48, w=110, h=20)
data_inicial = DateEntry(janela, width=30, background='darkred', foreground='white',font = ('Arial', 13), text_color= 'white', borderwidth=2, locale='pt_BR')
data_inicial.place(relx=0.35, rely=0.47, w=180, h=30)

# Data Final
global data_f
customtkinter.CTkLabel(janela, text="Data Final:", text_color= 'white', font=("Arial", 14))\
    .place(relx=0.2, rely=0.58, w=110, h=20)
data_final = DateEntry(janela, width=15, background='darkred', foreground='white', font=("Arial", 13), borderwidth=2, locale='pt_BR')
data_final.place(relx=0.35, rely=0.57, w=180, h=30)

#botão limpar
limpar = customtkinter.CTkButton(janela, text="Limpar Dados",fg_color="black", command=limpar)
limpar.place(relx=0.1, rely=0.7, w=200, h=40)


global botao
botao = customtkinter.CTkButton(janela, text="Filtrar AFD",fg_color="black", command=arquivo_afd)
botao.place(relx=0.4, rely=0.7, w=200, h=40)

global botao_data
botao_data = customtkinter.CTkButton(janela, text="Filtrar Data(1510)", fg_color="black", command=arquivo_afd_data)
botao_data.place(relx=0.7, rely=0.7, w=200, h=40)

global botao_data_671
botao_data_671 = customtkinter.CTkButton(janela, text="Filtrar Data(671)", fg_color="black", command=arquivo_afd_data_671)
botao_data_671.place(relx=0.7, rely=0.8, w=200, h=40)

global botao_verifica
botao_verifica = customtkinter.CTkButton(janela, text="Verificar AFD", fg_color="black", command=verificar_afd)
botao_verifica.place(relx=0.4, rely=0.8, w=200, h=40)
nome_arquivo_destino = "AFDFilter_NSR.txt"

customtkinter.CTkLabel(janela, text="© GTBS - 2024", anchor=W, text_color= 'black').place(relx=0.4, rely=0.89, w=130, h=50)


janela.mainloop()

#Fim
