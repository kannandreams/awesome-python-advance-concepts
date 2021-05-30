from deprecated import deprecated

@deprecated("method renamed as generic name")
def sms_notify(value):
    print(value)


def notify(value):
    print(value)

if __name__ == '__main__':
    sms_notify("sms")
    notify("sms")

