from tkinter import *
from tkinter import ttk, tix, messagebox
from tkcalendar import Calendar
import sqlite3

#  ficha do cliente:
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

#  botão imagem:
from PIL import ImageTk, Image

#  compilar imagem dentro do codigo:
#  usar site: base64.guru
import base64

from CadastroPessoas import *
