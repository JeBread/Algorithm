string = input()
for st in string:
  if st.isupper():
    print(st.lower(), end='')
  else:
    print(st.upper(), end='')