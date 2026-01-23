import os
import sys
import vlc
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QListWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QFileDialog
)

# VLC directory 
os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")

# VLC player instance
player = vlc.MediaPlayer()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("GlitterMusic")
window.resize(900, 600)

# ui
title = QLabel("Glitter Player")
title.setStyleSheet("font-size: 24px; font-weight: bold;")

add_song_btn = QPushButton("꧁⎝ 𓆩༺✧  Add Song ✧༻𓆪 ⎠꧂")
play_btn = QPushButton("𝄞 Play")
pause_btn = QPushButton("♫ Pause")
stop_btn = QPushButton("■ Stop")

song_list = QListWidget()

# functions
def add_song():
    files, _ = QFileDialog.getOpenFileNames(
        window,
        "Select Songs",
        "",
        "Audio Files (*.mp3 *.wav *.ogg);;All files (*)"
    )
    for file in files:
        song_list.addItem(file)

def play_song():
    current_item = song_list.currentItem()
    if current_item:
        file_path = current_item.text()
        player.stop()  # Stop any currently playing song
        player.set_mrl(file_path)
        player.play()

def pause_song():
    player.pause()

def stop_song():
    player.stop()

# buttons
add_song_btn.clicked.connect(add_song)
play_btn.clicked.connect(play_song)
pause_btn.clicked.connect(pause_song)
stop_btn.clicked.connect(stop_song)

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
main_layout.addLayout(control_layout)

window.setLayout(main_layout)

#style
window.setStyleSheet("""
QWidget {
    background-color: #121212;
    color: white;
    font-family: Arial;
}
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
