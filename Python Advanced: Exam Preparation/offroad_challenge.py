from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

