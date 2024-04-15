# FFT
Para obter um aumento significativo na eficiência, é necessário que se decomponha a computação da DFT em computações sucessivamente menores.
Nesse processo exploram-se ambas a simetria e a periodicidade da exponencial complexa:
$$Wn = e^{-j\frac{(2\pi)}{N}}
W{n}^{Kn} = e^{-j\frac{2pi}{N}Kn}$$

O princípio de decimação no tempo é mais bem ilustrado para o caso especial em que N é potência inteira de 2:
$`N = 2^l'$
