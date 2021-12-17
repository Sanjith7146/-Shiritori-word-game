def main():
  
  wordDict = open("word_list.txt", "r")
  valid_words = wordDict.read().splitlines()
  
 
  used_words = []
  game_over = False
  
  print('How to play: Type a vaild word.The last letter of the word must be the same as the first letter of the next word you are going to type.Remember the word should not repeat!Good Luck! ')
  while not game_over:
    
    curr_word = input('Please type a word:')
    

    
 
    if curr_word not in valid_words:
      print("Sorry I do not recognise that word. Please check your spelling and try agian")
      game_over=True
    
    if len(used_words) > 0:
      
      if curr_word[0] != used_words[-1][-1]:
        print( "You didn't type a word starting with '" + used_words[-1][-1] + "'.")
        game_over=True
     
      elif curr_word in used_words:
        print("You entered a word that has been typed before.")
        game_over=True
        break
      else:
        game_over=False
      
    
   
    
    used_words.append(curr_word)
    
    
main()
