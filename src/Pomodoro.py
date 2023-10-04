import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer


class PomodoroTimer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Pomodoro Timer")

        # Create a countdown timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Create a label to display the countdown time
        self.timer_label = QLabel("25:00")

        # Create a button to start the timer
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)

        # Create a button to reset the timer
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)

        # Create a layout for the window
        layout = QVBoxLayout()
        layout.addWidget(self.timer_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)

        # Set the layout of the window
        self.setLayout(layout)

        # Set the minimum size of the window
        self.setMinimumSize(300, 200)

    def start_timer(self):
        # Set the countdown time
        self.countdown_time = 25 * 60

        # Start the timer
        self.timer.start(1000)

    def update_timer(self):
        # Decrement the countdown time
        self.countdown_time -= 1

        # Update the timer label
        self.timer_label.setText(
            f"{self.countdown_time // 60}:{self.countdown_time % 60:02}")

        # If the countdown time has reached zero, stop the timer and play a sound
        if self.countdown_time == 0:
            self.timer.stop()
            # Play a sound to indicate the end of the timer

    def reset_timer(self):
        # Reset the countdown time
        self.countdown_time = 25 * 60

        # Update the timer label
        self.timer_label.setText("25:00")

        # Stop the timer
        self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a Pomodoro timer window
    timer = PomodoroTimer()

    # Show the window
    timer.show()

    # Start the main event loop
    sys.exit(app.exec_())
