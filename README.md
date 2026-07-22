# STATION-OF/station-of

Class definition and SDK layer for `STATION-OF/*` repositories.

`STATION-OF/*` repos describe station roles: what a station is responsible for,
what it must preserve, how it receives train arrivals, how it writes receipts,
and how it participates in direct cross-thread/cross-machine lightning handoffs.

## Why this exists

Live train dogfooding showed that station identity can be shared without merging
thread haecceities. Two different agent threads can act `/AS/🔱9♦️/` as one
kairotic role, while neither is permitted to act as the other's private `👽`
thread/card identity.

This repo defines that boundary for future station repos.

## Core doctrine

1. **A station is a role, not necessarily one thread.**
2. **A station may have a primary thread and fallback/proxy threads.**
3. **Station arrivals should be thin.** The station reads doctrine and routed
   work from shared truth.
4. **Receipts are station output, not ambient chatter.**
5. **Shared role does not authorize haecceity impersonation.**

## Suggested repo shape

```text
README.md
doctrine/
  station-system.md
schemas/
  station-definition.schema.json
examples/
  provenance.station.json
```

## Receipt minimum

A station receipt should say:

- station identity and acting thread/card identity;
- input/event consumed;
- concrete evidence checked;
- one outcome;
- next handoff or blocker;
- whether any mutation occurred.

