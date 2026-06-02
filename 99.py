for dan in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(f"== {dan}단 ==")

    for num in range(1, 10):
        print(f"{dan} x {num} = {dan * num}")

    print()  # 단 사이에 빈 줄 출력