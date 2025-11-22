def shutdown(n,m):
    if (n=="yes" and m=="yes"):
        print("shutdown")
    elif (n=="no" or m =="no"):
        print("Abort shutdown")
    else:
        print("Sorry")
shutdown("yes","no")