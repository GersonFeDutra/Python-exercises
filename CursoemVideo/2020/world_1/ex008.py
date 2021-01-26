distance: float = float(input("Enter a distance (meters): "))

print(f'The distance has:'
      f'\n{distance / 1000}km'
      f'\n{distance / 100}hm'
      f'\n{distance / 10}dam'
      f'\n{distance * 10 :.0f}dm'
      f'\n{distance * 100 :.0f}cm'
      f'\n{distance * 1000 :.0f}mm'
)
