from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast(
    'Python is here', 'Hello everybody!',
    duration=40, icon_path='../assets/img/bb8.ico'
)
