def main():
    for i in range(1000, 10000):
        try:
            print(u"{}\t{}".format(i, chr(i)) , end="\n")
        except Exception:
            pass



if __name__ == "__main__":
    main()