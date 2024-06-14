def enthält(self, symbol: str) -> bool:
    if self.arena[(0, 0)] == symbol:
        return True 
    if self.arena[(1, 0)] == symbol:
        return True 
    if self.arena[(2, 0)] == symbol:
        return True 
    if self.arena[(0, 1)] == symbol:
        return True 
    if self.arena[(0, 2)] == symbol:
        return True 
    if self.arena[(1, 1)] == symbol:
        return True 
    if self.arena[(1, 2)] == symbol:
        return True 
    if self.arena[(2, 1)] == symbol:
        return True 
    if self.arena[(2, 2)] == symbol:
        return True 