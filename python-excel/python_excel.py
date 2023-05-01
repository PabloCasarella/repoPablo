from openpyxl import Workbook
from openpyxl.styles import Font
import time

libro = Workbook()
hoja = libro.active

hoja['A1'] = 5
hoja['A2'] = 10

