class View:
    def __init__(self):
        ...

    async def start(self):
        ...

    async def end(self):
        ...

    async def update(self, dt):
        ...

    async def draw(self, surface):
        ...

    async def handle_event(self, event):
        ...

    async def on_mouse_move(self, event):
        ...

    async def on_mouse_click(self, event):
        ...

    async def on_key_press(self, event):
        ...