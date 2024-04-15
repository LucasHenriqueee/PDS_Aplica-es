# FFT
Para obter um aumento significativo na eficiência, é necessário que se decomponha a computação da DFT em computações sucessivamente menores.
Nesse processo exploram-se ambas a simetria e a periodicidade da exponencial complexa:
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
