def holidaybush(n):     # definicja funkcji - funkcja budująca choinkę rozmiaru n
	for i in range(n):
		print(("+" * (i * 2 + 1)).center(n * 2 - 1))
	print(("|").center(n * 2 - 1))
	print(("|").center(n * 2 - 1))


holidaybush(5)          # wywołanie funkcji - wydrukuj choinkę rozmiaru 5

# for i in range(n): - kręć pętlę, startując po kolei od i = 0 do i = n-1
# print("text")      - wypisz "text" na konsoli
# print(var)         - wypisz zawartość zmiennej var na konsoli
# ("text").center(n) - rozpaśnij text, aby zajmował n linijek i był wyśrodkowany
#                      np. ("abc").center(7) zzwróci wynik "  abc  "
#                      np. s.center(7) zzwróci wynik "  abc  ", jeżeli s="abc"