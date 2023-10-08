# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

play_order={
  "RRRRR": 0, "RRPRR": 0, "RRSRR": 0,
  "RRRRP": 0, "RRPRP": 0, "RRSRP": 0,
  "RRRRS": 0, "RRPRS": 0, "RRSRS": 0,
  
  "RRRPR": 0, "RRPPR": 0, "RRSPR": 0,
  "RRRPP": 0, "RRPPP": 0, "RRSPP": 0,
  "RRRPS": 0, "RRPPS": 0, "RRSPS": 0,
  
  "RRRSR": 0, "RRPSR": 0, "RRSSR": 0,
  "RRRSP": 0, "RRPSP": 0, "RRSSP": 0,
  "RRRSS": 0, "RRPSS": 0, "RRSSS": 0,
  
  "RPRRR": 0, "RPPRR": 0, "RPSRR": 0,
  "RPRRP": 0, "RPPRP": 0, "RPSRP": 0,
  "RPRRS": 0, "RPPRS": 0, "RPSRS": 0,
  
  "RPRPR": 0, "RPPPR": 0, "RPSPR": 0,
  "RPRPP": 0, "RPPPP": 0, "RPSPP": 0,
  "RPRPS": 0, "RPPPS": 0, "RPSPS": 0,
  
  "RPRSR": 0, "RPPSR": 0, "RPSSR": 0,
  "RPRSP": 0, "RPPSP": 0, "RPSSP": 0,
  "RPRSS": 0, "RPPSS": 0, "RPSSS": 0,
  
  "RSRRR": 0, "RSPRR": 0, "RSSRR": 0,
  "RSRRP": 0, "RSPRP": 0, "RSSRP": 0,
  "RSRRS": 0, "RSPRS": 0, "RSSRS": 0,
  
  "RSRPR": 0, "RSPPR": 0, "RSSPR": 0,
  "RSRPP": 0, "RSPPP": 0, "RSSPP": 0,
  "RSRPS": 0, "RSPPS": 0, "RSSPS": 0,
  
  "RSRSR": 0, "RSPSR": 0, "RSSSR": 0,
  "RSRSP": 0, "RSPSP": 0, "RSSSP": 0,
  "RSRSS": 0, "RSPSS": 0, "RSSSS": 0,
  
  "PRRRR": 0, "PRPRR": 0, "PRSRR": 0,
  "PRRRP": 0, "PRPRP": 0, "PRSRP": 0,
  "PRRRS": 0, "PRPRS": 0, "PRSRS": 0,
  
  "PRRPR": 0, "PRPPR": 0, "PRSPR": 0,
  "PRRPP": 0, "PRPPP": 0, "PRSPP": 0,
  "PRRPS": 0, "PRPPS": 0, "PRSPS": 0,
  
  "PRRSR": 0, "PRPSR": 0, "PRSSR": 0,
  "PRRSP": 0, "PRPSP": 0, "PRSSP": 0,
  "PRRSS": 0, "PRPSS": 0, "PRSSS": 0,
  
  "PPRRR": 0, "PPPRR": 0, "PPSRR": 0,
  "PPRRP": 0, "PPPRP": 0, "PPSRP": 0,
  "PPRRS": 0, "PPPRS": 0, "PPSRS": 0,
  
  "PPRPR": 0, "PPPPR": 0, "PPSPR": 0,
  "PPRPP": 0, "PPPPP": 0, "PPSPP": 0,
  "PPRPS": 0, "PPPPS": 0, "PPSPS": 0,
  
  "PPRSR": 0, "PPPSR": 0, "PPSSR": 0,
  "PPRSP": 0, "PPPSP": 0, "PPSSP": 0,
  "PPRSS": 0, "PPPSS": 0, "PPSSS": 0,
  
  "PSRRR": 0, "PSPRR": 0, "PSSRR": 0,
  "PSRRP": 0, "PSPRP": 0, "PSSRP": 0,
  "PSRRS": 0, "PSPRS": 0, "PSSRS": 0,
  
  "PSRPR": 0, "PSPPR": 0, "PSSPR": 0,
  "PSRPP": 0, "PSPPP": 0, "PSSPP": 0,
  "PSRPS": 0, "PSPPS": 0, "PSSPS": 0,
  
  "PSRSR": 0, "PSPSR": 0, "PSSSR": 0,
  "PSRSP": 0, "PSPSP": 0, "PSSSP": 0,
  "PSRSS": 0, "PSPSS": 0, "PSSSS": 0,
  
  "SRRRR": 0, "SRPRR": 0, "SRSRR": 0,
  "SRRRP": 0, "SRPRP": 0, "SRSRP": 0,
  "SRRRS": 0, "SRPRS": 0, "SRSRS": 0,
  
  "SRRPR": 0, "SRPPR": 0, "SRSPR": 0,
  "SRRPP": 0, "SRPPP": 0, "SRSPP": 0,
  "SRRPS": 0, "SRPPS": 0, "SRSPS": 0,
  
  "SRRSR": 0, "SRPSR": 0, "SRSSR": 0,
  "SRRSP": 0, "SRPSP": 0, "SRSSP": 0,
  "SRRSS": 0, "SRPSS": 0, "SRSSS": 0,
  
  "SPRRR": 0, "SPPRR": 0, "SPSRR": 0,
  "SPRRP": 0, "SPPRP": 0, "SPSRP": 0,
  "SPRRS": 0, "SPPRS": 0, "SPSRS": 0,
  
  "SPRPR": 0, "SPPPR": 0, "SPSPR": 0,
  "SPRPP": 0, "SPPPP": 0, "SPSPP": 0,
  "SPRPS": 0, "SPPPS": 0, "SPSPS": 0,
  
  "SPRSR": 0, "SPPSR": 0, "SPSSR": 0,
  "SPRSP": 0, "SPPSP": 0, "SPSSP": 0,
  "SPRSS": 0, "SPPSS": 0, "SPSSS": 0,
  
  "SSRRR": 0, "SSPRR": 0, "SSSRR": 0,
  "SSRRP": 0, "SSPRP": 0, "SSSRP": 0,
  "SSRRS": 0, "SSPRS": 0, "SSSRS": 0,
  
  "SSRPR": 0, "SSPPR": 0, "SSSPR": 0,
  "SSRPP": 0, "SSPPP": 0, "SSSPP": 0,
  "SSRPS": 0, "SSPPS": 0, "SSSPS": 0,
  
  "SSRSR": 0, "SSPSR": 0, "SSSSR": 0,
  "SSRSP": 0, "SSPSP": 0, "SSSSP": 0,
  "SSRSS": 0, "SSPSS": 0, "SSSSS": 0}

def player(prev_play, opponent_history=[]):
  if not prev_play:
      prev_play = 'R'

  opponent_history.append(prev_play)
  prediction = 'P'

  if len(opponent_history) > 4:
    last_five = "".join(opponent_history[-5:])
    play_order[last_five] = play_order.get(last_five, 0) + 1
      
    potential_plays = [
      "".join([*opponent_history[-4:], v]) 
      for v in ['R', 'P', 'S']
    ]

    sub_order = {
      k: play_order[k]
      for k in potential_plays if k in play_order
    }

    if sub_order:
      prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]
