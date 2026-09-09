from graphix import Window, Rectangle, Polygon, Point, Line, Circle

def draw_blank_patch(win, x, y, colour):
    x_br = x + 100
    y_br = y + 100
    
    rect = Rectangle(Point(x, y), Point(x_br, y_br))
    
    rect.fill_colour = colour
    rect.outline_colour = colour
    rect.draw(win)

def draw_patch1(win, x, y, colour):
    for i in range(11):
        line = Line(Point(x + i * 10, y), Point((x + 100) - i * 10, (y + 100)))
        line.fill_colour = colour
        line.draw(win)
        
    for i in range(11):
        line = Line(Point(x, y + i * 10), Point((x + 100), (y + 100) - i * 10))
        line.fill_colour = colour
        line.draw(win)
    

def draw_patch2(win, x, y, colour):
    big_circle_y = y + 30
    for i in range(2):
        for i in range(5):
            big_circle_x = x + ((i * 20) + 10)
            cir = Circle(Point(big_circle_x, big_circle_y), 10)
            cir.fill_colour = colour
            cir.outline_colour = colour
            cir.draw(win)
        big_circle_y = y + 70
        
    
    small_circle_y = y + 30
    for i in range(2):
        for i in range(4):
            small_circle_x = x + (i * 20) + 20
            cir = Circle(Point(small_circle_x, small_circle_y), 5)
            cir.fill_colour = colour
            cir.outline_colour = colour
            cir.draw(win)
        small_circle_y = y + 70   
    
    
    for i in range(3):
        triangle1_y = y + (i * 40)
        for i in range(5):
            point1 = Point((x + (i * 20)), (triangle1_y))
            point2 = Point((x + (i * 20) + 20), (triangle1_y))
            point3 = Point((x + (i * 20) + 10), (triangle1_y +  20))
            
            tri = Polygon([point1, point2, point3])
            tri.fill_colour = colour
            tri.outline_colour = colour
            tri.draw(win)  
    
    
    for i in range(3):
        triangle2_y = y + (i * 40)
        for i in range(5):
            point1 = Point((x + (i * 20)), (triangle2_y + 20))
            point2 = Point((x + (i * 20) + 20), (triangle2_y + 20))
            point3 = Point((x + (i * 20) + 10), (triangle2_y))
            
            tri = Polygon([point1, point2, point3])
            tri.fill_colour = colour
            tri.outline_colour = colour
            tri.draw(win)

def draw_patchwork(size, col1, col2, col3):
    win = Window("", size * 100, size * 100)
    
    x = 0
    y = 0
    
    for row in range (size):
        y = row * 100
        for column in range (size):
            x = column * 100
            if (row == 0 and column < size - 1) or (column == 0 and row < size - 1):
                draw_patch2(win, x, y, col1)
            
            elif row + column == size - 1 and (row % 2 == 0):
                draw_patch1(win, x, y, col2)
            
            elif row + column > size - 1 and ((size - 1 - column) % 2 == 0):
                draw_patch1(win, x, y, col3)
                
            elif column > 0 and row > 0 and column < size - 1 and row < size - 1 and column + row < size - 1:
                draw_blank_patch(win, x, y, col1)

            elif row + column == size - 1:
                draw_blank_patch(win, x, y, col2)

            elif row + column > size - 1:
                draw_blank_patch(win, x, y, col3)
                
    win.get_mouse()
    win.close()


def colour_input():
    allowed_colours = ["red", "green", "blue", "pink", "orange", "purple"]
    selected_colours = []
    
    for i in range(3):
        while True:
            colour = input("Enter a colour (red, green, blue, pink, orange, or purple):")
        
            colour.strip()
            colour.lower()
        
            if colour in allowed_colours and colour not in selected_colours:
                print("Colour is allowed")
                selected_colours.append(colour)
                break
            
            else:
                print("Either not allowed or already selected")
    
    return selected_colours
            

def get_size_input():
    allowed_sizes = [5, 7, 9]
    while True:
        size = input("Enter a size (5, 7, or 9): ")
        
        size.lower()
        
        if not size.isdigit():
            print("this input is not a number. Try again.")
            continue
        
        size = int(size)
        
        if size in allowed_sizes:
            return size
        
        else:
            print("Input is not allowed. Please enter 5, 7, or 9.")


def main():
    
    selected_colours = colour_input()
        
    size = get_size_input()
    
    draw_patchwork(size, selected_colours[0], selected_colours[1], selected_colours[2])


main()