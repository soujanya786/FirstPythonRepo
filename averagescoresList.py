"""This program is to make a
list of scores and find the average of it"""


def main():
    # to get the score values from the user
    list_scores = get_scores()
    print("The score values entered are:",list_scores)
    #to add the scores in total
    total = add_scores(list_scores)
    len_scores = len(list_scores)
    Avg_scores = compute_average(len_scores,total)
    print("The total is",total)
    print("The average is",Avg_scores)

def compute_average(len_scores,total):
    Avg_scores = total / len_scores
    return Avg_scores

def add_scores(list_scores):
    total = 0
    for i in list_scores:
        total = total + i
    return total

#Gets the list of scores from the user
def get_scores():
    list_scores = []
    while True:
        score = int(input("Please enter the score(0 to stop):"))
        if score == 0:
            break
        list_scores.append(score)
    return list_scores


if __name__ == '__main__':
    main()
