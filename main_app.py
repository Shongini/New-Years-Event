import flet as ft
from flet import FilePicker
import json
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "guests": [], 
        "event_info": {"name": "Sylwester", "location": "Nieznane", "price_per_person": 0}, 
        "organizers": []
    }

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

async def main(page: ft.Page):
    page.title = "🎆 Sylwester Event Manager"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 800
    page.window_height = 700

    data = load_data()

    async def update_guest_list():
        guest_list_view.controls.clear()
        for i, guest in enumerate(data["guests"]):
            guest_list_view.controls.append(
                ft.ListTile(
                    title=ft.Text(guest["name"]),
                    subtitle=ft.Text(
                        "Zapłacono" if guest.get("paid") else "Brak wpłaty", 
                        color="green" if guest.get("paid") else "red"
                    ),
                    trailing=ft.Row([
                        ft.IconButton(icon="check", on_click=lambda e, idx=i: toggle_paid(idx)),
                        ft.IconButton(icon="delete", icon_color="red", on_click=lambda e, idx=i: delete_guest(idx)),
                    ], tight=True)
                )
            )
        page.update()

    async def add_guest(e):
        if new_guest_input.value:
            data["guests"].append({"name": new_guest_input.value, "paid": False})
            new_guest_input.value = ""
            save_data(data)
            await update_guest_list()

    async def delete_guest(idx):
        data["guests"].pop(idx)
        save_data(data)
        await update_guest_list()

    async def toggle_paid(idx):
        data["guests"][idx]["paid"] = not data.get("guests")[idx].get("paid", False)
        save_data(data)
        await update_guest_list()

    async def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        name = line.strip()
                        if name:
                            data["guests"].append({"name": name, "paid": False})
                save_data(data)
                await update_guest_list()

    file_picker = ft.FilePicker()
    file_picker.on_result = pick_files_result
    page.overlay.append(file_picker)

    # UI Components
    new_guest_input = ft.TextField(hint_text="Imię i Nazwisko", expand=True)
    add_button = ft.Button("Dodaj Gościa", icon="add", on_click=add_guest)
    import_button = ft.Button("Importuj z TXT", icon="upload_file", on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=["txt"]))
    guest_list_view = ft.ListView(expand=1, spacing=10, padding=10)

    # Views
    guest_view = ft.Column([
        ft.Row([new_guest_input, add_button]),
        ft.Row([import_button]),
        ft.Divider(),
        guest_list_view
    ], visible=True, expand=True)

    info_view = ft.Column([
        ft.Text("Szczegóły Wydarzenia", size=25, weight="bold"),
        ft.ListTile(leading=ft.Icon("location_on"), title=ft.Text(data["event_info"]["location"])),
        ft.ListTile(leading=ft.Icon("attach_money"), title=ft.Text(f"Cena: {data['event_info']['price_per_person']} zł/os")),
        ft.Divider(),
        ft.Text("Organizatorzy:", size=20),
        ft.Text(", ".join(data["organizers"]))
    ], spacing=10, visible=False, expand=True)

    async def nav_change(e):
        index = e.control.selected_index
        guest_view.visible = (index == 0)
        info_view.visible = (index == 1)
        page.update()

    # Navigation Bar
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="people", label="Lista Gości"),
            ft.NavigationBarDestination(icon="info", label="Informacje"),
        ],
        on_change=nav_change
    )

    # Header
    header = ft.Container(
        content=ft.Row([
            ft.Icon("celebration", size=40, color="amber"),
            ft.Text("Sylwester 2021/2022", size=30, weight="bold", color="amber"),
            ft.Icon("celebration", size=40, color="amber"),
        ], alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        bgcolor="surfacevariant",
        border_radius=10
    )

    page.add(
        header,
        ft.Column([guest_view, info_view], expand=True)
    )
    await update_guest_list()

ft.run(main)
