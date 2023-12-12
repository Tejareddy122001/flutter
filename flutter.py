import tkinter as tk
from datetime import datetime, timedelta
import winsound

class ReminderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Daily Reminder App")

        self.days_of_week = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ]

        self.times_of_day = [f"{hour:02d}:00" for hour in range(24)]

        self.activities = [
            "Wake up", "Go to gym", "Breakfast", "Meetings",
            "Lunch", "Quick nap", "Go to library", "Dinner", "Go to sleep",
        ]

        # Dropdown for day
        self.day_var = tk.StringVar(master)
        self.day_var.set(self.days_of_week[0])
        self.day_dropdown = tk.OptionMenu(master, self.day_var, *self.days_of_week)
        self.day_dropdown.pack()

        # Dropdown for time
        self.time_var = tk.StringVar(master)
        self.time_var.set(self.times_of_day[0])
        self.time_dropdown = tk.OptionMenu(master, self.time_var, *self.times_of_day)
        self.time_dropdown.pack()

        # Dropdown for activities
        self.activity_var = tk.StringVar(master)
        self.activity_var.set(self.activities[0])
        self.activity_dropdown = tk.OptionMenu(master, self.activity_var, *self.activities)
        self.activity_dropdown.pack()

        # Button to set reminders
        self.set_reminders_button = tk.Button(
            master, text="Set Reminders", command=self.set_reminders
        )
        self.set_reminders_button.pack()

    def set_reminders(self):
        selected_day = self.day_var.get()
        selected_time = self.time_var.get()
        selected_activity = self.activity_var.get()

        current_time = datetime.now()
        reminder_time = datetime.strptime(f"{selected_day} {selected_time}", "%A %H:%M")

        if current_time > reminder_time:
            reminder_time += timedelta(days=7)  # If the selected time has passed for the current week, schedule it for the next week.

        self.schedule_reminder(selected_activity, reminder_time)

    def schedule_reminder(self, activity, reminder_time):
        current_time = datetime.now()
        time_difference = reminder_time - current_time
        seconds_until_reminder = time_difference.total_seconds()

        self.master.after(
            int(seconds_until_reminder * 1000),
            lambda: self.show_reminder(activity),
        )

    def show_reminder(self, activity):
        tk.messagebox.showinfo("Reminder", f"Don't forget to {activity}!")
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
