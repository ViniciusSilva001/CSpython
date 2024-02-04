p=float(input('Digite o preço do produto:R$'))
d=float(input('Digite a % de desconto:'))
print('O valor do produto de {} com o desconto de {} sairia por {:.2f}'.format(p, d, p-(p*d/100)))