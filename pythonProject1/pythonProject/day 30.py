print("30 Days down - What did you think?")
for i in range(1,31):
    print(f"Day {i}:")
    remark = input("")
    conclude = f"""You thought day {i}  Was"""
    print(f"{conclude: ^50}")
    print("\033[34m",f"{remark: ^50}","\033[0m")