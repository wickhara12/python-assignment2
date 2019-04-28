""" this is Rebecca's code for task 15 """
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


def graphs():
    x = ['Toy']
    y = [6]

    x2 = ['ToyBox']
    y2 = [5]

    plt.bar(x, y, color='c', align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('task 15')
    plt.ylabel('the total of different data in each class')
    plt.xlabel('class')

    plt.show()


#graphs()
