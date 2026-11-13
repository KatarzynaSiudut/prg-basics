def f(dice):
  if not dice:
    return None

  max_digit = dice[0]
  max_count = 1
  current_digit = dice[0]
  current_count = 1

  for x in dice[1:]:
    if x == current_digit:
      current_count += 1
    else:
      current_digit = x
      current_count = 1

    # Update the maximum if the current streak is longer
    if current_count > max_count:
      max_count = current_count
      max_digit = current_digit

  return int(max_digit)