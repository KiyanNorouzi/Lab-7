import numpy as np 
import time 
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####




def OptimizerPerform():


    lst1 = [np.random.rand() for i in range(1000000)]
    lst2 = [np.random.rand() for i in range(1000000)]


    arr1 = np.random.rand(1000000)
    arr2 = np.random.rand(1000000)


    start = time.perf_counter()


    result = [lst1[i] * lst2[i] for i in range(len(lst1))]

    end = time.perf_counter()

    print(f"Время выполнения операции поэлементного перемножения для списка: {end - start:.5f} секунд")


    start = time.perf_counter()


    result = np.multiply(arr1, arr2)

    end = time.perf_counter()

    print(f"Время выполнения операции поэлементного перемножения для массива NumPy: {end - start:.5f} секунд")

def HistogramPerform():
    
    data=pd.read_csv('data2.csv')
    fig, ax = plt.subplots()
    bins = np.linspace(np.min(data['Hardness']), np.max(data['Hardness']), 20)
    ax.hist(data, bins=bins, edgecolor="blue")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram")
    plt.show()


    fig, ax = plt.subplots()
    bins = np.linspace(np.min(data['Hardness']), np.max(data['Hardness']), 20)
    ax.hist(data['Hardness'], bins=bins, density=True, edgecolor="blue")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    ax.set_title("Normalized histogram")
    plt.show()

    std = np.std(data)

    print("Standard deviation:", std)

def ThreeDimensionalGraph():

    def z_func(x, y):
        return np.sin(x)


    x = np.linspace(-np.pi, np.pi, 100)
    y = 1 / x
    X, Y = np.meshgrid(x, y)
    Z = z_func(X, Y)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    fig.colorbar(surf)

    ax.set_title('x∈(-п;п); y=1/x; z=sin(x)')

    plt.show()

def AnimatedGraph():
      
    def y_func(x):
        return np.sin(x)

    x = np.linspace(0, 2*np.pi, 100)

    fig, ax = plt.subplots()

    line, = ax.plot(x, y_func(x))

    def animate(i):
        y = y_func(x + i/10)
        
        line.set_ydata(y)
        
        return line,

    anim = FuncAnimation(fig, animate, frames=100, interval=50)

    writer = PillowWriter(fps=20)

    anim.save('sin.gif', writer=writer)

    plt.show()

OptimizerPerform() #1s Task 
HistogramPerform() #2nd Task
ThreeDimensionalGraph() #3rd Task
AnimatedGraph() #Дополнительное задание