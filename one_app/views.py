#Задача 1
# from django.shortcuts import render
#
# def index(request):
#     fruits = ['яблоко', 'груша', 'слива']
#     return render(request, 'one_app/index.html', context={'fruits': fruits})

#Задача 2
# from django.shortcuts import render
#
# def index(request):
#     # Создаем пустой список для всей таблицы
#     table_data = []
#
#     # Внешний цикл по строкам (от 1 до 9)
#     for i in range(1, 10):
#         row = []  # Создаем пустую строку
#         # Внутренний цикл по столбцам (от 1 до 9)
#         for j in range(1, 10):
#             row.append(i * j)  # Добавляем результат умножения в строку
#         table_data.append(row)  # Добавляем готовую строку в общую таблицу
#
#     # Передаем готовую матрицу в шаблон
#     return render(request, 'one_app/index.html', {'index': table_data})

#Задание 3
# from django.shortcuts import render
#
# def index(request):
#     fruits = ['яблоко', 'груша', 'слива', 'апельсин', 'мандарин', 'юдзу', 'персика', 'слива', 'лимон']
#     return render(request, 'one_app/index.html', context={'fruits': fruits})

