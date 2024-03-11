def tower_of_hanoi(n,src,helper,dest):
    if(n==1):
        print(f"Disk {n} moved from {src} to {dest}")
        return 0
    tower_of_hanoi(n-1,src,dest,helper)
    print(f"Disk {n} moved from {src} to {dest}")
    tower_of_hanoi(n-1,helper,src,dest)

tower_of_hanoi(3,"src","helper","dest")
