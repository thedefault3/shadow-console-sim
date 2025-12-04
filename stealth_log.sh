#!/usr/bin/env bash
# stealth_log_generator.sh — harmless, generates a weird-looking log file locally.
# Usage: ./stealth_log_generator.sh
LOGFILE="weird.log"
echo "[`date --rfc-3339=seconds`] <init> shadow-console-sim starting..." > "$LOGFILE"
COUNT=0
while true; do
  TIMESTAMP=$(date --rfc-3339=seconds)
  RND=$((RANDOM%1000))
  case $((RANDOM%5)) in
    0) TYPE="AUTH"; MSG="token rotated";;
    1) TYPE="NET"; MSG="interface ghosted";;
    2) TYPE="FS"; MSG="inode anomaly detected";;
    3) TYPE="AI"; MSG="entropy drift";;
    4) TYPE="SYS"; MSG="checkpoint saved";;
  esac
  printf "[%s] <%s> %s #%d\n" "$TIMESTAMP" "$TYPE" "$MSG" "$RND" >> "$LOGFILE"
  # print a short live line every few seconds to terminal
  if (( COUNT % 7 == 0 )); then
    tail -n 6 "$LOGFILE" | sed -n '1,6p'
  fi
  sleep $((1 + RANDOM % 3))
  COUNT=$((COUNT+1))
done
