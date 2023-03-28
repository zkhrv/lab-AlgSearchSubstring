from Substring import boyer_moore, rabin_karp, kmp # импортируем написанный класс и методы класса
import timeit # импортируем библиотеку для подсчета времени работы алгоритмов
from prettytable import PrettyTable # импортируем библиотеку для красивого вывода результата работы программы
import re # импортируем библиотеку для работы с регулярными выражениями 

def read_file(file_path): # Функция для чтения файла 
    with open(file_path, 'r') as f: # открываем на чтение 
        return f.read() # возврат содержимого 
    
table = PrettyTable() # создаем таблицу
table.field_names = ["Измерение", "Результат"] # создаем два столбца с данными заголовками

def test_boyer_moore(file_path): # Тесты для функции boyer_moore
    text = read_file(file_path) # переменной text присваем текст из файла
    pattern = 'algorithm' # задаем паттерн поиска по тексту
    start_time = timeit.default_timer() # фиксируем время старта 
    result = boyer_moore(text, pattern) # переменной результат присваем результат работы алгоритма
    end_time = timeit.default_timer() # фиксируем время окончания работы
    count1 = end_time - start_time # вычисляем время работы алгоритма
    table.add_row(["Время работы алгоритма Бойера-Мура: ", "{:.8f}".format(count1)]) # выводим время работы
    table.add_row(["Результат работы алгоритма: ", len(result)]) # выводим результат работы. Функция len используется для определения количества найденных совпаденийвместо списка индексов найденных слов
    table.add_row(["Результат работы алгоритма (индексы вхождений): ", result])
    table.add_row(['-'*47, '-' * 13]) # разделитель в таблице
    
def test_rabin_karp(file_path): # Тесты для функции rabin_karp
    text = read_file(file_path) # переменной text присваем текст из файла
    pattern = 'algorithm' # задаем паттерн поиска по тексту
    start_time = timeit.default_timer() # фиксируем время старта 
    result = rabin_karp(text, pattern) # переменной результат присваем результат работы алгоритма
    end_time = timeit.default_timer() # фиксируем время окончания работы
    count2 =  end_time - start_time # вычисляем время работы алгоритма
    table.add_row(["Время работы алгоритма Рабина-Карпа: ", "{:.8f}".format(count2)]) # выводим время работы
    table.add_row(["Результат работы алгоритма: ", len(result)]) # выводим результат работы. Функция len используется для определения количества найденных совпаденийвместо списка индексов найденных слов
    table.add_row(["Результат работы алгоритма (индексы вхождений): ", result])
    table.add_row(['-'*47, '-' * 13]) # разделитель в таблице

def test_kmp(file_path): # Тесты для функции kmp
    text = read_file(file_path) # переменной text присваем текст из файла
    pattern = 'algorithm' # задаем паттерн поиска по тексту
    start_time = timeit.default_timer() # фиксируем время старта 
    result = kmp(text, pattern) # переменной результат присваем результат работы алгоритма
    end_time = timeit.default_timer() # фиксируем время окончания работы
    count3 =  end_time - start_time # вычисляем время работы алгоритма
    table.add_row(["Время работы алгоритма Кнута-Морриса-Пратта: ", "{:.8f}".format(count3)]) # выводим время работы
    table.add_row(["Результат работы алгоритма: ", len(result)]) # выводим результат работы. Функция len используется для определения количества найденных совпаденийвместо списка индексов найденных слов
    table.add_row(["Результат работы алгоритма (индексы вхождений): ", result])

if __name__ == '__main__':
    file_path = 'fileExample.txt' # путь к файлу 
    test_boyer_moore(file_path)
    test_rabin_karp(file_path)
    test_kmp(file_path)
    print(table) # вывод таблицы 

