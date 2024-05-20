import matplotlib.pyplot as plt


def mypie1():
    label1 = ['Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti']
    # labels=list(label1)
    sizes = [23, 27, 21]
    print(sizes)
    colors1 = ['yellowgreen', 'lightskyblue', 'magenta']
    # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
    plt.title("Games in PCGBM for various Graphics card")
    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    a = plt.show()
    print(a)


def mypie2():
    label1 = ['i3', 'i5', 'i7']
    # labels=list(label1)
    sizes = [25, 22, 24]
    print(sizes)
    colors1 = ['red', 'blue', 'magenta']
    # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
    plt.title("Games in PCGBM for various Processors")
    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    b = plt.show()
    print(b)


def mypie3():
    label1 = ['4GB', '8GB', '16GB']
    # labels=list(label1)
    sizes = [24, 19, 28]
    print(sizes)
    colors1 = ['lightskyblue', 'yellowgreen', 'brown']
    # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
    plt.title("Games in PCGBM for various RAM")
    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    c = plt.show()
    print(c)


def mypie4():
    label1 = ['Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100']
    # labels=list(label1)
    sizes = [14, 22, 20, 12, 3]
    print(sizes)
    colors1 = ['red', 'blue', 'magenta', 'yellowgreen', 'brown']
    # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
    plt.title("Games in PCGBM for various prices($)\n")
    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    d = plt.show()
    print(d)


def mypie5():
    label1 = ['40 to 60', '61 to 80', '81 to 100']
    # labels=list(label1)
    sizes = [3, 19, 48]
    print(sizes)
    colors1 = ['red', 'blue', 'cyan', ]
    # SPLIT_OF_GRAPH=(0,0,0,0,0.1,0,0,0,0)
    plt.title("Games in PCGBM for various Review Score out of 100\n")
    plt.pie(sizes, explode=None, labels=label1, colors=colors1, shadow=True, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    d = plt.show()
    print(d)


def bar1():
    import numpy as np
    import matplotlib.pyplot as plt
    objects = ('Geforce GTX 1050 Ti', 'Geforce GTX 1060', 'Geforce GTX 1070 Ti')
    y_pos = np.arange(len(objects))
    types = (23, 27, 21)
    plt.bar(y_pos, types, align='center', color='yellowgreen')
    plt.xticks(y_pos, objects)
    plt.ylabel('Number Of Games')
    plt.title('Number Of Games According to Graphics Card')
    plt.show()


def bar2():
    import numpy as np
    import matplotlib.pyplot as plt
    objects = ('i3', 'i5', 'i7')
    y_pos = np.arange(len(objects))
    types = (25, 22, 24)
    plt.bar(y_pos, types, align='center', color='lightgreen')
    plt.xticks(y_pos, objects)
    plt.ylabel('Number Of Games')
    plt.title('Number Of Games According to processor')
    plt.show()


def bar3():
    import numpy as np
    import matplotlib.pyplot as plt
    objects = ('4GB', '8GB', '16GB')
    y_pos = np.arange(len(objects))
    types = (24, 19, 28)
    plt.bar(y_pos, types, align='center', color='lightskyblue')
    plt.xticks(y_pos, objects)
    plt.ylabel('Number Of Games')
    plt.title('Number Of Games According to RAM')
    plt.show()


def bar4():
    import numpy as np
    import matplotlib.pyplot as plt
    objects = ('Free', '1 to 20', '$21 to $40', '$41 to $60', '$61 to $100')
    y_pos = np.arange(len(objects))
    types = (14, 22, 20, 12, 3)
    plt.bar(y_pos, types, align='center', color='brown')
    plt.xticks(y_pos, objects)
    plt.ylabel('Number Of Games')
    plt.title('Number Of Games According to Various prices($)')
    plt.show()


def bar5():
    import numpy as np
    import matplotlib.pyplot as plt
    objects = ('40 to 60', '61 to 80', '81 to 100')
    y_pos = np.arange(len(objects))
    types = (3, 19, 48)
    plt.bar(y_pos, types, align='center', color='magenta')
    plt.xticks(y_pos, objects)
    plt.ylabel('Number Of Games')
    plt.title('Number Of Games According to Various review score(out of 100)')
    plt.show()


forgraphs = input("IF YOU WANT TO SEE GRAPHS (ENTER Y) : ").lower()
if forgraphs == "y":
    print('Select the graph you want to see')
    print('1.Pie chart')
    print('2.Bar graph')
    choice = int(input('Enter choice of graphs : '))
    if choice == 1:
        print('1.Games in PCGBM for various Graphics card')
        print('2.Games in PCGBM for various Processors')
        print('3.Games in PCGBM for various RAM')
        print('4.Games in PCGBM for various prices($)')
        print("5.Games in PCGBM for various Review Score out of 100\n")

        choice1 = int(input('Enter choice of Pie Charts : '))
        if choice1 == 1:
            mypie1()
        elif choice1 == 2:
            mypie2()
        elif choice1 == 3:
            mypie3()
        elif choice1 == 4:
            mypie4()
        elif choice1 == 5:
            mypie5()
    elif choice == 2:
        print('1.Number Of Games According to Graphics Card')
        print('2.Number Of Games According to processor')
        print('3.Number Of Games According to RAM')
        print('4.Number Of Games According to Various prices($)')
        print('5.Number Of Games According to Various review score(out of 100)')
        choice3 = int(input('Enter the choice of Bar Graphs : '))
        if choice3 == 1:
            bar1()
        elif choice3 == 2:
            bar2()
        elif choice3 == 3:
            bar3()
        elif choice3 == 4:
            bar4()
        elif choice3 == 5:
            bar5()

    else:
        print("exiting")
else:
    print("exiting")
    exit()
