import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import keyboard
from plyer import notification

# Initialize application and global variables
text = "KeyMuter"
is_block = 0
tray_icon = None
mute_action = None
unmute_action = None

# Function to mute the keyboard
def muter():
    global text, is_block, mute_action, unmute_action
    if is_block == 0:
        text = "Keys are Muted"
        update_tooltip(tray_icon, text)
        notification.notify(title="KeyMuter", message="Your keys are Muted", timeout=5)
        for i in range(256):
            keyboard.block_key(i)
        is_block = 1
        unmute_action.setChecked(False)
        mute_action.setChecked(True)

# Function to unmute the keyboard
def unmuter():
    global text, is_block, mute_action, unmute_action
    if is_block == 1:
        text = "Keys are UnMuted"
        update_tooltip(tray_icon, text)
        notification.notify(title="KeyMuter", message="Your keys are UnMuted", timeout=5)
        for i in range(256):
            keyboard.unblock_key(i)
        is_block = 0
        unmute_action.setChecked(True)
        mute_action.setChecked(False)

# Function to update the tooltip of the system tray icon
def update_tooltip(tray_icon, new_text):
    tray_icon.setToolTip(new_text)

# Main function to set up the application and system tray
def main():
    global tray_icon, mute_action, unmute_action
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    tray_icon = QSystemTrayIcon(QIcon("icon.png"), app)
    tray_icon.show()
    tooltip_text = text
    tray_icon.setToolTip(tooltip_text)
    menu = QMenu()
    mute_action = QAction("Mute", triggered=muter, checkable=True)
    menu.addAction(mute_action)
    unmute_action = QAction("UnMute", triggered=unmuter, checkable=True)
    unmute_action.setChecked(True)
    menu.addAction(unmute_action)
    tray_icon.setContextMenu(menu)
    sys.exit(app.exec_())

# Placeholder function for showing notifications (not currently used)
def show_notification():
    pass

if __name__ == "__main__":
    main()
