from talon import Module, actions, noise

noise_module = Module()

@noise_module.action_class
class NoiseActions:
    def noise_pop():
        """Invoked when the user does the pop noise."""
        pass

    def noise_hiss_start():
        """Invoked when the user starts hissing (potentially while speaking)"""
        pass

    def noise_hiss_stop():
        """Invoked when the user finishes hissing (potentially while speaking)"""
        pass

    
def hiss_handler(active):
    if active: 
        print('s')
        actions.key('shift')

def on_pop(active):
    print('pop')
    actions.key('shift')

noise.register("hiss", hiss_handler)
noise.register("pop", on_pop)
