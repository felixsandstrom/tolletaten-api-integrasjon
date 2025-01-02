import requests

"""
Tolltariff og Tollavgift Oppslag Script

Dette scriptet lar brukeren søke etter tolltariffstrukturer og relaterte tollavgifter 
for en spesifisert vare ved bruk av toll.no API-er. Scriptet henter data fra to kilder:
1. Tolltariffstruktur: For å finne varen i tolltariffens hierarki (avsnitt, kapittel, posisjon).
2. Tollavgiftssatser: For å hente tollsatsen (TALL landgruppe) til varen.

Funksjonalitet:
- Søke etter en spesifikk vare basert på vare-id.
- Vise hierarkisk plassering (avsnitt, kapittel, posisjon, underposisjon) for varen.
- Hente og vise tollavgift for varen (TALL landgruppe).
"""

DATASET_URL = "https://data.toll.no/api/3/action/package_show?id=tolltariffstruktur"
TOLLAVGIFTSATS_URL = "https://data.toll.no/api/3/action/package_show?id=tollavgiftssats"

def hent_tolltariffstruktur():
    try:
        print("Henter dataset-metadata...")
        response = requests.get(DATASET_URL)
        response.raise_for_status()

        resource_url = next(
            (res["url"] for res in response.json()["result"]["resources"] if res["format"].upper() == "JSON"),
            None
        )
        if not resource_url:
            raise ValueError("Ingen gyldig JSON-ressurs funnet")

        print("Henter dataset-data...")
        data_response = requests.get(resource_url)
        data_response.raise_for_status()

        return data_response.json()
    except Exception as e:
        print(f"En feil oppstod ved henting av data: {e}")
        return None


def hent_tollavgiftsats():
    try:
        print("Henter tollavgiftsats-data...")
        response = requests.get(TOLLAVGIFTSATS_URL)
        response.raise_for_status()

        resource_url = next(
            (res["url"] for res in response.json()["result"]["resources"] if res["format"].upper() == "JSON"),
            None
        )
        if not resource_url:
            raise ValueError("Ingen gyldig JSON-ressurs funnet")

        print("Henter tollavgiftsats-data...")
        data_response = requests.get(resource_url)
        data_response.raise_for_status()

        return data_response.json()
    except Exception as e:
        print(f"En feil oppstod ved henting av data: {e}")
        return None


def finn_tollavgiftsats(vare_id, tollavgiftsats_data):
    for vare in tollavgiftsats_data.get("varer", []):
        if vare["id"] == vare_id:
            for avtale in vare.get("avtalesatser", []):
                if avtale["landgruppe"] == "TALL":
                    sats = avtale["sats"][0]
                    return {
                        "satsVerdi": sats["satsVerdi"],
                        "satsEnhet": sats.get("satsEnhetBeskrivelse", "Ingen beskrivelse"),
                        "fomdato": sats["fomdato"],
                        "tomdato": sats.get("tomdato", "Ubegrenset")
                    }
    return None


def finn_vare_hierarki(vare_id, data):
    for avsnitt in data.get("avsnitt", []):
        for kapittel in avsnitt.get("kapitler", []):
            for posisjon in kapittel.get("inndelinger", []):
                result = søk_oppdelinger(vare_id, posisjon)
                if result:
                    return avsnitt, kapittel, posisjon, result
    return None, None, None, None


def søk_oppdelinger(vare_id, oppdeling):
    if oppdeling.get("type") == "vare" and oppdeling.get("id") == vare_id:
        return {"type": "vare", "data": oppdeling}

    if oppdeling.get("type") == "underposisjon":
        for sub_oppdeling in oppdeling.get("oppdelinger", []):
            result = søk_oppdelinger(vare_id, sub_oppdeling)
            if result:
                return {"type": "underposisjon", "beskrivelse": oppdeling.get("beskrivelse"), "data": result["data"]}

    for sub_oppdeling in oppdeling.get("oppdelinger", []):
        result = søk_oppdelinger(vare_id, sub_oppdeling)
        if result:
            return result

    return None


def hovedprogram():
    # Fetch the datasets once
    data = hent_tolltariffstruktur()
    tollavgiftsats_data = hent_tollavgiftsats()

    if not data or not tollavgiftsats_data:
        print("Ingen data tilgjengelig. Avslutter.")
        return

    while True:
        print("\nTolltariff Oppslag")
        print("===================")
        vare_id = input("Skriv inn 'vare id' for å søke (eks. 01012100): ").strip()

        avsnitt, kapittel, posisjon, treff = finn_vare_hierarki(vare_id, data)

        if avsnitt and kapittel and posisjon and treff:
            tollavgift = finn_tollavgiftsats(vare_id, tollavgiftsats_data)
            print("\nResultater:")
            print(f"Avsnitt: {avsnitt['id']} - {avsnitt['beskrivelse']}")
            print(f"Kapittel: {kapittel['id']} - {kapittel['beskrivelse']}")
            print(f"Posisjon: {posisjon['id']} - {posisjon['beskrivelse']}")

            if treff["type"] == "underposisjon":
                print(f"  Underposisjon: {treff['beskrivelse']}")
                print(f"  Vare: {treff['data']['id']} - {treff['data']['vareslag']}")
            elif treff["type"] == "vare":
                print(f"  Vare: {treff['data']['id']} - {treff['data']['vareslag']}")

            if tollavgift:
                print(f"\nTollavgift (TALL):")
                print(f"  Sats: {tollavgift['satsVerdi']}")
                print(f"  Enhet: {tollavgift['satsEnhet']}")
                print(f"  Gyldig fra: {tollavgift['fomdato']} til {tollavgift['tomdato']}")
            else:
                print("\nIngen tollavgift funnet for denne varen.")
        else:
            print(f"Ingen treff funnet for vare id '{vare_id}'.")



if __name__ == "__main__":
    hovedprogram()


