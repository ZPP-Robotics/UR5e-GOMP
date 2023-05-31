import old_version_paths as ovp
from experiments_init import old_version_moveL


paths = [ovp.path1, ovp.path2, ovp.path3, ovp.path4, ovp.path5, ovp.path6, 
         ovp.path7, ovp.path8, ovp.path9, ovp.path10, ovp.path11, ovp.path12]

def run_experiment():
    print("start")
    print("Which path do you want to run?")
    path_id = int(input())
    print(paths[path_id-1])

    old_version_moveL(paths[path_id-1])

    print("done")
    print("Reverse movement?[y/n]")
    reverse = input()

    if reverse == "y":
        print("start")
        old_version_moveL(paths[path_id-1][::-1])
        print("done")

run_experiment()