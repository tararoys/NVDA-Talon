# NVDA-Talon
No eyes.  No hands.  No need for headphones.  Complete control of your windows machine.   Very lightweight set of talon voice commands for interacting with NVDA 


Listen to the following podcast to see what it sounds like when you can have your computer talk to you, and you can give it orders back.  The following is a demonstration of using NVDA to read the screen outloud, using Talon voice control to allow the computer to accept your verbal orders, and what is possible when you install this particular set of files on your computer. 

https://youtu.be/TI7m049FgtE


## Installation and setup: 

1. This setup depends on having NVDA 2022.3.1 or later installed, following the installation instructions here: https://www.nvaccess.org/download/ 

IMPORTANT:  This script assumes the NVDA key is set to the INSERT key and none of the commands that start with NVDA will work unless the NVDA key is set to be 'insert.'  

2. This setup depends on having Talon voice installed, either via https://talonvoice.com/docs/index.html#getting-started or via the instrucitons on the installation video here: https://www.youtube.com/watch?v=XyooOp2ZXv0

Additionally, this script set depends on having the knausj-talon script set installed.  https://github.com/knausj85/knausj_talon#windows-setup

(Specifically, it depends on the files knausj_talon/core/key/keys.py and knausj_talon/core/key/keys.talon, and the files knausj_talon_core/numbers/numbers.talon, and knausj_talon/core/numbers/numbers.py which are the files in knuasj_talon that create the voice commands for simulating a keyboard and keyboard shortcuts.  While I haven't personally tested this, I *think* you could copy just those four files instead of the whole set.  The advantage to that is that you don't have 2000 extra unknown voice commands that you could accidentally give your computer- and instead, you have just the ones that simulate a keyboard.  The disadvantatge is that it's extra work and I haven't actually tested just using those four files.) 

3. So, if you have NVDA, Talon, and knausj_talon installed, you can install these scripts into the talon home directory (the same way you installed knausj talon) 

And then you will be able to to do everything I did in the podcast linked above.  

## Features

I call this this script set 'small' and 'lightweight' because all it does is allow you to speak NVDA keyboard shortcuts out loud instead of having to physically type them in.  This means that you need to know what the shortcuts are, and also how to translate them into Talon commands.  There are two main 'gotchas' when translating a typed keyboard shortcut into a talon verbal command, discussed in item 4.  However, what this means is if you are already a heavy user of NVDA, you can simply speak the keyboard shortcuts you already know instead of having to learn a whole new set of commands. 

This script set has four core features:  

### 1. Sleeping on Startup

  When Talon is started, it will start in sleep mode.  This means NVDA will not be able to immediately give it orders.  The component that does this is located in nvda.py.  https://github.com/tararoys/NVDA-Talon/blob/50d7233d8fa492bb5e2fc48b3636f614e1a66e4f/nvda.py#L51-L55

### 2. Listening when you say 'Listen' 

When in sleep mode, Talon is set up to ignore everything that does not start with the word 'listen'.  This setup is accomplished in the three 'momentary' files momentary.py, momentary.talon, and momentary-command.talon.  In order to get your computer to listen you you, you have to format your commands like 'listen one' or 'listen tab' or 'listen nvda f12'  

### 3. Speaking the NVDA Key

 To press a keyboard shortcut that includes the nvda key, you say NVDA and then you say the shortcut.  For example, the keyboard shortcut nvda-1 toggles on the nvda speak help feature, the one that lets you press keyboard shortcuts and hear a description of what they are supposed to do without actually doing them.  To toggle that on and off with Talon voice control under this setup, you wuld say 'listen nvda one'



### 4. NVDA Stops Talking When You Hiss At it.

Talon has the ability to recognize noises as well as voice commands.  This script set wired talon's 'hissing' noise to NVDA's shift key.


# Essential Knowledge:  

## Translating your keyboard shortcuts into their Equivalent Talon Commands

There are two main 'gotchas' when verbalizing an nvda command- first, Talon has it's own phonetic alphabet for all the letters, and second, the windows key is named 'super.' 

Talon voice control uses it's own phonetic alphabet.  In order to speak nvda keyboard shortcuts, you will need to know that phonetic alphabet.  This means that in order to press a shortcut like NVDA-t (the shortcut to read a window title) you need to say 'listen nvda trap' where 'trap' is the talon phonetic alphabet word for 't.' 

That alphabet is as follows: 

```
air 	a
bat 	b
cap 	c
drum 	d
each 	e
fine 	f
gust 	g
harp 	h
sit 	i
jury 	j
crunch 	k
look 	l
made 	m
near 	n
odd 	o
pit 	p
quench 	q
red 	r
sun 	s
trap 	t
urge 	u
vest 	v
whale 	w
plex 	x
yank 	y
zip 	z
```

The other main gotcha is that the talon name for the windows key is 'super', so if you are trying to access the windows start menu by pressing the windows key, you will need to say 'listen super' 

## Learning To Make the Noises to Get NVDA to stop Talking

This is set up to toggle speech on and off on two noises: a hiss and a pop.  The reason for these two noises is because these are the only two noises that are currently built into the free version of Talon.  If you want any other noises, you have to 1. pay for the current talon Beta and 2. do a boatload of configuration.  So if you want to not spend money and time, it's important to learn to make the two free noises the free version of Talon currently recognizes. 

in particular, when talon recognizes you making the following noise: 

https://noise.talonvoice.com/static/previews/hiss.mp3?add64163ccf7896c1c7f876d2ad70a6d

then it will press the shiftkey and nvda will stop talking- or start talking again.  

  The shift key pauses speach and then restarts it- so if you hiss while NVDA is talking, it will shut up, and if you hiss again, it will start again where it left off.  (This has all the usual caveats that NVDA has when using the shift key- in that it requires you to use very specific speach synthesizers like the built-in NVDA one or certain windows OneCore voices that are built to be able to do this.  

Known difficulties with using 'hiss' to get your computer to shush for a minute is that English has a lot of words that include hissing sounds, so if your microphone picks up a particularly siblant english word NVDA might shut up literally because you or your speach synthesizer said the word 'hiss' in a particularlly hissy accent.  

You may also notice in the code that I wired the 'pop' sound to toggle speech off and on.   While this works, many people find learning to make the 'pop' sound annoying.  

This is the 'pop' sound talon is looking for: 

https://noise.talonvoice.com/static/previews/pop.mp3?4ae02cb5221d89545ee24c9d2874650c

Instructions for how to make the sound can be found here:  https://github.com/talonvoice/noise/blob/master/noises.md#pop

Making The Sound

- Relax your jaw and keep your lips pressed very gently together
- Push a very tiny bit of air into your mouth, then quickly open your jaw, pulling your lips apart
- This should create a gentle pop sound that resonates within your mouth and cheeks
- This works best with a bit of moisture on your lips
- Not everyone can do this!

https://noise.talonvoice.com/static/previews/pop.mp3?4ae02cb5221d89545ee24c9d2874650c




## Setting Up Other Noises

It is *possible* to wire other sounds to do the same job. I, however, don't bother.  

If you do wish to bother- for example, if you have time and money and want to make it respont to a shhh noise,  see https://github.com/chaosparrot/parrot.py/blob/master/docs/TALON_VOICE.md  
