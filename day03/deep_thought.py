def answer(a):
    if a == '42' or a == 'forty-two' or a == 'forty two':
        return 'Yes'
    else:
        return 'No'
    
    
def main():
    q = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    print (answer(q.strip()))
    
if __name__ == "__main__":
    main()