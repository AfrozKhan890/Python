import tkinter as tk

# Constants
CELL_SIZE = 40
ROWS, COLS = 10, 10
ERASER_SIZE = 60

# Customizable colors
GRID_COLOR = 'red'  
ERASER_COLOR = 'yellow'    
BACKGROUND_COLOR = 'lightblue'  
BORDER_COLOR = 'black'    

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg=BACKGROUND_COLOR)
        self.canvas.pack()
        self.cells = []
        self.draw_grid()

        # Eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline=ERASER_COLOR, width=2)
        
        # Bind mouse movement
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def draw_grid(self):
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=GRID_COLOR, outline=BORDER_COLOR)
                row_cells.append(rect)
            self.cells.append(row_cells)

    def move_eraser(self, event):
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE

        self.canvas.coords(self.eraser, x1, y1, x2, y2)
        self.erase_cells(x1, y1, x2, y2)

    def erase_cells(self, x1, y1, x2, y2):
        for row in range(ROWS):
            for col in range(COLS):
                rect = self.cells[row][col]
                cell_coords = self.canvas.coords(rect)
                if self.overlaps(x1, y1, x2, y2, *cell_coords):
                    self.canvas.itemconfig(rect, fill='purple')  

    def overlaps(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

# Run the application
root = tk.Tk()
root.title("Canvas Eraser")
app = EraserCanvas(root)
root.mainloop()
