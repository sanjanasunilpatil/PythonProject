class Demo:

    def calculate_probability(self, pE, sampleEvent):
        return pE/sampleEvent

d = Demo()

print("probability of drawing ace from cards ", d.calculate_probability(4, 52))

print("probability of drawing ace after drawing a king on 1st draw ", d.calculate_probability(4, 51))

print("probability of drawing ace after drawing an ace on 1st draw ", d.calculate_probability(3, 51))

print("probability of three heads, HHH ", d.calculate_probability(1, 8))

print("probability that you observe exactly one heads ", d.calculate_probability(3, 8))

print("probability that you observe at least two heads ", d.calculate_probability(4, 8))


