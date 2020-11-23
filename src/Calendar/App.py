import src.Calendar.Events as ce, src.Calendar.Gui as ci

if __name__ == '__main__':
    # Iniciamos la base de datos y lanzamos la interfaz creada
    ce.iniciar_bbdd()
    app = ci.App()