def getTopics():
    return """Electron Transport Chain (ETC) in Type I vs. Type II fibers
– Overlay mitochondrial density and O₂ usage; visualize Complex I–IV.
|
NAD⁺/NADH ratios during aerobic vs. anaerobic glycolysis
– Lactate accumulation shifts NADH:NAD⁺ — perfect for a metabolic bottleneck graphic.
|
mTORC1 activation: PI3K → AKT → TSC2 → Rheb pathway
– Full growth signaling cascade triggered by resistance training and amino acids.
|
AMPK activation under caloric deficit
– Shows catabolic signaling suppressing MPS, promoting autophagy.
|
Myonuclear domain theory
– Cell size increase is limited by nuclei count → satellite cells must donate more.
|
Hormone-receptor binding kinetics: Testosterone vs. Cortisol
– Affinity, saturation, half-life comparisons, receptor downregulation under chronic load.
|
Mitochondrial biogenesis: PGC-1α signaling cascade
– Endurance-induced transcription factors that expand mitochondrial content.
|
Leucine’s direct binding to Sestrin2 → mTOR activation
– The exact point where nutrition meets intracellular signal.
|
Glut4 translocation in muscle from insulin and contraction stimuli
– Why lifting boosts glucose uptake independent of insulin.
|
Progressive Overload
– How to increase volume (weight, reps, sets) over time to build muscle.
|
Training to Failure vs. RIR (Reps in Reserve)
– Visual showing muscle activation at different RIR levels.
|
Hypertrophy Rep Ranges
– 6–12 reps sweet spot, plus why 5s and 20s can also work if close to failure.
|
Rest Time Between Sets
– 30–60 sec for hypertrophy, 2–5 min for strength — explained with a bar chart.
|
Compound vs. Isolation Exercises
– Venn diagram showing muscles hit, carryover, and use cases.
|
Training Splits: Push/Pull/Legs vs. Full Body vs. Bro Split
– Pros/cons visual or weekly planner format.
|
DOMS ≠ Muscle Growth
– Visual myth-buster: soreness doesn't mean effective training.
""".split("|")


def getPrompt(subject, clipLengthMinutes):
    prompt = "Make a short conversation between Peter Griffin and Stevie Griffin from Family Guy discussing an intricate nerdy fitness conversation that will be mass appealing and interesting to those with little to moderate knowledge of fitness. Make sure you dive into chemistry, biology, and appeal to topics that often have misconceptions. Make it a back and forth dialogue that lasts about " + clipLengthMinutes + " minute. Make sure it is extremely nerdy and very in depth and science based. It should discuss " + subject + (
        ". The format should be an array of json objects with the following format:\n\n"
        "[{\"character\": \"Peter\", \"text\": \"<text>\"}, {\"character\": \"Stewie\", \"text\": \"<text>\"}, {\"character\": \"Peter\", \"text\": \"<text>\"}]\n\n")
    return prompt
