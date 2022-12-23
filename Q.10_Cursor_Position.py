# cursor_Position

import win32api
import win32api as a 

position =  a.GetCursorPos() 
print(f"The present cursor position is: {position}") 