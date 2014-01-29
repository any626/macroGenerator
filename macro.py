class Macro:
    a = 30
    b = 48
    c = 46
    d = 32
    e = 18
    f = 33
    g = 34
    h = 35
    i = 23
    j = 36
    k = 37
    l = 38
    m = 50
    n = 49
    o = 24
    p = 25
    q = 16
    r = 19
    s = 31
    t = 20
    u = 22
    v = 47
    w = 17
    x = 45
    y = 21
    z = 44
    up = 57416
    left = 57416
    lctrl = 57373
    enter = 14
    header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Macro RepeatingMode=\"1\">"
    header_repeat = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Macro>"
    footer = "</Macro>"
    delay_open = "<DelayEvent>"
    delay_close = "</DelayEvent>"
    keydown = "<KeyBoardEvent Down=\"true\">"
    keyup = "<KeyBoardEvent Down=\"false\">"
    key_close = "</KeyBoardEvent>"
    
    def __init__(self,string, filename):
        self.string = string
        self.macro = None
        self.filename = filename

    def xml(self):
        file = open(self.filename, 'w+')
        file.write(header_repeat + '\n')
        #needs to be completed
        
    def stringToMacro(self):
        for x in self.string:
            #convert characters into hash
            macro = macro + characters[x]
            
                   
        
        
