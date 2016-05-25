import os
def debug(leading_text, variable):
	if os.environ.get('MYDEBUG','0') == '1':
		print leading_text, variable

