# This set of Talon commands allows you to use Talon to press NVDA keyboard shortcuts

nvda <user.keys>: key("insert:down {keys} insert:up")
    #generically presses nvda key and any other keys listed.  
nvda <user.modifiers> <user.unmodified_key>: key("insert:down {modifiers}-{unmodified_key} insert:up")
    #includes modifiers 
nvda ndva: key(insert:2)
    #restores the nvda key to it's original purpose??? is this one even necessary?  Probably should delete this later. 
<user.modifiers>: key("{modifiers}")
    #allows presssing of single modifier keys

#This is a helper command that specifically tells you the filepath and the line number a voice command is defined on. 
# So you can say things like 'locate nvda 1' 
# and talon will copy to the clipboard and speak out loud the file name, the file location, and the line number a voice command is defined. 

locate <user.text>$: user.talon_locate_rule(text)
    #locates where a voice command is defined. Example: locate nvda one results in it giving the path and line number the voice command nvda one is defined on. 
