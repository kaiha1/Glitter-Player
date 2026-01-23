from PyQt6.QtWidgets import  (
    QApplication, QWidget,
    QPushButton, QListWidget, 
    QVBoxLayout, QHBoxLayout, QLabel,
    QFileDialog
)
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("GlitterMusic")
window.resize(900, 600)

def add_song():
    files, _ = QFileDialog.getOpenFileNames(
        window,
        "Select Songs",
        "",
        "Audio Files(*.mp3 *.wav *.ogg);;All files (*)"
    )
for file in files:
    song_list.addItem(file)

add_song_btn.clicked.connect(add_song)

title = QLabel("Glitter Player")
title.setStyleSheet("font-size: 20px; font-weight: bold;")

add_song_btn = QPushButton("Add song")
play_btn = QPushButton("Play")
pause_btn = QPushButton("Pause")

song_list = QListWidget()

top_layout = QHBoxLayout()
top_layout.addWidget(add_song_btn)
top_layout.addStretch()

control_layout = QHBoxLayout()
control_layout.addWidget(play_btn)
control_layout.addWidget(pause_btn)

main_layout = QVBoxLayout()
main_layout.addWidget(title)
main_layout.addLayout(top_layout)
main_layout.addWidget(song_list)
main_layout.addLayout(control_layout)


window.setLayout(main_layout)
window.setStyleSheet("""
QWidget {
    background-color: #b5b9ba;
    color: white;
    font-family: Arial;
}

QLabel {
    font-size: 20px;
    font-weight: bold;
}

QPushButton {
    background-color: #b5b9ba;
    color: black;
    padding: 10px;
    border-radius: 8px;
}

QPushButton:hover {
    background-color: #b5b9ba;
}

QListWidget {
    background-color: #1e1e1e;
    border-radius: 6px;
}
""")
window.setStyleSheet("""
QWidget {
    background-color: #b5b9ba;
    color: white;
    font-family: Arial;
}

QLabel {
    font-size: 20px;
    font-weight: bold;
}

QPushButton {
    background-color: #1DB954;
    color: black;
    padding: 10px;
    border-radius: 8px;
}

QPushButton:hover {
    background-color: #1ed760;
}

QListWidget {
    background-color: #1e1e1e;
    border-radius: 6px;
}
""")


window.show()

sys.exit(app.exec())
