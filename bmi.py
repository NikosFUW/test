#coding utf-8
waga = float(input('Podaj wagę> '))
wzrost = float(input('Podaj wzrost> '))
BMI = waga/(wzrost**2)

komunikat = 'Prawidłowe.'

if BMI <= 18.5:
    komunikat = 'Za niskie.'
elif BMI >= 25:
    komunikat = 'Za wysokie.'

print('BMI wynosi {} - {}'.format(BMI,komunikat))