import requests
usdoreur = int(input('type 1 for usd and 2 or euros'))
if usdoreur != 1 and usdoreur != 2:
    print('ERROR, unknown currency typeS')
else:   
    userinput = float(input("Enter amount "))

    req = requests.get('https://api.frankfurter.dev/v2/rates?base=usd')

    data = req.json()

    for x in data:
        if usdoreur == 1:
            yo = userinput * x['rate']
            currency = 'Euros'
        else:

            yo = userinput / x['rate']
            currency = 'Dollars'
        if x['base'] == 'USD' and x['quote'] == 'EUR':
            print(f'{x['date']}\n {yo} {currency}')        