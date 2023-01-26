alimento = input('Comes frutas?')
x= ''
if alimento == 'false':
    print('Necesitas comer frutas')
elif alimento == 'true':
   x= input('Cuantas frutas comes?')
if x>='5':
    print('Sigue así')
    fruta=input('Cuantas frutas comes al día?')
    if fruta >='2':
        print('Comes slaudable')
    else:
        print('Te recomendaria comer una fruta mas')
if x<'5' and x>'2':
    input('Come mas frutas a la semana')
if x<='2':
    print('Necesitas comer frutas')