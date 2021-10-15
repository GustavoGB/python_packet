from dev_aberto import hello
import babel.dates
import gettext
import datetime
gettext.install('cli',localedir='locale')

if __name__ == '__main__':

    date, name = hello()

    formated_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z') 

    formated_date = babel.dates.format_datetime(formated_date)

    print(_('Último commit feito em:'), formated_date, _(' por'), name)
