Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> message = 'Hello, do you know my other computer is your computer?'
>>> print(message)
Hello, do you know my other computer is your computer?
>>> translated = ' '
>>> print(translated)
 
>>> i len(message) - 1
SyntaxError: invalid syntax
>>> i = len(message) - 1
>>> while i >= 0 :
	translated = translated + message[i]
	i = i - 1

	
>>> print(translated)
 ?retupmoc ruoy si retupmoc rehto ym wonk uoy od ,olleH
>>> 