from collections import deque

daily_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque(int(x) for x in input().split(", "))

peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
conquered_peaks = []

while daily_portions and daily_stamina:

    portion = daily_portions.pop()
    stamina = daily_stamina.popleft()

    result = portion + stamina

    if peaks:
        for peak, height in peaks.items():
            if result >= height:
                conquered_peaks.append(peak)
                del peaks[peak]
                break
            break

    if not peaks:
        break

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(peak, end="\n") for peak in conquered_peaks]
