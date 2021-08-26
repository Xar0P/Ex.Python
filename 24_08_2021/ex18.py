# Produza um sistema onde você irá organizar vários contratos e lançar vários pagamentos dentro de um sistema. 
# Faça com que o usuário digite um valor de entrada 
# para cadastrar o código de um banco, e logo após coloque o valor da despesa, 
# seguido de uma descrição da despesa, e da data que o item foi criado.

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from PIL import ImageTk, Image # pip install Pillow
import csv

# class Funcionario:

#     def __init__(self, cpf, nome, idade, cargo) -> None:
#         self.cpf = cpf
#         self.nome = nome
#         self.idade = idade
#         self.cargo = cargo
#         self.salario = self._salario()
#         self._valor_banco = 20000

#     @property
#     def valor_banco(self):
#         return self._valor_banco

#     @valor_banco.setter
#     def valor_banco(self, valor):
#         self._valor_banco = valor

#     def _salario(self):
#         return 1000


# class Funcionarios:

#     def __init__(self) -> None:
#         self.funcionarios = []

#     def add_funcionario(self, funcionario: object) -> None:
#         self.funcionarios.append(funcionario)

class NoBank(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class InvalidField(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class Bancos:

    def procurar(self, cod: str = None) -> str:
        if cod == '':
            raise InvalidField()

        with open('24_08_2021/Bancos Associados.csv','r', encoding='UTF-8') as file:
            for line in file:
                line = line.split(';')
                if line[0] == cod:
                    return line
        
        raise NoBank()

    def tratar_cod(self, cod_banco) -> str:
        if len(cod_banco) == 1:
            cod_banco = f'00{cod_banco}'
        elif len(cod_banco) == 2:
            cod_banco = f'0{cod_banco}'

        return cod_banco

    def depositar(self, destino, valor) -> None:
        destino.valor_banco += valor



class Contrato(Bancos):

    def __init__(self, cod_banco: str = None, val_despesa: str = None, desc_despesa: str = None) -> None:
        self.cod_banco = self.tratar_cod(cod_banco)
        self.info_banco = self.procurar(self.cod_banco)

        self.val_despesa = self._despesa_float(val_despesa)
        self.desc_despesa = self._tratar_despesa(desc_despesa)
        self.data_registro = date.today().strftime('%d/%m/%Y')

    def __str__(self) -> str:
        return f'\nBanco: {self.info_banco[0]} - {self.info_banco[1]}\n\nValor: R${self.val_despesa:,.2f}\nDescrição: {self.desc_despesa}\nData do registro: {self.data_registro}\n'

    def _despesa_float(self, despesa) -> float:
        if despesa == '':
            raise InvalidField()

        despesa = despesa.replace('.','').replace(',','.')
        return float(despesa)


    def _tratar_despesa(self, desc) -> str:
        if desc == '':
            raise InvalidField()

        return desc



class Contratos:

    def __init__(self) -> None:
        self.contratos = []

    def add_contrato(self, contrato: object) -> None:    
        self.contratos.append(contrato)

    def pagamento(self, funcionarios: list) -> None:
        i = 0
        for funcionario in funcionarios:
            bancos = Bancos()
            if i < len(self.contratos):
                bancos.depositar(funcionario, self.contratos[i].val_despesa)
            else:
                print('Todos os contratos foram pagos.')
                return
            i += 1



class App(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.pack()
        self._config_window(r"C:\Users\pietr\OneDrive\Imagens\Captura de tela 2021-08-04 151453.png",'Exercício 18','500','400')
        self._criar_widgets()
        self.inside = False
        self.contratos = Contratos()


    def _config_window(self, dir_icon: str, title: str, size_w: str, size_h: str) -> None:
        
        try:
            self.master.tk.call('wm','iconphoto', self.master._w, ImageTk.PhotoImage(Image.open(dir_icon)))
        except Exception:
            pass

        self.master.title(title)
        self.master.minsize(size_w,size_h)
        self.master.resizable(0,0)

    def _criar_widgets(self) -> None:

        self._entry_section()

        button = ttk.Button(self.master, text="Enviar dados", style='Teste.TButton',command=lambda: self._get_inputs())
        button.place(relwidth=0.90,relheight=0.08, rely=0.4, relx=0.05)
        self.master.bind('<Return>',lambda event=None: button.invoke())

        self.frame_results = ttk.Labelframe(self.master)
        self.frame_results.place(relwidth=1, relheight=0.5, rely=0.55)

    def _entry_section(self) -> None:

        # Código banco
        label_cod = ttk.Label(self.master,text="Código do banco")
        label_cod.place(relwidth=0.35,relheight=0.08, rely=0.05, relx=0.05)

        self.input_cod = tk.StringVar()
        self.input_cod = ttk.Entry(self.master, textvariable=self.input_cod)
        self.input_cod.place(relwidth=0.6,relheight=0.08, relx=0.35, rely=0.05)


        # Valor despesa
        label_val_desp = ttk.Label(self.master,text="Valor da despesa")
        label_val_desp.place(relwidth=0.35,relheight=0.08, rely=0.15, relx=0.05)

        self.input_val_desp = tk.StringVar()
        self.input_val_desp = ttk.Entry(self.master, textvariable=self.input_val_desp)
        self.input_val_desp.place(relwidth=0.6,relheight=0.08, relx=0.35, rely=0.15)


        # Descrição despesa
        label_desc = ttk.Label(self.master,text="Descrição da despesa")
        label_desc.place(relwidth=0.35,relheight=0.08, rely=0.25, relx=0.05)

        self.input_desc = tk.StringVar()
        self.input_desc = ttk.Entry(self.master, textvariable=self.input_desc)
        self.input_desc.place(relwidth=0.6,relheight=0.08, relx=0.35, rely=0.25)


    def _get_inputs(self) -> None:

        try:
            if self.inside:
                self.inside.destroy()

            value_cod = self.get_input(self.input_cod)
            value_despesa = self.get_input(self.input_val_desp)
            value_desc = self.get_input(self.input_desc)


            contrato = Contrato(value_cod, value_despesa, value_desc)
            self.contratos.add_contrato(contrato)

            self.inside = tk.Label(self.frame_results, text=contrato)
            self.inside.pack()

            self.input_cod.delete(0,'end')
            self.input_val_desp.delete(0,'end')
            self.input_desc.delete(0,'end')

        except InvalidField:
            messagebox.showerror(title='Erro',message='Insira todos os campos!')
        except NoBank:
            messagebox.showerror(title='Erro',message='Banco não encontrado!')
        except ValueError:
            messagebox.showerror(title='Erro',message='Valor da despesa inválido!')
        except Exception as e:
            messagebox.showerror(title='Erro',message='Ocorreu um erro! Tente novamente.')



    def get_input(self, input_name):
        text = input_name.get()
        return text



if __name__ == '__main__':

    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

    with open('24_08_2021/Despesas.csv','w',newline='',encoding='UTF-8') as csvfile:
        fieldnames = ['ID','BANCO','VALOR','DESCRIÇÃO','REGISTRO']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

        writer.writeheader()
        i = 1
        for contrato in app.contratos.contratos:
            writer.writerow({
                'ID':i,
                'BANCO':f'{contrato.info_banco[0]} - {contrato.info_banco[1]}',
                'VALOR':f'R${contrato.val_despesa:,.2f}',
                'DESCRIÇÃO':contrato.desc_despesa,
                'REGISTRO':contrato.data_registro
            })
            i += 1