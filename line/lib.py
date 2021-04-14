def find_initial_state_of_tape(ListInst):
    """ Функция предназначена для нахождения первоначального состояни
        согнутой ленты. 
        Создается список его размер такой же как размер параметра функции.
        Этот список предназначен для симуляции разгибания согнутой ленты
        Этот список является двумерным массивом.
        Первому элементу этого списка присваивается аргумент функции.
        Затем нужно поделить все элементы списка по полам для симуляцмм разгибания
        получившиеся полусписки записать в список для симуляции разгибания, для подробностей смотрите код  
    """
    #ListInst список моделирующий ленту в согнутом состояние
    
    #список моделирующий разгибание ленты
    vertical_tape = list()
    vertical_tape.append(ListInst)
    
    #моделирование сгибания
    #моделирование заканчивается когда толщина ленты становится 1 клетка что соответствует размерности элементов
    #vertical_tape в 1
    while len(vertical_tape[0]) > 1:
        #это пепеременная моделирует еще раз согнутую ленту
        tmp_vertical_tape = list(range(len(vertical_tape)*2))
        #цикл создан для прохода по всем элементам vertical_tape и деления их пополам
        #эти элементы являются согнутыми отрезками ленты
        for i in range(len(vertical_tape)):
            #сохраняем длинну отрезка который будем сгибать
            length_of_vertical_tape = len(vertical_tape[i])
            #находим середену где будем сгибать
            middle_index_of_vertical_tape = length_of_vertical_tape//2
            
            half_list_on_top = vertical_tape[i][middle_index_of_vertical_tape:length_of_vertical_tape]
            half_list_on_top.reverse()
            tmp_vertical_tape[len(vertical_tape)-i-1] = half_list_on_top
            
            half_list_on_bottom = vertical_tape[i][0:middle_index_of_vertical_tape]
            tmp_vertical_tape[len(vertical_tape)+i] = half_list_on_bottom
            
            
        vertical_tape = tmp_vertical_tape
        
    #так как при разгибании у нас получилась вертикальная лента ее низ оказался началомм ленты которую сгибали
    #чтобы перевести ее в нормальный вид мы должны записать ее в список где первый элемент соответвует началу ленты
    vertical_tape_normal = list()
    for value in vertical_tape:
        vertical_tape_normal.append(value[0])

    vertical_tape_normal.reverse()
    return vertical_tape_normal
