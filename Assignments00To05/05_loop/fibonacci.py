MAX_term_value = 10000
def main():
   current_term = 0
   next_term = 1
   while current_term <= MAX_term_value :
       print(current_term)
       term_next = current_term + next_term
       current_term = next_term
       next_term = term_next



if __name__ == '__main__':
    main()