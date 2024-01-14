import matplotlib.pyplot as plt

def show_result(x, y):
    plt.plot(x, y, label='Rozkład temperatury')
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.title('Metoda Elementów Skończonych')
    plt.legend()
    plt.show()
    