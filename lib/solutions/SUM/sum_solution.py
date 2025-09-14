
class SumSolution:
    
    def compute(self, x, y):
        if x > 100 or x < 0:
            raise ValueError(f"x={x} value out of bounds")
        if y > 100 or y < 0:
            raise ValueError(f"y={y} value out of bounds")
        return x + y
