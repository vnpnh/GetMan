class Struct:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			if isinstance(value, dict):
				setattr(self, key, Struct(**value))
			else:
				setattr(self, key, value)

	def __repr__(self):
		attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
		return f'Struct({attributes})'

	def __str__(self):
		attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
		return f'Struct: {attributes}'

	def __getitem__(self, key):
		return getattr(self, key)

	def __setitem__(self, key, value):
		setattr(self, key, value)

	def __delitem__(self, key):
		delattr(self, key)
