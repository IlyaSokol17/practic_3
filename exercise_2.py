second = int(input('введите секунду от 1 до 86400'))
hours = int(second / 3600)
minute = int((second - hours * 3600)/60)
seconds = second - hours * 3600 - minute * 60
seconds = second - (minute * 60 + hours * 60 * 60)
print(f'время -  {hours}:{minute}:{seconds}')