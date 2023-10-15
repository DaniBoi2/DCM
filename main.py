from pacemaker_gui import Pacemaker_GUI

try:
    if __name__ == "__main__":
        pacemaker = Pacemaker_GUI()
        pacemaker.run()
except Exception as e:
    print("The following error has occured: ", e)
