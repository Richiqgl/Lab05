import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_cerca = None
        self._matricola = None
        self._nome= None
        self._cognome=None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.Dropdown(options=[])
        self._controller.popola_tendina()
            #label="name",
            #width=200,
            #hint_text="Insert a your name"


        # button for the "hello" reply
        self.btn_cerca = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.cercaIscritti)
        row1 = ft.Row([self.txt_name, self.btn_cerca],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        #riga 2
        self._matricola=ft.TextField(label="matricola",disabled=False,width=120)
        self._nome=ft.TextField(label="nome",disabled=False,width=120)
        self._cognome=ft.TextField(label="cognome",disabled=False,width=120)
        row2=ft.Row([self._matricola,self._nome,self._cognome],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #row3
        self._btncercaStudente=ft.ElevatedButton(text="Cerca Studente")#,on_click=self._controller.cercaIscritto)
        self._btncercacorsi=ft.ElevatedButton(text="Cerca corsi")#,on_click=self._controller.cercaCorsi)
        self.btnIscrivi=ft.ElevatedButton(text="Iscrivi")#,on_click=self._controller.iscrivi)
        row3=ft.Row([self._btncercaStudente,self._btncercacorsi,self.btnIscrivi],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
