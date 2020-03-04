#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import partners
from bcolors import bcolors
import os

def showStatus(showVotes):
  if (showVotes):
    partners.sort(key=lambda x: x['Votes'], reverse = True)
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

def getVotes(invalids, votes):
  votesRemaining(votes)
  print('>>> Agora digite')
  text = 'O numero do seu voto: '
  partnerVoted = int(input(text))
  points = [15,12,10,9,8]
  if partnerVoted not in invalids:
      power = points[votes - 1]
      t = '\tVoto validado! Você votou em {} com {} ponto(s).\n'.format(partners[partnerVoted-1]['Name'], power)
      bcolors.output(bcolors, t, bcolors.BOLD+bcolors.HEADER)
      partners[partnerVoted-1]['Votes'] += power
      votes -= 1
      invalids.append(partnerVoted)
  elif partnerVoted in invalids:
      t1 = '\tQuem está votando é {}'.format(partners[invalids[0]-1]['Name'])
      if partnerVoted == invalids[0]:
        t2 = '\tNão pode votar em si mesmo!'
      else:
        t2 = '\tNão pode votar 2x na mesma pessoa!'
      bcolors.output(bcolors, t1, bcolors.BOLD)
      bcolors.output(bcolors, t2, bcolors.UNDERLINE)
  return partnerVoted, votes, invalids

numberOfPartners = len(partners)
totalVotes = numberOfPartners - 1
while numberOfPartners > 0:
  votes = totalVotes
  whoAreVotingNow = whoAreYou(numberOfPartners)
  partnerVoted = None
  invalids = []
  invalids.append(whoAreVotingNow)
  while votes > 0 or partnerVoted == whoAreVotingNow:
    partnerVoted, votes, invalids = getVotes(invalids, votes)
  numberOfPartners -= 1
  # Clear the screen.
  os.system('clear')

showStatus(True)
