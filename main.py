class Pes:

  def __init__(self, stekot,chodenie,hranie_sa):
    self.stekot = stekot
    self.chodenie = chodenie
    self.hranie_sa = hranie_sa

    def stekot(self):
      return self.stekot
    
    def chodenie(self):
      return self.chodenie
  
    def hranie_sa(self):
      return self.hranie_sa
    
p = Pes()
print(p.stekot())
#output: Stekam
print(type(p))
#output: <class main.Pes>
    