from winotify import Notification

toast = Notification(
    app_id="Warning!",
    title="Go to drink a water!",
    msg="It's important to stay hydrated. Please take a moment to drink some water.",
)

toast.show()