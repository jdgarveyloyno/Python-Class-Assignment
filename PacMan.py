from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=400)
canvas.pack()

board = []
file = open("shape.txt", "r")
for line in file:
    board.append(line)
file.close()

for row in range(len(board)):
    for col in range(len(board[row])):
        char = board[row][col]
    
        x1 = col * 40 + 10
        y1 = row * 40 + 10
        x2 = x1 + 40
        y2 = y1 + 40
        
        if char == "*":
            canvas.create_rectangle(x1, y1, x2, y2, fill="#ffffff")
            
        if char == 'P':
            canvas.create_arc(x1, y1, x2, y2, start=25, extent=315, fill="#ffff00", outline="#000", width=2)
            canvas.create_oval(x1 + 14, y1 + 6, x1 + 20, y1 + 12, fill="#000", width=0.1)

            
root.mainloop()
