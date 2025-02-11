def MatchHistory(region: str, puuid: str):
        return f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}"

def Match(region: str, matchid: str):
        return f"https://api.henrikdev.xyz/valorant/v4/match/{region}/{matchid}"