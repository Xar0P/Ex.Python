class Item:

    def __init__(self, probabilidade: str = '1/170') -> None:
        self.probabilidade = probabilidade

    def chance_item(self, inim_mortos) -> None:
        valor = ((eval(self.probabilidade)) * inim_mortos) * 100
        probabilidade_maximo = self.probabilidade.split('/')

        p_30 = (float(probabilidade_maximo[1])) * (30/100) / float(probabilidade_maximo[0])
        p_30_str = f'\nPara você ter 30% de chances de conseguir o item você deverá matar {p_30:.0f} inimigos no jogo.\n'

        p_40 = (float(probabilidade_maximo[1])) * (40/100) / float(probabilidade_maximo[0])
        p_40_str = f'Para você ter 40% de chances de conseguir o item você deverá matar {p_40:.0f} inimigos no jogo.\n'

        p_50 = (float(probabilidade_maximo[1])) * (50/100) / float(probabilidade_maximo[0])
        p_50_str = f'Para você ter 50% de chances de conseguir o item você deverá matar {p_50:.0f} inimigos no jogo.\n'

        p_60 = (float(probabilidade_maximo[1])) * (60/100) / float(probabilidade_maximo[0])
        p_60_str = f'Para você ter 60% de chances de conseguir o item você deverá matar {p_60:.0f} inimigos no jogo.\n'

        p_70 = (float(probabilidade_maximo[1])) * (70/100) / float(probabilidade_maximo[0])
        p_70_str = f'Para você ter 70% de chances de conseguir o item você deverá matar {p_70:.0f} inimigos no jogo.\n'

        p_80 = (float(probabilidade_maximo[1])) * (80/100) / float(probabilidade_maximo[0])
        p_80_str = f'Para você ter 80% de chances de conseguir o item você deverá matar {p_80:.0f} inimigos no jogo.\n'

        p_90 = (float(probabilidade_maximo[1])) * (90/100) / float(probabilidade_maximo[0])
        p_90_str = f'Para você ter 90% de chances de conseguir o item você deverá matar {p_90:.0f} inimigos no jogo.\n'

        p_95 = (float(probabilidade_maximo[1])) * (95/100) / float(probabilidade_maximo[0])
        p_95_str = f'Para você ter 95% de chances de conseguir o item você deverá matar {p_95:.0f} inimigos no jogo.\n'

        p_97 = (float(probabilidade_maximo[1])) * (97/100) / float(probabilidade_maximo[0])
        p_97_str = f'Para você ter 97% de chances de conseguir o item você deverá matar {p_97:.0f} inimigos no jogo.\n'

        atual = f'\nVocê já matou {inim_mortos} inimigos e a probabilidade que teve ao mata-los foi de {valor}.\n'

        return f'{p_30_str}\n{p_40_str}\n{p_50_str}\n{p_60_str}\n{p_70_str}\n{p_80_str}\n{p_90_str}\n{p_95_str}\n{p_97_str}\n{atual}'

if __name__ == "__main__":

    item = Item('1/170')

    print(item.chance_item(50))
