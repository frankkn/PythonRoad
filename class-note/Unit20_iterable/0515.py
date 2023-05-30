def atom_gen(L):
  if L is None:
    return 
  if type(L) in {list, tuple}:
    for child in L:
      # for atom in atom_gen(child):
      #   yield atom
      yield from atom_gen(child)
  else:
    yield L
        
L = ['F1',['F4','F5',['F8']],'F2','F3','D3',['F6','F7']]
print([i for i in atom_gen(L)])