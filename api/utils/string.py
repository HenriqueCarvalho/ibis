from api.utils import tipo_fluxo
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def valor_formatado(valor, fluxo=None):
    """
    Formata o valor em double/floar para uma string.

    120.00 -> R$ 120.00

    Parameter: (valor :double, tipo_fluxo :enum default None)

    Return: String
    """

    if valor < 0:
        #return "-R$ " + str(valor * -1)
        valor *= -1
        return '-R$ ' + locale.currency(valor, grouping=True, symbol=False)
    elif fluxo == tipo_fluxo.ENTRADA:
        #return "R$ " + str(valor)
        return 'R$ ' + locale.currency( valor, grouping=True, symbol=False)
    elif fluxo == tipo_fluxo.SAIDA:
        #return "-R$ " + str(valor)
        return '-R$ ' + locale.currency( valor, grouping=True, symbol=False)
    
    return 'R$ ' + locale.currency( valor, grouping=True, symbol=False)