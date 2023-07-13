def convert_date(date):
    result = ''
    months = {
      '01': 'Январь',
      '02': 'Февраль',
      '03': 'Март',
      '04': 'Апрель',
      '05': 'Май',
      '06': 'Июнь',
      '07': 'Июль',
      '08': 'Август',
      '09': 'Сентябрь',
      '10': 'Октябрь',
      '11': 'Ноябрь',
      '12': 'Декабрь'
    }
    split_date = date.split("-")
    print(split_date)
    print(months[str(split_date[1])])
    result = f'{split_date[2]}, {months[str(split_date[1])]}'
    print(result)
    return result


def convert_time(time):
    print(str(f'{time.split(":")[0]}:{time.split(":")[1]}'))
    return str(f'{time.split(":")[0]}:{time.split(":")[1]}')



