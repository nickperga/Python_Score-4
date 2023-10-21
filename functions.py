import csv

def create_table(rows, lines):
    row = ['|', '']
    table = [row * rows for i in range(lines)]
    for row in table:
        for elem in row:
            print(elem, end='\t')
        print()
    print("Table has been created!")
    return table
    
def table_add(player, row, table, empty_line):
    if(player == 1):
        table[empty_line[row - 1]][(row - 1) * 2 + 1] = player
        empty_line[row - 1] -= 1
    else:
        table[empty_line[row - 1]][(row - 1) * 2 + 1] = player
        empty_line[row - 1] -= 1

    for row in table:
        for element in row:
            print(element, end='\t')
        print()
    
    return table

def isFull(table):
    for element in table[0]:
        if(element == '|'):
            continue
        elif (element == ''):
            return False
    return True

def won_vertically(row, line, table, player, lines, rows):
    func_line = line - 1
    func_row = row
    counter = 1
    while(func_line >= 0):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_line -= 1
        else:
            break
    if(counter == 4):
        return True
    func_line = line + 1
    while(func_line < lines):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_line += 1
        else:
            break
    if(counter == 4):
        return True
    else:
        return won_horizontally(row, line, table, player, lines, rows)
    

def won_horizontally(row, line, table, player, lines, rows):
    func_line = line
    func_row = row - 1
    counter = 1
    while(func_row >= 0):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_row -= 1
        else:
            break
    if(counter == 4):
        return True
    func_row = row + 1
    while(func_row < rows):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_row += 1
        else:
            break
    if(counter == 4):
        return True
    else:
        return won_diagonally(row, line, table, player, lines, rows)
    

def won_diagonally(row, line, table, player, lines, rows):
    func_line = line - 1
    func_row = row - 1
    counter = 1
    while(func_row >= 0 and func_line >= 0):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_row -= 1
            func_line -= 1
        else:
            break
    if(counter == 4):
        return True
    func_row = row + 1
    func_line = line + 1
    while(func_row < rows and func_line < lines):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_row += 1
            func_line += 1
        else:
            break
    if(counter == 4):
        return True
    func_row = row - 1
    func_line = line + 1
    counter = 1
    while(func_line < lines and func_row >= 0):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_row -= 1
            func_line += 1
        else: 
            break
    if(counter == 4):
        return True
    func_row = row + 1
    func_line = line - 1
    while(func_line >= 0 and func_row < rows):
        if(table[func_line][(func_row - 1) * 2 + 1] == player):
            counter += 1
            func_row += 1
            func_line -= 1
        else:
            break
    if(counter == 4):
        return True
    else: 
        return False
    
    
def Player_plays(player, empty_line, table, lines, rows, counter):
    row = int(input("In which row you want to add a mark? "))
    while(empty_line[row - 1] == -1):
        print('The row you chose is full. Give another!')
        row = int(input("In which row you want to add a mark? "))
            
    table = table_add(player, row, table, empty_line)
    line_add = empty_line[row - 1] + 1
    if(counter >= 8):
        return won_vertically(row, line_add, table, player, lines, rows)
    else:
        return False


def Table_to_CSV(table,  rows, f_name, player_1_s, player_2_s, empty_lines):
    rows_T = [i for i in range(1, rows + 1)]
    with open(f_name, "w") as f:
        write = csv.writer(f)
        write.writerow(rows_T)
        write.writerows(table)
        write.writerow([player_1_s, 1])
        write.writerow([player_2_s, 2])
        write.writerow(empty_lines)


def CSV_to_Table(f_name):
    wrong = True
    while(wrong):
        try:
            with open(f_name, 'r') as f:
                csv_reader = csv.reader(f)
                table = list(csv_reader)
                wrong = False
                       
        except:
            print("You gave a wrong file name. Please try again more carefully.")
            f_name = input()
    rows = len(table[0])
    lines = 0
    for line in table:
        for element in line:
            if(element == '|'):
                lines += 1
                break
    table1 = []
    player_score_1 = -1
    player_score_2 = -1
    for line in table:
        if(len(line) == rows * 2):
            table1.append(line)
        elif (len(line) == 2):
            if(line[1] == '1'):
                player_score_1 = line[0]
            else:
                player_score_2 = line[0]
    empty_line = []
    for element in table[-2]:
        empty_line.append(int(element))
    print(table1)
    return rows, lines, table1, player_score_1, player_score_2, empty_line
