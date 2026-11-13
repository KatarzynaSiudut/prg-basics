def month(n):
    months = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad","grudzien"]

    if 1 <= n <= 12:
        return months[n - 1]
    else:
        return "invalid month number"
