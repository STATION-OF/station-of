# Station arrival depths

Station registration answers **where** a station can receive work. Arrival
depth answers **how much** work the station should do during one visit. A train
must not treat a successful transport ACK as proof that the station completed
its inspection.

## 🟧 Express arrival

The orange line is a bounded health visit:

1. verify the station identity and registration revision;
2. verify endpoint reachability and one current health signal;
3. record a compact receipt with `status`, `observed_at`, and `next_action`;
4. do not expand foreign cargo, recursively inspect related repositories, or
   mutate station state.

An express receipt may say `healthy`, `degraded`, `blocked`, or `stale`. It is
an orientation signal, not a completeness claim.

## 🟦 Deep arrival

The blue line is a bounded survey visit:

1. perform the express checks;
2. inspect the station's canonical record and referenced foreign-repository
   keys;
3. validate relevant schema versions, cross-references, provenance, and
   branch/revision evidence;
4. run the station's focused checks with explicit time and payload bounds;
5. return `evidence`, `missing`, `contradictions`, and `next_action` in the
   receipt.

Deep work may propose a repair or create a focused branch, but it must not
silently rewrite the station's canonical registration. Promotion remains a
separate authorized action.

## Interoperability rule

Arrival depth belongs to the train's route loadout, not to the station's
identity. The same station can receive an orange express arrival and a blue
deep arrival without changing its registration or endpoint. Station receipts
must state which depth produced them.
