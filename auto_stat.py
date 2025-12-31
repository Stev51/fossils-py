import sys

if len(sys.argv) < 8:
    print(f"Proper usage: {sys.argv[0]} [stages] [HP] [ATK] [DEF] [SPA] [SPD] [SPE]")
    sys.exit(0)

stages: int = int(sys.argv[1])
HP: int = int(sys.argv[2])
ATK: int = int(sys.argv[3])
DEF: int = int(sys.argv[4])
SPA: int = int(sys.argv[5])
SPD: int = int(sys.argv[6])
SPE: int = int(sys.argv[7])
BST: int = HP + ATK + DEF + SPA + SPD + SPE

stats: list[int] = [HP, ATK, DEF, SPA, SPD, SPE]

for stage in range(1, stages+1):

    new_stats: list[int] = []
    stage_bst: int = round( float(BST) * (float(stage) / float(stages)) )
    stat_total: int = 0
    
    for stat in stats:
        new_stat = round( (float(stat) / float(BST)) * float(stage_bst) )
        new_stats.append(new_stat)
        stat_total += new_stat

    print()
    print(f"=== STAGE {stage} ===")
    print()
    print(f" HP: {new_stats[0]}")
    print(f"ATK: {new_stats[1]}")
    print(f"DEF: {new_stats[2]}")
    print(f"SPA: {new_stats[3]}")
    print(f"SPD: {new_stats[4]}")
    print(f"SPE: {new_stats[5]}")
    print()
    print(f"Recommended BST: {stage_bst}")
    print(f"Given BST: {stat_total}")

print()

