# Implementação da FFT por decimarão no tempo
Para obter um aumento significativo na eficiência, é necessário que se decomponha a computação da DFT em computações sucessivamente menores.
Nesse processo exploram-se ambas a simetria e a periodicidade da exponencial complexa:
$$Wn = e^{-j\frac{(2\pi)}{N}}$$
$$W{n}^{Kn} = e^{-j\frac{2pi}{N}Kn}$$

O princípio de decimação no tempo é mais bem ilustrado para o caso especial em que N é potência inteira de 2:
$$N = 2^l$$

Como N é um inteiro par, é possível computar X(k) separando x(n) em duas subsequências de N/2 pontos cada, uma para a qual n é par e a outra para a qual n é ímpar. Assim, sendo X(k) dada por
$$X[k] = \sum_{n=0}^{N-1}x(0).W_{N}^{Kn}$$
tem-se
$$X[k] = \sum_{npar}x(n).W_{N}^{Kn}+\sum_{nimpar}x(n).W_{N}^{Kn}$$

Substituindo-se n par por n = 2r e n ímpar por n = 2r + 1, a equação pode ser reescrita:
$$X[k]=\sum_{r=0}^{\frac{N}{2}-1}x(2r)W_{\frac{N}{2}}^{rk}+W_{N}^k\sum_{r=0}^{(\frac{N}{2})-1}x(2r+1)W_{\frac{N}{2}}^{rk} = G(k) + W_N^kH(k)
$$

Cada um dos somatórios na equação acima corresponde a uma DFT de N/2 pontos, o primeiro correspondendo à DFT dos coeficientes de índice par da sequência x(n), e o segundo à DFT dos coeficientes de índice ímpar da sequência x(n). Apesar de k variar entre 0 e N-1, cada um dos somatórios só precisa ser computado para k variando do 0 a (N/2)-1, pois G(k) e H(k) são periódicas em k com período N/2. Após as duas DFT's, correspondentes aos dois somatórios na equação serem computadas, elas são combinadas para formar a DFT X(k).

Tudo isso será implementado no código FFFpy

## FFT.py
### Separação das componentes pares e impares de forma recursiva
```python
 if (N <= 1): # verificar o comprimento 
        return x
else:
        Wn = np.exp(-2j * np.pi * np.arange(N//2) / N)
        par = fft(x[0::2])
        impar = fft(x[1::2])
```
Se o comprimento da lista x for maior que 1, então o código divide a lista em duas partes:

-par: Contendo os elementos de índices pares de x.<br/>
-impar: Contendo os elementos de índices ímpares de x.

A função fft é chamada recursivamente para calcular as transformadas de Fourier das listas par e impar. Isso significa que a função está sendo aplicada em partes menores do problema (metade das amostras) repetidamente até atingir a condição base. Depois que as transformadas de Fourier das partes pares e ímpares são calculadas recursivamente, elas são combinadas para formar a transformada de Fourier completa da lista original x. Isso é feito usando os fatores de rotação apropriados Wn e a propriedade da Transformada Rápida de Fourier (FFT) que permite combinar as transformadas de maneira eficiente.
O resultado final é retornado como a concatenação das transformadas parciais combinadas.
