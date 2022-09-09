import cv2
import tkinter as tk
import imutils
from pytesseract import pytesseract
from PIL import Image, ImageTk
from googletrans import Translator 

root = tk.Tk()
root.title('Imagem em texto')
cap = cv2.VideoCapture(0)
video = None
frame = None
img_texto = None


def tradu():
    global img_texto
    try:
        traduzido = Translator().translate(text=img_texto, dest='pt').text
        text_box = tk.Text(root, height=12, width=74, padx=10, pady=15, font=("helvetica", 16), border=10, wrap='word')
        text_box.insert(1.0, traduzido)
        text_box.tag_configure("left", justify="left")
        text_box.tag_add("center", 1.0, "end")
        text_box.place(relx=0.5, rely=0.80, anchor=tk.CENTER)
    except:
        pass


def texto():
    global img_texto
    caminhot = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = caminhot
    img_texto = pytesseract.image_to_string("foto.jpg")
    text_box = tk.Text(root, height=12, width=74, padx=10, pady=15, font=("helvetica", 16), border=10, wrap='word')
    text_box.insert(1.0, img_texto)
    text_box.tag_configure("left", justify="left")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(relx=0.5, rely=0.80, anchor=tk.CENTER)


def foto():
    global frame
    cv2.imwrite("foto.jpg", frame)
    

def live_video():
    global video
    video = cv2.VideoCapture(0)
    iniciar()


def iniciar():
    global video
    global frame
    ret, frame = video.read()
    
    if ret == True:
        frame = imutils.resize(frame, width=640)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=img)
        BordaVideo.configure(image=image)
        BordaVideo.image = image
        BordaVideo.after(10, iniciar)
    else:
        video.release()


def fechar():
    global video
    #BordaVideo.place_forget()
    video.release()


# tamanho do monitor que acessou o programa
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# tamanho da tela do app
app_width = int(screen_width / 2)
app_height = int(screen_height / 1.2)

# pegando o ponto da tela pra por o app
x = (screen_width / 2) - (app_width / 2) 
y = (screen_height / 2) - (app_height / 2)
# parte de geometria q determina onde o app aparece na tela do usuario
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# tela do app
canvas = tk.Canvas(root, width=app_width, height=app_height)
canvas.grid(columnspan=3, rowspan=3)
logo = Image.open('fundo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(root, text="Iniciar video", command=live_video, width=10, height=2)
button.place(x=40, y=30)
button2 = tk.Button(root, text="Print", command=foto, width=10, height=2)
button2.place(x=40, y=70)
button3 = tk.Button(root, text="Texto", command=texto, width=10, height=2)
button3.place(x=40, y=110)
button4 = tk.Button(root, text="Traduzir", command=tradu, width=10, height=2)
button4.place(x=40, y=150)
button5 = tk.Button(root, text="Fechar video", command=fechar, width=10, height=2)
button5.place(x=40, y=190)

BordaVideo = tk.Label(root, bg="black")
BordaVideo.place(x=160, y=30)


root.protocol("WM_DELETE_WINDOW")
root.mainloop()

















