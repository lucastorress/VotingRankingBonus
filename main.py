from config import partners
from bcolors import bcolors

def showStatus(showVotes):
  if (showVotes):
    t = '\t*** Votação finalizada ***'
    bcolors.output(bcolors, t, bcolors.BOLD+bcolors.WARNING)
  for index, partner in enumerate(partners):
    number = '{} '.format(index+1)
    name = '-> Nome: {} '.format(partner['Name'])
    # role = '-> Cargo: {} '.format(partner['Role'])
    votes = '-> Votos: {}'.format(partner['Votes'])
    if (showVotes):
      t = number+name+votes
      bcolors.output(bcolors, t, bcolors.BOLD+bcolors.OKBLUE)
    else:
      t = number+name
      bcolors.output(bcolors, t, bcolors.OKBLUE)

def votesRemaining(votes):
  showStatus(False)
  if votes > 1:
    v = 'votos'
  else:
    v = 'voto'
  t = '\tVocê tem apenas {} {}.'.format(votes, v)
  bcolors.output(bcolors, t, bcolors.BOLD+bcolors.OKGREEN)

def whoAreYou(partnerVoting):
  whoAreVotingNow = partnerVoting-1
  t1 = '>>> Quem está votando é {}'.format(partners[whoAreVotingNow]['Name'])
  t2 = '>>> Faltam {} pessoas votarem.'.format(whoAreVotingNow)
  bcolors.output(bcolors, t1, bcolors.BOLD+bcolors.HEADER)
  if whoAreVotingNow != 0:
    bcolors.output(bcolors, t2, bcolors.WARNING)
  return whoAreVotingNow+1

def getVotes(whoAreVotingNow, votes):
  votesRemaining(votes)
  print('>>> Agora digite')
  text = 'O numero do seu voto: '
  partnerVoted = input(text)
  if partnerVoted != whoAreVotingNow:
      t = '\tVoto validado! Você votou em {}.\n'.format(partners[partnerVoted-1]['Name'])
      bcolors.output(bcolors, t, bcolors.BOLD+bcolors.HEADER)
      partners[partnerVoted-1]['Votes'] += 1
      votes -= 1
  elif partnerVoted == whoAreVotingNow:
      t1 = '\tQuem está votando é {}'.format(partners[whoAreVotingNow-1]['Name'])
      t2 = '\tNão pode votar em si mesmo!'
      bcolors.output(bcolors, t1, bcolors.BOLD)
      bcolors.output(bcolors, t2, bcolors.UNDERLINE)
  return partnerVoted, votes

numberOfPartners = len(partners)
while numberOfPartners > 0:
  votes = 2
  whoAreVotingNow = whoAreYou(numberOfPartners)
  partnerVoted = None
  while votes > 0 or partnerVoted == whoAreVotingNow:
    partnerVoted, votes = getVotes(whoAreVotingNow, votes)
  numberOfPartners -= 1

showStatus(True)
