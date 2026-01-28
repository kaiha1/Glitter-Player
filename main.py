import os
import sys
import vlc
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QListWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QFileDialog,
    QListWidgetItem, QMainWindow, QToolBar, QStatusBar, QInputDialog,
    QMenu
)
from PyQt6.QtCore import QTimer

playlists = {}
current_playlist = None 

themes = {
    "Black": """
        QWidget { background-color: #121212; color: white; }
        QPushButton { background-color: #59D2FE; color: #0b1c2d; }
    """,

    "Pink": """
        QWidget { background-color: #1b0f17; color: #ffd6e8; }
        QPushButton { background-color: #ff7eb6; color: #1b0f17; }
    """,

    "Blue": """
        QWidget { background-color: #0b1c2d; color: #cfe9ff; }
        QPushButton { background-color: #59D2FE; color: #0b1c2d; }
    """,

    "Purple": """
        QWidget { background-color: #1a1026; color: #e6d9ff; }
        QPushButton { background-color: #9b7bff; color: #1a1026; }
    """,

    "White": """
        QWidget { background-color: #f4f4f4; color: #111; }
        QPushButton { background-color: #222; color: white; }
    """
}

# VLC directory 
os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")

# VLC player instance
player = vlc.MediaPlayer()
current_song_path = None 

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("GlitterMusic")
window.resize(900, 600)

# ui
title = QLabel("Glitter Player")
title.setStyleSheet("font-size: 24px; font-weight: bold;")

add_song_btn = QPushButton("꧁⎝ 𓆩༺✧  Add Song ✧༻𓆪 ⎠꧂")
play_btn = QPushButton("𝄞 Play")
pause_btn = QPushButton("♫ Pause")
stop_btn = QPushButton("■ Stop")

listening_label = QLabel("Listening time: 00:00:00")
listening_label.setStyleSheet("font-size: 14px;")

player = vlc.MediaPlayer()
current_song_path = None

listening_seconds = 0

timer = QTimer()
timer.setInterval(1000)  # 1 second

song_list = QListWidget()



# functions
def add_song():
    files, _ = QFileDialog.getOpenFileNames(
        window,
        "Select Songs",
        "",
        "Audio Files (*.mp3 *.wav *.ogg);;All files (*)"
    )
    for file_path in files:
        item = QListWidgetItem(os.path.basename(file_path))
        item.setData(256, file_path)
        song_list.addItem(item)

def play_song():
    global current_song_path

    item = song_list.currentItem()
    if not item:
        return
    
    file_path = item.data(256)

    if current_song_path != file_path:
        player.stop()
        media = vlc.Media(file_path)
        player.set_media(media)
        current_song_path = file_path
    

    

    player.play()

    if not timer.isActive():
        timer.start()
       
def pause_song():
    if player.is_playing():
        player.pause()
        timer.stop()

def stop_song():
    player.stop()

def apply_theme(name):
    if name in themes:
        window.setStyleSheet(themes[name])

def update_listening_time():
    global listening_seconds
    listening_seconds += 1

    hours = listening_seconds // 3600
    minutes = (listening_seconds % 3600) // 60
    seconds = listening_seconds % 60 

    listening_label.setText(
        f"Listening time: {hours:02d}:{minutes:02d}:{seconds:02d}"
    )
timer.timeout.connect(update_listening_time)

def create_playlist():
    global playlists

    name, ok = QInputDialog.getText(
        window,
        "New Playlist",
        "Playlist name:"
    )

    if not ok or not name:
        return

    selected_items = song_list.selectedItems()
    if not selected_items:
        return

    playlists[name] = [item.data(256) for item in selected_items]

    print(f"Created playlist '{name}' with {len(playlists[name])} songs")



# buttons
add_song_btn.clicked.connect(add_song)
play_btn.clicked.connect(play_song)
pause_btn.clicked.connect(pause_song)
stop_btn.clicked.connect(stop_song)
play_btn.clicked.connect(play_song)
pause_btn.clicked.connect(pause_song)
song_list.itemDoubleClicked.connect(play_song)


# layout
top_layout = QHBoxLayout()
top_layout.addWidget(add_song_btn)
top_layout.addStretch()

control_layout = QHBoxLayout()
control_layout.addWidget(play_btn)
control_layout.addWidget(pause_btn)
control_layout.addWidget(stop_btn)

main_layout = QVBoxLayout()
main_layout.addWidget(title)
main_layout.addLayout(top_layout)
main_layout.addWidget(song_list)
main_layout.addWidget(listening_label)
main_layout.addLayout(control_layout)

# CENTRAL WIDGET (THIS IS REQUIRED)
central_widget = QWidget()
central_widget.setLayout(main_layout)
window.setCentralWidget(central_widget)

toolbar = QToolBar("Main Toolbar")
window.addToolBar(toolbar)

theme_menu = QMenu(" Theme", window)

for theme_name in themes:
    action = QAction(theme_name, window)
    action.triggered.connect(lambda checked, t=theme_name: apply_theme(t))
    theme_menu.addAction(action)

toolbar.addAction(theme_menu.menuAction())

playlist_action = QAction("➕ Playlist", window)




#style
window.setStyleSheet("""

QLabel {
    font-size: 24px;
    font-weight: bold;
}
QPushButton {
    background-color: #59D2FE;
    color: #0b1c2d;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #3fc3f5;
}
QPushButton:pressed {
    background-color: #2ab3ec;
}
QListWidget {
    background-color: #1e1e1e;
    border-radius: 10px;
    padding: 6px;
}
""")

# show the app window ;)
window.show()
sys.exit(app.exec())