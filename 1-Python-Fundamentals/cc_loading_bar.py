def loading_bar(total):
    for amount_loaded in range(0, total + 1, 5):
        if amount_loaded == total * 0.25 // 1:
            print(f"{amount_loaded} 1/4 of the way there")
        elif amount_loaded == total * 0.5 // 1:
            print(f"{amount_loaded} 1/2 of the way there")
        elif amount_loaded == total * 0.75 // 1:
            print(f"{amount_loaded} 3/4 of the way there")
        elif amount_loaded == total:
            print(f"{amount_loaded} Loading Complete")
        else:
            print(amount_loaded)


loading_bar(100)
