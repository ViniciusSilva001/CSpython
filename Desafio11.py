altura=float(input('Digite a altura da parede:'))
largura=float(input('Digite a largura da parede:'))
area=largura*altura
print('Sua parede tem a dimensão de {}x{} e a área de {}m²'.format(largura, altura , area))
tinta=area/2
print('Você precisara de {}l de tinta para pintar toda a parede'.format(tinta))