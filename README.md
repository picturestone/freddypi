# freddypi

## Protocol
All requests are get-requests to the root.

Header-Fields:
* Conent-Type: application/json
### Move
```
{
	command: 'move',
	parameter: {
		leftwheel: <INTEGER>
		rightwheel: <INTEGER>
	}
}
```
Parameters:
* leftwheel: Describes the percentage of speed on the left wheel. Ranges between -100 and 100.
* rightwheel: Describes the percentage of speed on the right wheel. Ranges between -100 and 100.

Example:
```
{
	command: 'move',
	parameter: {
		leftwheel: 100,
		rightwheel: 50
	}
}
```
### Light
```
{
	command: 'light',
	parameter: {
		mode: <STRING>
	}
}
```
Parameters:
* mode: Describes the mode the lights should be in. Modes are: 'blink', 'off'

Example:
```
{
	command: 'light',
	parameter: {
		mode: 'blink'
	}
}
```
### Buzzer
```
{
	command: 'buzzer',
	parameter: {
		mode: <STRING>
	}
}
```
Parameters:
* mode: Describes the mode the buzzer should be in. Modes are: 'alarm', 'off'

Example:
```
{
	command: 'buzzer',
	parameter: {
		mode: 'alarm'
	}
}
```
### LCD
```
{
	command: 'lcd',
	parameter: {
		text: <STRING>
	}
}
```
Parameters:
* mode: Describes the string the lcd displays should show.

Example:
```
{
	command: 'lcd',
	parameter: {
		mode: 'Your car sucks!'
	}
}
```
