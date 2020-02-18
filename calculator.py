
import wx

class Calculator(wx.Panel):
    
    # variables for calculations 
    op = "" 
    result = 0 
    num1 = ""
    num2 = "" 
    flag = False # To check if ready to calculate or not
    displayString = ""
    
    # Color Variables 
    panelBackground = wx.Colour(45,49,64)
    btnBackground = wx.Colour(91,98,127)
    btnForground = wx.Colour(163,177,229)
    btnHover = wx.Colour(136,147,191)
    displayForground = btnForground = wx.Colour(222,223,224)
    
    
    def __init__(self,parent):
        super(Calculator,self).__init__(parent)
        self.SetBackgroundColour(self.panelBackground)
        '''
        ### Add label and buttons to the panel 
        '''
        self.display = wx.StaticText(self,pos=(0,25),size=(305,35),style=wx.TE_RIGHT) # CalculatorDisplay
        self.display.SetForegroundColour(self.btnForground)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.display.SetFont(font)
        
        # Buttons placement and styling
        font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        for indexY, row in enumerate(("789/","456*","123-",".0C+"),start=1):
            for indexX, char in enumerate(row,start=0):
                btn = wx.Button(self,label=char,style=wx.BORDER_NONE,size=(75,60),pos=(2+indexX*2+indexX*75,indexY*2+indexY*60))
                btn.SetBackgroundColour(self.btnBackground)
                if indexY == 4 and indexX == 2 :
                    btn.SetForegroundColour(wx.Colour(220,140,121))
                else:
                    btn.SetForegroundColour(self.btnForground)                
                btn.SetFont(font)
                btn.Bind(wx.EVT_BUTTON, self.OnBtnClicked)
                btn.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)
                btn.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        
        # Equal button        
        btn = wx.Button(self,label="=",style=wx.BORDER_NONE,size=(306,60),pos=(2,10+5*60))
        btn.SetBackgroundColour(self.btnBackground)
        btn.SetForegroundColour(self.btnForground)     
        btn.SetFont(font)
        btn.Bind(wx.EVT_BUTTON, self.OnBtnClicked)  
        btn.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)
        btn.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        
    def OnBtnClicked(self, event):
        lbl = event.GetEventObject().GetLabel() # Get the label from the clicked button
        
        
        if lbl == "+" or lbl == "-" or lbl == "*" or lbl == "/":
            if self.num1 == "":
                self.num1 = "0"
            self.DoOperation()
            self.op = lbl
        elif lbl == "C": # Clear display and reset variable
            self.ClearDisplay()
        elif lbl == "=":
            if self.num2 == "":
                result = self.CheckWholeNumber(float(self.num1))
                displayString = result
            else:
                self.DoOperation()            
        else:
            if self.op == "":
                if lbl == "." :
                    if "." not in self.num1:
                        self.num1 += "."
                else:
                    self.num1 += lbl
            else:
                if lbl == ".":
                    if "." not in self.num2:
                        self.num2 += "."    
                else:
                    self.num2 += lbl
                    self.flag = True
        
        
        self.displayString = self.num1 + self.op +self.num2
        self.display.SetLabel(self.displayString)
    
    def Calculate(self,num1,num2,op):
        if op == "+":
            return float(num1) + float(num2)
        elif op == "-":
            return float(num1) - float(num2)
        elif op == "*":
            return float(num1) * float(num2)
        elif op == "/":
            if(float(self.num2) == 0):
                wx.MessageBox("Can't devide with 0","Invalid operation")
                self.ClearDisplay()
            else:
                return float(num1) / float(num2)   
        
    def DoOperation(self):
        if self.flag == True:
            self.result = self.Calculate(self.num1,self.num2,self.op)
            self.num2 = ""
            self.op = ""
            if self.result != None:
                self.num1 = str(self.CheckWholeNumber(self.result))
            self.flag = False    
            
    def ClearDisplay(self):
        self.result = 0
        self.num1 = ""
        self.num2 = ""
        self.op = ""
        self.displayString = ""
    
    def CheckWholeNumber(self,num):
        if num.is_integer():
            return int(num)
        else:
            return num
        
    # change Button Color on MouseEnter event
    def OnMouseEnter(self,event):
        btn = event.GetEventObject()
        btn.SetBackgroundColour(self.btnHover)
        event.Skip()
    
    # Reset Button Color on MouseLeave event
    def OnMouseLeave(self,event):
        btn = event.GetEventObject()
        btn.SetBackgroundColour(self.btnBackground)
        event.Skip()    
            
class Frame(wx.Frame):
    def __init__(self,parent,title):
        super(Frame,self).__init__(parent,id=wx.ID_ANY,style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,title=title,size=(316,402))
        
        self.panel = Calculator(self) # Add a calculator panel to the frame
        self.SetIcon(wx.Icon("cal_icon.png")) # Set the icon

if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame(None,"Calculator")
    frame.Show(True)
    app.MainLoop()













































