import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import DISABLED, NORMAL
from PIL import ImageTk, Image # pip install Pillow

class App(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.pack()
        self._config_window(r"24_08_2021/carpe_diem.png",'Exercício 19','500','300')
        self._criar_widgets()
        self.inside = False


    def _config_window(self, dir_icon: str, title: str, size_w: str, size_h: str) -> None:
        
        try:
            self.master.tk.call('wm','iconphoto', self.master._w, ImageTk.PhotoImage(Image.open(dir_icon)))
        except Exception:
            pass

        self.master.title(title)
        self.master.minsize(size_w,size_h)
        self.master.resizable(0,0)


    def _criar_widgets(self) -> None:

        self._entry_prob()

        self.frame_results = ttk.Labelframe(self.master)
        self.frame_results.place(relwidth=1, relheight=0.85, rely=0.35)

    
    def _entry_prob(self) -> None:
        
        self.label_prob = ttk.Label(self.master,text="Probabilidade do item")
        self.label_prob.place(relwidth=0.32,relheight=0.08, rely=0.05, relx=0.05)

        self.input_prob = tk.StringVar()
        self.input_prob = ttk.Entry(self.master, textvariable=self.input_prob)
        self.input_prob.place(relwidth=0.34,relheight=0.08, relx=0.32, rely=0.05)
        self.input_prob.insert(0,'1 em 170')
        self.input_prob.bind("<FocusIn>", lambda args: self.input_prob.delete('0', 'end'))

        self.button_prob = ttk.Button(self.master, text="Enviar",command=lambda: self._get_prob())
        self.button_prob.place(relwidth=0.27,relheight=0.08, rely=0.05, relx=0.68)
        self.master.bind('<Return>',lambda event=None: self.button_prob.invoke())

    
    def _entry_kills(self) -> None:
 
        self.label_kills = ttk.Label(self.master,text="Inimigos mortos")
        self.label_kills.place(relwidth=0.32,relheight=0.08, rely=0.15, relx=0.05)

        self.input_kills = tk.StringVar()
        self.input_kills = ttk.Entry(self.master, textvariable=self.input_kills)
        self.input_kills.place(relwidth=0.34,relheight=0.08, relx=0.32, rely=0.15)

        self.button_send = ttk.Button(self.master, text="Enviar",command=lambda: self._get_kills())
        self.button_send.place(relwidth=0.27,relheight=0.08, rely=0.15, relx=0.68)
        self.master.bind('<Return>',lambda event=None: self.button_send.invoke())


    def _get_prob(self) -> None:

        self.button_prob['state'] = DISABLED
        self.value_prob = self.get_input(self.input_prob)
        self.input_prob['state'] = DISABLED

        if self.value_prob == '':
            messagebox.showerror(title='Erro',message='Insira todos os campos!')
            self._reset()

        self._entry_kills()

    
    def _get_kills(self) -> None:

        self.button_send['state'] = DISABLED
        self.value_kills = self.get_input(self.input_kills)
        self.input_kills['state'] = DISABLED

        self.button_reset = ttk.Button(self.master, text='Reiniciar', command=lambda: self._reset())
        self.button_reset.place(relwidth=0.45,relheight=0.08,rely=0.27,relx=0.05)

        self.button_close = ttk.Button(self.master, text='Finalizar', command=lambda: self.master.destroy())
        self.button_close.place(relwidth=0.45,relheight=0.08,rely=0.27,relx=0.50)

        self._send_values()

    def _send_values(self) -> None:

        try:
            item = Item(self.value_prob)

            self.inside = tk.Label(self.frame_results, text=item.chance_item(self.value_kills))
            self.inside.pack()
        except ValueError:
            messagebox.showerror(title='Erro',message='Insira todos os campos!')
            self._reset()
        except IndexError:
            messagebox.showerror(title='Erro',message='Esses valores estão muito estranhos, tente mudar eles.')
            self._reset()


    def get_input(self, input_name) -> str:
        text = input_name.get()
        return text


    def _reset(self) -> None:

        if self.inside:
                self.inside.destroy()
        
        self.button_prob['state'] = NORMAL
        self.master.bind('<Return>',lambda event=None: self.button_prob.invoke())
        self.input_prob['state'] = NORMAL
        self.input_prob.delete(0,'end')
        self.label_kills.destroy()
        self.button_send.destroy()
        self.input_kills.destroy()


class Item:

    def __init__(self, probabilidade: str = '1/170') -> None:
        self.probabilidade = self._format_prob(probabilidade)

    def _format_prob(self, prob) -> str:
        if 'em' in prob:
            prob = prob.replace('em', '/')
            return prob
        if 'chance' in prob:
            prob = prob.replace('chance', '/')
            return prob
        if '/' in prob:
            return prob

        raise IndexError
        
    def chance_item(self, inim_mortos) -> None:
        inim_mortos = int(inim_mortos)

        valor = ((eval(self.probabilidade)) * inim_mortos) * 100
        probabilidade_maximo = self.probabilidade.split('/')

        p_30 = (float(probabilidade_maximo[1])) * (30/100) / float(probabilidade_maximo[0])
        p_30_str = f'Para você ter 30% de chances de conseguir o item você deverá matar {p_30:.0f} inimigos no jogo.'

        p_40 = (float(probabilidade_maximo[1])) * (40/100) / float(probabilidade_maximo[0])
        p_40_str = f'Para você ter 40% de chances de conseguir o item você deverá matar {p_40:.0f} inimigos no jogo.'

        p_50 = (float(probabilidade_maximo[1])) * (50/100) / float(probabilidade_maximo[0])
        p_50_str = f'Para você ter 50% de chances de conseguir o item você deverá matar {p_50:.0f} inimigos no jogo.'

        p_60 = (float(probabilidade_maximo[1])) * (60/100) / float(probabilidade_maximo[0])
        p_60_str = f'Para você ter 60% de chances de conseguir o item você deverá matar {p_60:.0f} inimigos no jogo.'

        p_70 = (float(probabilidade_maximo[1])) * (70/100) / float(probabilidade_maximo[0])
        p_70_str = f'Para você ter 70% de chances de conseguir o item você deverá matar {p_70:.0f} inimigos no jogo.'

        p_80 = (float(probabilidade_maximo[1])) * (80/100) / float(probabilidade_maximo[0])
        p_80_str = f'Para você ter 80% de chances de conseguir o item você deverá matar {p_80:.0f} inimigos no jogo.'

        p_90 = (float(probabilidade_maximo[1])) * (90/100) / float(probabilidade_maximo[0])
        p_90_str = f'Para você ter 90% de chances de conseguir o item você deverá matar {p_90:.0f} inimigos no jogo.'

        p_95 = (float(probabilidade_maximo[1])) * (95/100) / float(probabilidade_maximo[0])
        p_95_str = f'Para você ter 95% de chances de conseguir o item você deverá matar {p_95:.0f} inimigos no jogo.'

        p_97 = (float(probabilidade_maximo[1])) * (97/100) / float(probabilidade_maximo[0])
        p_97_str = f'Para você ter 97% de chances de conseguir o item você deverá matar {p_97:.0f} inimigos no jogo.'

        atual = f'\nVocê já matou {inim_mortos} inimigos e a probabilidade que teve ao mata-los foi de {valor:.0f}%.\n'

        return f'{p_30_str}\n{p_40_str}\n{p_50_str}\n{p_60_str}\n{p_70_str}\n{p_80_str}\n{p_90_str}\n{p_95_str}\n{p_97_str}\n{atual}'

if __name__ == "__main__":

    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
