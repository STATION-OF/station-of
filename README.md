# STATION-OF

This repository owns canonical station registration records. A train may pin a
record revision, but cannot author or silently repair a station's endpoint.

`schemas/station-registration.schema.json` defines the v1 registration
contract. An endpoint is eligible for a conductor-run arrival only when its
record is `application-ack-verified`; station-controlled mode remains explicit
for a registered station that cannot receive conductor arrivals.

