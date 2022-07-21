def printlist(lista):
  for key,value in lista.items():
    print(key, "-",value)

def run():
  my_list = [x for x in range(1,100000) if x%4 == 0 and x%6==0 and x%9==0]
  print(my_list)


if __name__=='__main__':
  run()