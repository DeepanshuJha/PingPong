# Ping Pong Game in Python using Turtle
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
<img src="pingPong.png" width="800" height="600" class="center">

## Change the Audio Code for Mac, Windows, Ubuntu
### Mac
```python
import os
os.system("afplay", "bounce.wav&") # & is for async
```

### Ubuntu
```python
import os
os.system("aplay", "bounce.wav&") # & is for async
```

### Window
```python
import winsound
winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
```

