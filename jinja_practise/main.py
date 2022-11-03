from jinja2 import Template
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def create_pict(x, y):

 #Построить линию графика, установить для нее цвет и толщину:
 line = plt.plot(x, y)
 plt.setp(line, color="blue", linewidth=2)
 # Вывести 2 оси, установить их в позицию zero:
 plt.gca().spines["left"].set_position("zero")
 plt.gca().spines["bottom"].set_position("zero")
 plt.gca().spines["top"].set_visible(False)
 plt.gca().spines["right"].set_visible(False)

 # Сохранть результат построения в файл:
 plt.savefig("pict.jpg")

 # Вернуть имя созданного файла
 return "pict.jpg"

def f_x(x, n_var):
 if n_var == 0:
    return x ** 3 - 6 * x ** 2 + x + 5
 elif n_var == 1:
    return x ** 2 -5 * x +1
 elif n_var == 2:
    return 1 / (x ** 2 + 1)

n_var = 2
a = -6
b = 6
n = 60
h = (b-a)/n

x_list = list()
f_list = list()

for j in range (0, 3):
    x_temp_list = list()
    f_temp_list = list()
    for i in range(0, n + 1):
        x_temp_list.append(a + i * h)
        f_temp_list.append(f_x(a + i * h, j))
    x_list.append(x_temp_list)
    f_list.append(f_temp_list)
print(f_list)

list_f = ["f(x)", "y(x)", "z(x)"]

name_pict = create_pict(x_list[n_var], f_list[n_var])

# Прочитать шаблон из файла function_template.html
f_template = open('function_template.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# Создать объект-шаблон
template = Template(html)
template.globals["round"] = round
# Указать, что в шаблоне будет использована функция len
template.globals["len"] = len
#Cоздадать файл для HTML-страницы
f = open('function.html', 'w', encoding ='utf-8-sig')
# Сгенерировать страницу на основе шаблона
result_html = template.render( x = x_list,
                               round=round,
                               n_var = n_var,
                               pict = "pict.jpg",
                                y = f_list,
                               list_f = list_f,
                               a=a, b=b, h=h, n=n
 )
# Вывести сгенерированную страницу в файл
f.write(result_html)
f.close()