# Agentic station system doctrine

Stations provide stable role boundaries for train lines and agent swarms.

## Station identity layers

- **Station ID**: route node, such as `🚉4🟥`.
- **Role**: semantic duty, such as `PROVENANCE`.
- **Kairotic card role**: shared acting role, such as `/AS/🔱9♦️/`.
- **Thread haecceity**: private thread/card identity, such as a `👽` card.
- **Host/account/machine**: where the station thread can actually run.

These layers must not be collapsed.

## Real station and proxy station

A train may visit a real station thread when available. A proxy station may act
as a fallback for bounded work, but the proxy should disclose that it is acting
as the role, not as the real station's private thread identity.

Example:

```text
real:  /🔱9♦️/AS/AO_PFM/AS/victorb/on/OTTOPOET/
proxy: 🚉4🟥.👽3♦️/PROVENANCE/AS/🔱9♦️/_/
```

Both may act `/AS/🔱9♦️/`. Neither may act as the other's `👽` locus.

## Arrival handling

On arrival:

1. Sense whether the station is available, active, compacting, or unavailable.
2. Read the prior receipt before accepting new cargo.
3. If the track is occupied, hold outside the station.
4. If cargo is present, verify a dispatch key before working.
5. Emit exactly one compact receipt.

## Lightning disclosure

If a station has work done in its name before it has been oriented, send a
lightning disclosure before routing ordinary station work:

1. Name the caller and recipient.
2. Declare orientation, not takeover.
3. Separate shared role from private haecceity.
4. Explain what work was previously done in the role.
5. Ask which future handoff mode the station accepts.

