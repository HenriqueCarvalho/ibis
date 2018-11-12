from rest_framework.serializers import DateTimeField

#contante dos dias
DAY = {
    'Sunday':'Domingo',
    'Monday':'Segunda',
    'Tuesday':'Terça',
    'Wednesday':'Quarta',
    'Thursday':'Quinta',
    'Friday':'Sexta',
    'Saturday':'Sabado',
}

MONTH = {
    'Jan':'Jan',
    'Feb':'Fev',
    'Mar':'Mar',
    'Apr':'Abr',
    'May':'Mai',
    'Jun':'Jun',
    'Jul':'Jul',
    'Aug':'Ago',
    'Sep':'Set',
    'Oct':'Out',
    'Nov':'Nov',
    'Dec':'Dez',
}

def getMonthStart(date):
    """
    return the first day of month
    date:
    String YYYY-mm-dd
    """
    aux = date.split('-')[:2]
    return '-'.join((aux[0],aux[1],'01'))

def getMonthEnd(date):
    aux = date.split('-')[:2]
    return '-'.join((aux[0],aux[1],'30'))

def translate_date_en_to_pt(date):
    """
    Converte a data em ingles para pt
    Lembrando que o formato esperado é 
    "%A %d %b %Y" - Monday 27 Oct 2018
    retorno
    Segunda, 27 Out. 2018
    """
    #print("date dentro da funcao eh 1",date)
    #date = str(date)
    aux = date.split(' ')
    #recupera o dia e mes
    day = aux[0]
    month = aux[2]
    #renomeando dia e mes
    month = MONTH[month]
    day = DAY[day]

    return '{}, {} {}. {}'.format(day,aux[1],month,aux[3])