def find_initial_state_of_tape(ListInst):
    
    vertical_tape = list()
    vertical_tape.append(ListInst)
    
    while vertical_tape[0].__len__() > 1:
        tmp_vertical_tape = list(range(vertical_tape.__len__()*2))
        for i in range(vertical_tape.__len__()):
            length_of_vertical_tape = vertical_tape[i].__len__()
            middle_index_of_vertical_tape = length_of_vertical_tape//2
            
            half_list_on_top = vertical_tape[i][middle_index_of_vertical_tape:length_of_vertical_tape]
            half_list_on_top.reverse()
            tmp_vertical_tape[vertical_tape.__len__()-i-1] = half_list_on_top
            
            half_list_on_bottom = vertical_tape[i][0:middle_index_of_vertical_tape]
            tmp_vertical_tape[vertical_tape.__len__()+i] = half_list_on_bottom
            
            
        vertical_tape = tmp_vertical_tape
    vertical_tape_normal = list()
    for value in vertical_tape:
        vertical_tape_normal.append(value[0])
    
    return vertical_tape_normal
