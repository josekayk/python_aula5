def obter_lado_quadrado():
    """
    Função que solicita ao usuário o valor do lado do quadrado, garantindo que a entrada seja válida.
    """
    while True:
        try:
            lado = float(input("Digite o comprimento do lado do quadrado (em unidades): "))

            if lado <= 0:
                print("O valor do lado deve ser maior que zero. Tente novamente.")
            else:
                return lado
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")


def calcular_area_quadrado(lado):
    """
    Função que calcula a área do quadrado com base no comprimento do lado.
    """
    return lado ** 2


def calcular_dobro_area(area):
    """
    Função que calcula o dobro da área de um quadrado.
    """
    return 2 * area


def exibir_resultados(lado, area, dobro_area):
    """
    Função para exibir os resultados de maneira amigável.
    """
    print("\n" + "=" * 40)
    print(f"A área do quadrado com lado {lado} é: {area:.2f} unidades quadradas")
    print(f"O dobro da área do quadrado é: {dobro_area:.2f} unidades quadradas")
    print("=" * 40)


def main():
    """
    Função principal que orquestra as demais funções e exibe o resultado final.
    """
    lado = obter_lado_quadrado()
    area = calcular_area_quadrado(lado)
    dobro_area = calcular_dobro_area(area)
    exibir_resultados(lado, area, dobro_area)


# Chama a função principal para executar o programa
main()
