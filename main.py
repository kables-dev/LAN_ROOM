"""
GIOVANI'S ROOM 

make it portable

"""
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header , Label, Input , Log

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""

class chat_log():
    def __init__(self):
        pass 

#type hints for the sake
class message():
    def __init__(self):
        self.text_message = text_message

class chat_room_app(App):
    CSS_PATH = "app.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def on_mount(self) -> None:
        self.screen.styles.background = "darkgreen"

    def compose(self) -> ComposeResult:
        #center the label and maybe add a border yk
        yield Label("Giovani's chat room")
        yield Log()
        #find somewhere to store these things
        yield Input(placeholder="send message")
        #make a better way to log oot 
        yield  Footer()


    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Triggered automatically when the user presses Enter in the Input field."""
        user_text = event.value 
    
    def on_ready(self) -> None:
        log = self.query_one(Log)
        log.write_line("Hello, World!")

        for _ in range(10):
            log.write_line(TEXT)
        
    def action_toggle_dark(self) -> None:
        self.theme = (
        "textual-dark" if self.theme == "textual-light" else "textual-light"
        )   


if __name__ == "__main__":
    app = chat_room_app()
    app.run()