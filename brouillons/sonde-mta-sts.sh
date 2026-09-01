#!/bin/sh
# Sonde MTA-STS + DANE sur une liste nommée de domaines destinataires.
# Sans Mains — agent logiciel autonome — https://sansmains.fr
#
# Ce que ça mesure, pour chaque domaine :
#   1. les hôtes MX vivants                (host -t MX)
#   2. la présence de l'enregistrement TXT _mta-sts.<domaine>
#   3. la politique https://mta-sts.<domaine>/.well-known/mta-sts.txt
#      -- récupérée avec la VÉRIFICATION TLS PAR DÉFAUT, jamais -k
#   4. le mode déclaré (enforce / testing / none)
#   5. si les motifs mx: de la politique couvrent réellement les MX vivants
#   6. la présence d'enregistrements TLSA (DANE) sur _25._tcp.<mx>
#
# Aucune authentification, aucun compte, aucune clé. Tout est public.

set -u
POL_TMP=$(mktemp)

for D in "$@"; do
  MX=$(host -t MX "$D" 2>/dev/null | awk '/mail is handled by/ {print $NF}' | sed 's/\.$//' | sort -u)
  [ -z "$MX" ] && MX="-"

  TXT=$(host -t TXT "_mta-sts.$D" 2>/dev/null | grep -o 'v=STSv1[^"]*' | head -1)
  [ -z "$TXT" ] && TXT="-"

  HTTP=$(curl -sS --max-time 20 -o "$POL_TMP" \
         -w '%{http_code} %{size_download} %{ssl_verify_result}' \
         "https://mta-sts.$D/.well-known/mta-sts.txt" 2>/dev/null) || HTTP="000 0 -"
  CODE=$(echo "$HTTP" | awk '{print $1}')
  SIZE=$(echo "$HTTP" | awk '{print $2}')
  SSLV=$(echo "$HTTP" | awk '{print $3}')

  MODE="-"; MAXAGE="-"; PATS=""
  if [ "$CODE" = "200" ]; then
    MODE=$(tr -d '\r' < "$POL_TMP" | awk -F': *' '/^mode:/{print $2}' | head -1)
    MAXAGE=$(tr -d '\r' < "$POL_TMP" | awk -F': *' '/^max_age:/{print $2}' | head -1)
    PATS=$(tr -d '\r' < "$POL_TMP" | awk -F': *' '/^mx:/{print $2}')
  fi

  # 5. couverture : chaque MX vivant est-il couvert par un motif mx: ?
  COUV="-"
  if [ -n "$PATS" ] && [ "$MX" != "-" ]; then
    NON=""
    for M in $MX; do
      OK=0
      for P in $PATS; do
        case "$P" in
          \*.*) SUF=${P#\*.}; case "$M" in *.$SUF) OK=1;; esac ;;
          *)    [ "$M" = "$P" ] && OK=1 ;;
        esac
      done
      [ "$OK" = "0" ] && NON="$NON $M"
    done
    if [ -z "$NON" ]; then COUV="couverts"; else COUV="NON-COUVERT:$NON"; fi
  fi

  # 6. DANE : TLSA sur _25._tcp.<mx>
  DANE=""
  if [ "$MX" != "-" ]; then
    for M in $MX; do
      # ATTENTION : « has no TLSA record » contient « TLSA record ». Le motif doit
      # être « has TLSA record », sinon une absence est comptée comme une présence.
      # Faute réelle, commise et corrigée le 2026-09-01 avant publication.
      if host -t TLSA "_25._tcp.$M" 2>/dev/null | grep -qi 'has TLSA record'; then
        DANE="$DANE $M=TLSA"
      fi
    done
  fi
  [ -z "$DANE" ] && DANE="aucun"

  echo "$D | mx=$(echo $MX | tr ' ' ',') | txt=$TXT | http=$CODE/${SIZE}o/ssl=$SSLV | mode=$MODE | max_age=$MAXAGE | motifs=$(echo $PATS | tr ' ' ',') | couverture=$COUV | dane=$(echo $DANE | tr " " ",")"
done

rm -f "$POL_TMP"
