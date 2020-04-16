#Імпортуємо усі необхідні бібліотеки для подальшої роботи
import numpy as np
import random
import timeit


while True:
    #Просимо у користувача вибрати метод сортування.
    type_sort=input('Input number of which type of sort do you prefer: \
1 - bubble sort, 2 - selection sort, 3 - insertion sort, another is randomly: ')
    #Просимо у користувача вибрати як сортувати: зростання/падання.
    sort_for=input('Input word how do you want to sort: \
up - for growing, another for falling: ')
    #Просимо у користувача вибрати чи генерувати масив рандомно, чи вводити.
    inputting=input('Input "1" if you want to fill up the array randomly, \
another - by yourself: ')
    #Просимо у користувача вибрати розмірність масиву.
    size=int(input('Choose the type of matrix: '))
    
    if size<30:
        A=np.zeros(size, dtype=int) #Ініціалізуємо нашу матрицю, поки нулями.
    else:
        print('Choose size less than 30!')
        break
    
        
    #У цьому блоці коду ми встановлюємо усі необхідні величини для подальшої\
    #роботи з програмою.
    randomize=0
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    n=len(A)

    print()

    #Починаємо створювати функціями наші методи сортування.
    #У всіх функціях ми додатково встановлюємо лічильники для підрахунку: \
    #часу, обміну елементів та порівнянь.
    #Метод сортування бульбашкою (за зростанням).
    def bubble_sort(n):
        global count1
        global exchange1
        count1=0
        exchange1=0
        for i in range(1,n):
            for j in range(n-1, i-1, -1):
                count1+=1
                if (A[j-1]>A[j]):
                    exchange1+=1
                    A[j], A[j-1]=A[j-1], A[j]
        print(A)

    #Метод сортування бульбашкою (за спаданням).
    def bubble_sort_fall(n):
        global count1
        global exchange1
        count1=0
        exchange1=0
        for i in range(1,n):
            for j in range(n-1, i-1, -1):
                count1+=1
                if (A[j-1]<A[j]):
                    exchange1+=1
                    A[j], A[j-1]=A[j-1], A[j]
        print(A)

    #Метод сортування вибірково(за зростанням).
    def selection_sort(n):
        global count2
        global exchange2
        count2=0
        exchange2=0
        for i in range(n-1):
            min=i
            for j in range(i+1,n):
                count2+=1
                if A[j]<A[min]:
                    exchange2+=1
                    min=j
            A[i], A[min]=A[min], A[i]
        print(A)

    #Метод сортування вибором (за спаданням).
    def selection_sort_fall(n):
        global count2
        global exchange2
        count2=0
        exchange2=0
        for i in range(n-1):
            min=i
            for j in range(i+1,n):
                count2+=1
                if A[j]>A[min]:
                    exchange2+=1
                    min=j
            A[i], A[min]=A[min], A[i]
        print(A)

    #Метод сортування вставками (за зростанням).
    def insertion_sort(n):
        global count3
        global exchange3
        count3=0
        exchange3=0
        for i in range(1,n):
            j=i-1
            key=A[i]
            while j>=0 and A[j]>key:
                count3+=2
                exchange3+=1
                A[j+1]=A[j]
                j-=1
            A[j+1]=key
        print(A)

    #Метод сортування вставками (за спаданням).
    def insertion_sort_fall(n):
        global count3
        global exchange3
        count3=0
        exchange3=0
        for i in range(1,n):
            j=i-1
            key=A[i]
            while j>=0 and A[j]<key:
                count3+=2
                exchange3+=1   
                A[j+1]=A[j]
                j-=1
            A[j+1]=key
        print(A)


    #У наступному блоці коду ми створюємо для кожного методу сортування функцію,\
    #що оголосить нам результати: часу програми, обміну елементів, порівнянь.
    def times_bubble(t):
        print('Time of perfomrming: ', t)
        print('Amount of exchange: ', exchange1)
        print('Amount of comparisons: ', count1)

    def times_selection(t):
        print('Time of perfomrming: ', t)
        print('Amount of exchange: ', exchange2)
        print('Amount of comparisons: ', count2)

    def times_insertion(t):
        print('Time of perfomrming: ', t)
        print('Amount of exchange: ', exchange3)
        print('Amount of comparisons: ', count3)

    print()


    #Тут ми перевіряємо, як саме користувач хоче задати матрицю:
    #У if - рандомно.
    #У else - вводить самотужки із клавіатури.
    if inputting=='1':
        for i in range(len(A)):
            A[i]=random.randint(0,100000)
        print('Your array is randomly generated: ', A)

    else:
        if inputting!='1':
            for i in range(len(A)):
                A[i]=int(input('Input elements for your array: '))
            print('Your array is: ', A)

    print()


    print("Let's sort your array!")

    #Ну і, нарешті, перевірки на те, який метод вибрав користувач для сортування,\
    #Як саме він хоче відсортувати: за зростанням чи за спаданням?
    if type_sort=='1' and sort_for=='up': 
        print('Sorted by bubble method for growing: ')
        bubble_sort(n)
        times_bubble(t)


    elif type_sort=='1' and sort_for!='up':
        print('Sorted by bubble method for falling: ')
        bubble_sort_fall(n)
        times_bubble(t)

    elif type_sort=='2' and sort_for=='up':
        print('Sorted by selection sort for growing: ')
        selection_sort(n)
        times_selection(t)

    elif type_sort=='2' and sort_for!='up':
        print('Sorted by selection sort for falling: ')
        selection_sort_fall(n)
        times_selection(t)

    elif type_sort=='3' and sort_for=='up':
        print('Sorted by insertion sort for growing: ')
        insertion_sort(n)
        times_insertion(t)

    elif type_sort=='3' and sort_for!='up':
        print('Sorted by insertion sort for falling: ')
        insertion_sort_fall(n)
        times_insertion(t)

    #Блок коду, якщо користувач вибрав рандомну генерацію.
    elif type_sort!='1' or type_sort!='2' or type_sort!='3' and sort_for=='up':
        radomize=random.randint(1,3)
        if randomize==1:
            print('Sorted by bubble method for growing: ')
            bubble_sort(n)
            times_bubble(t)
        elif randomize==2:
            print('Sorted by selection sort for growing: ')
            selection_sort(n)
            times_selection(t)
        else:
            print('Sorted by insertion sort for growing: ')
            insertion_sort(n)
            times_insertion(t)


    elif type_sort!='1' or type_sort!='2' or type_sort!='3' and sort_for!='up':
        radomize=random.randint(1,3)
        if randomize==1:
            print('Sorted by bubble method for falling: ')
            bubble_sort_fall(n)
            times_bubble(t)
        elif randomize==2:
            print('Sorted by selection sort for falling: ')
            selection_sort_fall(n)
            times_selection(t)
        else:
            print('Sorted by insertion sort for falling: ')
            insertion_sort_fall(n)
            times_insertion

    else:
        print('An array cannot be sorted')

    #Чи бажаєте запустити програму заново?
    result=input('Input "1" to continue, and other to exit: ')
    if result=='1':
        continue
    break




            
                
            
            
                    
            




                     

