while True:
  try:
    killograms = int(input('Введите количество киллограм: '))
    tonn = killograms // 1000
    print(f'Тонн: {tonn}')
    break
  except:
    print('Введите пожалуйста количество кг!')
    continue
