# freddypi

## Installs
pip install httpserver gpiozero pigpio --user

## Protocol
All requests are get-requests to the root.

Header-Fields:
* Conent-Type: application/json
### Move
```
{
	'command': 'move',
	'parameter': {
		'direction': <STRING>
		'speed': <INTEGER>
	}
}
```
Parameters:
* direction: Describes the direction the robot should go. Possible values are: 'left', 'right', 'forward', 'backward'
* speed: Describes the percentage of speed. Ranges between 0 and 100.

Example:
```
{
	'command': 'move',
	'parameter': {
		'direction': 'forward'
		'speed': 75
	}
}
```
### Light
```
{
	'command': 'light',
	'parameter': {
		'mode': <STRING>
	}
}
```
Parameters:
* mode: Describes the mode the lights should be in. Modes are: 'blink', 'off'

Example:
```
{
	'command': 'light',
	'parameter': {
		'mode': 'blink'
	}
}
```
### Buzzer
```
{
	'command': 'buzzer',
	'parameter': {
		'mode': <STRING>
	}
}
```
Parameters:
* mode: Describes the mode the buzzer should be in. Modes are: 'alarm', 'off'

Example:
```
{
	'command': 'buzzer',
	'parameter': {
		'mode': 'alarm'
	}
}
```
### LCD
```
{
	'command': 'lcd',
	'parameter': {
		'text': <STRING>
	}
}
```
Parameters:
* mode: Describes the string the lcd displays should show.

Example:
```
{
	'command': 'lcd',
	'parameter': {
		'text': 'Your car sucks!'
	}
}
```
