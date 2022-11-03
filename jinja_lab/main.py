from jinja2 import Template
def add_spaces(text):
    return " ".join(text)

def discs(n):
    if n==1:
        return "дисциплина"
    if n == 2:
        return "дисциплины"
    if n==3:
        return "дисциплины"
    if n==4:
        return "дисциплины"
    if n==5:
        return "дисциплин"

student =[
 ["Алина", "Бизнес-информатика", ["Базы данных",
 "Программирование", "Эконометрика", "Статистика"], "ж"],
 ["Вадим", "Экономика", ["Информатика", "Теория игр",
 "Экономика", "Эконометрика", "Статистика"], "м"],
 ["Ксения", "Экономика", ["Информатика", "Теория игр",
 "Статистика"], "ж"]
 ]
f_template = open('ind_test_template.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
template = Template(html)
template.globals["add_spaces"] = add_spaces
template.globals["len"] = len
template.globals["discs"] = discs
result_html = template.render(user = student[2])
f = open('test.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()