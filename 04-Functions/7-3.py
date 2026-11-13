def month(n):
  
  months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
  ]

  # Sprawdzenie, czy numer mieści się w zakresie od 1 do 12
  if 1 <= n <= 12:
    return months[n - 1]
  else:
    return "Invalid month number"
  






