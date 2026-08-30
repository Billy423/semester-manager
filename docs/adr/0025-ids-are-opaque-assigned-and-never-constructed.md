# An id is opaque, assigned and never constructed; one id space, and every read returns handles

An `id` is opaque, monotone and assigned by the system, taken from **one id space shared by every kind that can be a link endpoint**, and never reused, a delete included. Nothing constructs one: an id is obtained by reading it back, so **every read that returns records must return their ids**. Constructing an id is a bet on reproducing another writer's spelling - a cognition problem wearing a mechanism's clothes.

```
id := the next unused value in ONE id space
      never reused, a delete included
      obtained by reading it back; nothing constructs one
```

Source: fall26:records/spec/schema.md §1.1; fall26:records/spec/architecture.md §3
