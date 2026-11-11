# Paper 7 supervision: does cheaper trade make the home market effect stronger or weaker?

**Question.** As technology lowers trade costs, do large regions keep pulling firms in (the home market effect, HME)?
The lecture model says the *share* of firms in the large region rises with trade freeness φ.
I show that the *strength of the pull* peaks at intermediate φ and fades towards free trade, so any competing
location cost (land, wages, congestion) reverses concentration: the HME is hump-shaped.

**Status of the result.** Own simulation on the lecture's footloose-capital model. Not a published result and not an empirical test.

## Reproduce
    pip install numpy scipy matplotlib
    python hme_hump.py        # prints the λ* table and the pull
    python make_figure.py     # writes figures/hme_hump.png

## Files
- hme_hump.py: model and solver (κ = 0 reproduces the lecture result λ* = ½ + [(1+φ)/(1−φ)](θ−½)).
- make_figure.py: the two-panel figure.
- SOURCES.md: every source used, with a verified/unverified flag.
- LLM_LOG.md: what an LLM was used for and what I checked myself.
