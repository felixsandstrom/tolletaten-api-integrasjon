
# Tolltariff og Tollavgift Oppslag | Tolltariff and Duty Lookup Tool

**Norwegian:**  
Tolltariff og Tollavgift Oppslag er et Python-basert verktøy designet for å hente og vise hierarkiske tolltariffstrukturer og tilhørende tollavgifter for spesifikke varer. Verktøyet bruker API-er fra toll.no for å hente sanntidsdata og gir detaljerte resultater om klassifikasjoner og tollsatser.

**English:**  
The Tolltariff and Duty Lookup Tool is a Python-based tool designed to fetch and display hierarchical tariff structures and related duty rates for specific goods. The tool uses APIs from toll.no to retrieve real-time data and provides detailed results on classifications and duty rates.

---

## Funksjoner | Features
- **Hierarkisk Strukturoppslag | Hierarchical Structure Lookup**:  
  Norwegian: Navigerer gjennom tolltariffens hierarki (avsnitt, kapittel, posisjon, underposisjon).  
  English: Navigates through tariff hierarchy (section, chapter, position, sub-position).

- **Detaljerte Tollsatser | Detailed Duty Rates**:  
  Norwegian: Henter tollsatser (TOLL) for varer og viser gyldighetsområder.  
  English: Fetches duty rates (TOLL) for goods and displays valid ranges.

- **Fleksible Spørringer | Flexible Queries**:  
  Norwegian: Lar brukeren søke etter varer ved hjelp av spesifikke ID-er.  
  English: Allows users to search for goods by their specific ID.

- **Sanntids API-integrasjon | Real-Time API Integration**:  
  Norwegian: Henter oppdaterte data fra toll.no-datasett.  
  English: Fetches the latest data from toll.no datasets.

---

## Mer Informasjon | More Information
**Norwegian:**  
For flere verktøy for å filtrere og analysere tolldata, besøk mitt nettsted [tollportalen.no](https://tollportalen.no). Der finner du en rekke ressurser som hjelper deg med å forstå og bruke tollrelatert informasjon mer effektivt.

**English:**  
For additional tools to filter and analyze customs data, visit my website [tollportalen.no](https://tollportalen.no). You’ll find a variety of resources to help you better understand and utilize tariff-related information.

---

## Forutsetninger | Prerequisites
- **Norwegian:** Python 3.7 eller nyere.  
  **English:** Python 3.7 or higher.  
- **Norwegian:** Nødvendige Python-biblioteker (installeres via `requirements.txt`).  
  **English:** Required Python libraries (installed via `requirements.txt`).

---

## Installasjon | Installation

### 1. Klon Repositoriet | Clone the Repository
```bash
git clone https://github.com/dittbrukernavn/tolltariff-tool.git
cd tolltariff-tool
```

### 2. Opprett et Virtuelt Miljø | Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts ctivate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer Avhengigheter | Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Kjør Applikasjonen | Run the Application
```bash
python tolltariff_og_avgifter.py
```

---

## Bruk | Usage
1. **Norwegian:** Start skriptet.  
   **English:** Launch the script.
2. **Norwegian:** Skriv inn **Vare ID** (Goods ID) når du blir bedt om det.  
   **English:** Enter **Goods ID** when prompted.
3. **Norwegian:** Verktøyet vil:  
   **English:** The tool will:  
   - **Norwegian:** Navigere tolltariffens hierarki (avsnitt, kapittel, posisjon, underposisjon).  
     **English:** Navigate the tariff hierarchy (section, chapter, position, sub-position).  
   - **Norwegian:** Vise relevante detaljer som beskrivelser og klassifikasjoner.  
     **English:** Display relevant details such as descriptions and classifications.  
   - **Norwegian:** Hente og vise tollavgiften (TOLL) for spesifisert vare under TALL-gruppen.  
     **English:** Fetch and display the duty rate (TOLL) for the specified good under the TALL group.

---

## Eksempel | Example

### Eksempel Inndata | Example Input:
```plaintext
Skriv inn 'vare id' for å søke (eks. 01012902):
```

### Eksempel Utdata | Example Output:
```plaintext
Resultater:
Avsnitt: 01 - Levende dyr; animalske produkter
Kapittel: 01 - Levende dyr
Posisjon: 0101 - Hester, esler, muldyr og mulesler, levende.
  Underposisjon: hester:
  Vare: 01012902 - av vekt under 133 kg

Tollavgift (TALL):
  Sats: 37,61
  Enhet: Per kg
  Gyldig fra: 2015-01-01 til 
```

---

## Lisens | License
**Norwegian:** Dette prosjektet er lisensiert under MIT-lisensen.  
**English:** This project is licensed under the MIT License.

---

## Forfatter | Author
**Norwegian:** **Felix Sandström**  
Spesialist i Data Integrasjon og Automatisering.  
For spørsmål, kontakt meg på [kontakt@felixwebutvikling.no].  

**English:** **Felix Sandström**  
Specialist in Data Integration and Automation.  
For inquiries, contact me at [kontakt@felixwebutvikling.no].
