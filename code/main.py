#IMPORTS 

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label
import sqlite3
import milestone
import session

from finance import FinanceMenu

class MainMenu(App):
    """textual app with match cases mapped via buttons/clicks"""
    
    CSS = """
    Screen { 
        background: #1e1e1e;
        padding: 2;
    }
    Label {
        color: #ffffff;
        margin-bottom: 1;
    }
    Button {
        margin-bottom: 1;
        width: 100%;
        background: #34495e;
        color: white;

    }
    """ 

    def compose(self) -> ComposeResult:
        """defines the widgets that appear on the screen"""
        yield Header()
        yield Label("Welcome! What would you like to do today?")

        #BUTTONS
        #each button has unique id or it will result in the same action. i know you know duh, but... still left this here incase anyone doesnt understand why
        
        yield Button("Finances", id="btn_finance")
        yield Button("Milestones", id="btn_milestone")
        yield Button("Academics", id="btn_academics")
        yield Button("Sesssions", id="btn_session")
        yield Button("Exit", id="btn_exit", variant="error")

        #yield Button("", id="btn_update")
        
        
        
        yield Footer()



    def on_button_pressed(self, event: Button.Pressed) -> None:
        """ Handles all the button click events and describes the subsequent actions"""
        button_id = event.button.id or ""
        button_id = button_id.strip()
        if not button_id:
            return

        #button id value maps to the match case 
        match button_id:
    
            case "btn_finance":
                #finance.finance_handler()
                self.push_screen(FinanceMenu())
            case "btn_milestone":
                #milestone.milestone_handler()
                self.notify("Milestones underwork!")
            case "btn_academics":
                self.notify("Academics coming soon")
            case "btn_session":
                session.session_handler()
                self.notify("Sessions underwork!")
            case "btn_exit":
                self.exit()
            case "":
                pass
            case _:
                self.notify("Unknown button action! Please enter a valid input")

if __name__ == "__main__":
    app = MainMenu()
    app.run()



# while True:
#     choice = input(f"Type the name of the module you want access from the selection below.\n{('=' * width)}\n1. finance\n2. milestone\n3. session\n4. exit\n")
    
#     match choice:
#         case "finance":
#             finance.finance_handler()
#         case "milestone":
#             milestone.milestone_handler()
#         case "session":
#             session.session_handler()
#         case  "exit":
#             break