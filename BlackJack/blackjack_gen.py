#!/usr/bin/env python3
class	Card:
  ACE, JACK, QUEEN, KING = 'A', 'J', 'Q', 'K'
  FACES	=	(ACE, 2, 3,	4, 5,	6, 7, 8, 9, 10, JACK, QUEEN, KING)
  SUITS	=	tuple(map(chr,	(9824,	9827,	9829,	9830)))
  SPADE, CLUB, HEART, DIAMOND = SUITS	#	♠	♣	♥	♦
  def	__init__(self, suit, face):
    self._suit =	suit
    self._face =	face
  def	__int__(self):
    if self._face in {Card.JACK, Card.QUEEN, Card.KING}:
      return	10
    return 1 if self._face == Card.ACE else self._face
  def	__str__(self):
    return self._suit	+	str(self._face)
  def	__repr__(self):
    return __class__.__name__ + repr((self._suit, self._face))

class	Deck:
  def	__init__(self):
    self._deck = [Card(suit, face) for suit in Card.SUITS for face in Card.FACES]
  def	shuffle(self):
    import random
    random.shuffle(self._deck)
  def	__iter__(self):
    return iter(self._deck)

def	Dealer():
  player = Player()
  D	=	Deck()
  D.shuffle()
  it = iter(D)
  ans	=	next(player) #	let	player run,	expect hardwired "yes"
  total	=	0
  while	ans	== 'yes':
    c	=	next(it) #	draw next card
    total	+= int(c)
    print(f'your card: {c}, ', end='')
    ans	=	player.send(c)
  if ans in {'lost', 'won'}:
    print(f'you	{ans}')
  else: # ans = no, draw one more	card and see
    c	=	next(it)
    print(f'next card: {c}, you '+ ('lost' if total+int(c) <= 21 else 'won'))

def	Player():
  c	=	yield('yes')
  total	=	int(c)
  while	total	<	21:
    ans	=	input(f'total = {total}, more card? [y/n] ')
    if ans not in	{'Y',	'y'}:	#	assume	no	if	not	yes
      yield("no") #	does	not	come	back
    else:
      c	=	yield("yes")
      total	+= int(c)	
  #	either	we	reached	or	exceeded	21,	so	no	more	card
  yield 'lost' if	total	>	21 else 'won'

if __name__ == '__main__':
  Dealer()