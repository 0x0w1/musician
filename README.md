# musician

Two Claude Code skills for producing music with [Suno](https://suno.com) — one for songs with lyrics, one for instrumentals.

Give either skill a single line. Get back a prompt set you can paste into Suno without editing, and a record of every decision so you can change one thing later without losing the rest.

```
실패했지만 다시 시작하려는 마음을 노래하고 싶어.
밤에 혼자 코딩하면서 들을 음악을 만들고 싶어.
```

## Install

```bash
claude plugins marketplace add /path/to/musician
claude plugins install suno-music-skills@musician
```

Or from inside a session:

```
/plugin marketplace add /path/to/musician
/plugin install suno-music-skills@musician
```

On first run the skills create `~/.claude/suno/profile.md` and ask for the two things they cannot infer: your Suno plan and your default lyric language.

## The two skills

| Skill | Handles | Produces |
|---|---|---|
| `suno-vocal-song` | Anything with text to be sung | Title, Lyrics, Styles, Exclude Styles, Voice Gender, sliders |
| `suno-instrumental` | Anything without | Title, structure tags, Styles, Exclude Styles, Instrumental toggle, sliders |

The boundary is **"is there text to be sung?"** — nothing else. Structure tags aren't sung, so an instrumental using `[Build-Up]` stays on the instrumental side. Ask the wrong skill and it hands you to the other one rather than redesigning your request.

## How it works

- **Slots, not free writing.** Styles is assembled from seven ordered slots. Suno weights earlier terms more heavily, so the order is fixed rather than left to chance — and because slots are addressable, `make it female vocal` changes two of them and leaves the rest byte-identical.
- **Non-redundancy over word count.** The constraint is that no two descriptors say the same thing. Specific instrument and production detail is kept; synonym piles are collapsed.
- **Three fields, three jobs.** Lyrics is what gets performed. Styles is the music you want. Exclude Styles is the music you don't. Production direction never enters the lyrics box.
- **Version dialects.** v4.5, v5, and v5.5 have identical fields and limits but listen differently, so the same slots render in different prose depending on your profile.
- **Revisions test for contradiction, not improvement.** A change spreads only where leaving it would make the prompt contradict itself. "Would be better" is unbounded and turns every tweak into a redesign.
- **Artist names never reach output.** They're blocked by Suno and risk account strikes, so references are decomposed into era, genre, texture, instrumentation, and vocal character — and the translation is shown to you in one line so you can correct it before generating.

## Layout

```
skills/
├── _shared/
│   ├── suno-reference.md      facts — fields, limits, tags, each tagged with verification status
│   ├── compiler-rules.md      rules — slots, budget, exclusions, sliders, guardrails, revisions
│   └── profile.template.md    taste — the one file you swap when handing this to someone else
├── suno-vocal-song/
└── suno-instrumental/
```

Everything except `profile.template.md` is neutral. Personal taste lives in the profile, which is why this is shareable as-is.

State lives outside the plugin, in `~/.claude/suno/` — the plugin directory is a versioned cache and gets replaced on update.

## Testing

Test inputs and a nine-point evaluation checklist are in [TESTING.md](TESTING.md).

## Status

v0.1.0. Two behaviors are owner-confirmed but not independently verified — see `skills/_shared/suno-reference.md` §10.

## License

Apache-2.0
