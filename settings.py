#Узнаём операционну систему
from sys import platform

## выясняем размер экрана пользователя
if platform == "linux" or platform == "linux2":
    from screeninfo import get_monitors
    m = get_monitors()[0] #получем первый монитор
    data = str(m).split(',') #разделяем данные на части для обработки
    USER_SCREEN_W = int(data[2].split('=')[1]) #Ширина
    USER_SCREEN_H = int(data[3].split('=')[1]) #Высота

elif platform == "darwin": #mac OS
    print(platform)

elif platform == "win32":
    import ctypes
    user32 = ctypes.windll.user32
    USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
