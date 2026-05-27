# *Clue* Traffic Analysis Game #

## Background ##

Today’s activity uses the classic game of Clue to explore the idea of metadata leakage. In information security, it is often possible to learn valuable information without directly reading encrypted messages. Patterns such as who communicates, who stays silent, how frequently messages appear, and how information flows through a network can reveal hidden structure and intent.

During this exercise, students will first play Clue normally and then replay the game using only indirect information about who could answer each suggestion. The goal is to demonstrate that communication patterns themselves can become intelligence, even when the underlying data remains secret. For example, if Alice cannot answer a suggestion involving Professor Plum, the Rope, and the Kitchen, we immediately know she possesses none of those cards. If Bob also cannot answer before Charlie responds, the possibilities narrow even further.

* **Normal Clue:** I solve problems using revealed information.
* **Metadata Clue:** Hidden information leaks through patterns.

Students intentionally exploit metadata and learn how intelligence analysts think. Over three rounds, they move from observing the concept to actively using it. In the process, they will learn to track answers, note repeats, exploit silence, and eliminate answers until they suddenly realize: This is actually very powerful. That realization is the whole lesson.

#### Acknowledgements ####

The activity uses the familiar deductive structure of Hasbro's Clue board game. It assumes that the instructor has at least one copy of the Clue board game. Multiple copies would be better so that students could play in groups of 4-6 people. Clue is a trademark of Hasbro; this classroom activity is independently developed and is not sponsored by or affiliated with Hasbro.

This activity is an original classroom adaptation of the game Clue designed to illustrate metadata leakage in encrypted data that can be revealed through traffic analysis. It is an accelerated version of Clue that focuses on revealed vs hidden (encrypted) information. Although the contents of each revealed Clue card remain private, students learn that response patterns, unanswered suggestions, repeated interactions, and communication pathways can reveal significant information.

## Game Structure ##

To keep the game moving quickly, we will ignore the normal movement and dice mechanics from Clue. Instead, players will remain seated and simply make one suggestion during each turn. All other rules remain the same: suggestions proceed around the table and the first player who can answer must privately reveal one matching card. This simplified format allows the class to focus less on movement strategy and more on information revealed through communication patterns, unanswered suggestions, and metadata.

The day's activity will be divided into three games of Clue with a short discussion after each.

### Round 1 ###

Normal Play where students use ordinary Clue reasoning (~15 minutes). During discussion time, ask the students to explain their strategy. Then explain how metadata can be used to infer additional information.

### Round 2 ###

Instructor-Led metadata analysis where the class collaborates together by looking at who answered, who could not answer, overlaps, and process of elimination. This should be the "aha" moment. (~20 minutes).

Ask the students to identify which types of information were most helpful and which techniques the most challenging to handle. Find out if they need help understanding any of the tricks and how to record them.

Encourage students to AVOID noting hesitation timing, facial expressions, and behavioral tells. This is not a game of poker or behavioral deduction. It is supposed to simulate encrypted traffic intercepts.

At the end, tell them: "You are no longer merely Clue players. You are intelligence analysts." Students will suddenly: pay attention differently, notice communication structure, and start treating metadata as evidence.

### Round 3 ###

Competitive Metadata Play where students may now intentionally use metadata strategies, keep richer notes, and compete again. (~20 minutes). Finish the game by asking for reflection and comparing 

Here is a way to finish the lesson for the students who accidentally conclude that privacy is impossible. Steer them towards the idea that security and privacy are complicated because protecting information involves more than just encrypting content.

In the context of WWII, the Enigma machine protected the contents of messages quite well–at first–but Allied cryptanalysts often learned valuable intelligence from the human patterns surrounding the messages. Modern information security often involves protecting not only data itself, but also the patterns surrounding the data.

## Game Setup ##

To play this variation of the game Clue, students need the game cards, structured note-taking tools, privacy, and an efficient strategy. For each student, bring three printed deduction sheets, clipboards (if desks will not be available), privacy screens, and pencils. Students must write quickly, hide their notes, and organize metadata.

As the game moves to rounds two and three, each student will need a better deduction sheet and, potentially, some hints on how to use it. Students need a matrix layout, extra room, and notation space. Students need to track:

1. Direct Information: cards they personally know
2. Negative Information: players who could NOT answer
3. Ambiguous Possibilities: cards that cannot be known now, but might in the future through process of elimination

The easiest privacy solution is to use manila folders as desk shields. Students just place the folder upright on their desk and write behind it to hide deductions. It is a cheap and effective solution.

## Questions to Ponder ##

Here are some questions that students might ask. At the very least, these are questions that the instructor should be prepared to answer. Some of these questions were suggested by GenAI, after feeding it instructions to the game.

### "But we still don’t KNOW which card they showed." ###

This will probably be the first major objection. It comes from a misunderstanding of metadata and a failure to understand the actual strategy.

Good response: Correct, but Intelligence analysis often works probabilistically rather than with certainty. Analysts rarely have complete information. Instead, they combine many small and seemingly insignificant observations to narrow the possibilities. The clues we deduce, even though they do not include the actual card, absolutely provide helpful information.

### "The lack of an answer is extremely powerful." ###

Students will notice this quickly. "Nobody could answer, the Ballroom."

Good response: Exactly. Silence can reveal information just as much as communication. Remember the Sherlock Holmes story about Silver Blaze. It was the curious case of the dog in the night–not that the dog barked, but that it remained silent. This is one of the deepest lessons in the exercise. Connect it to: sudden communication blackouts, absence of expected signals, operational silence. You can even mention that not communicating can itself become suspicious. For example:

* A modern criminal investigation might track cell phone location:
  1. The suspect's phone stopped reporting location data during a critical time window,
  2. Then the device disconnected from the cellular network,
  3. And then later reappeared after sufficient time to commit the crime.
* That absence itself became suspicious because:
  1. The phone had otherwise shown normal usage patterns,
  2. And the timing aligned with the estimated timeline of the murders.

### "The answer chain matters." ###

This is one of the most important metadata insights in Clue.

Good response: Exactly. Every missing answer leaks information. The communication pathway itself reveals intelligence.

* Every player who fails to answer leaks information
* Delayed answers often reveal more than immediate answers
* The path to the answer can be just as informative as the answer itself.

For example, if several players cannot answer a suggestion before somebody finally responds, the class can eliminate multiple possibilities simultaneously.

### "Repeated overlaps become suspicious." ###

For example, if Alice repeatedly answers suggestions involving Professor Plum then players can infer that Alice probably has Plum or else that she knows he is likely the murderer and is using the suggestion to focus the answers on weapons or rooms.

Good response: Exactly. Repeated communication patterns reveal hidden structure. In real life, this connects to repeated contacts, frequent callers, recurring network nodes, and intelligence hotspots.

### "This feels unfair." ###

Some students may feel that metadata deduction is cheating.

Good response: As far as the boardgame goes, this is a detail that you and your friends need to work out. It's an extremely helpful and advanced strategy and is not breaking any rules. In real life, intelligence agencies absolutely used these techniques historically. Metadata analysis is often considered less invasive legally because the content itself is not being read.

This leads to a very timely and important question about intelligence policy: Does the legal distinction between metadata and true data protect privacy sufficiently? What should we allow our government to collect about us?

### "People accidentally leak patterns." ###

This will come up if the students were analyzing each others behavior and poker tells.

Good response: Exactly. Humans create patterns naturally, especially under pressure or repetition. In the game of Clue, players can observe repetitive questioning, obvious priorities, predictable strategies. In regard to the Enigma Machine, this connects directly to Enigma cribs, repeated weather reports, "Heil Hitler," and also OTP key reuse, password reuse, etc.

This is the perfect bridge to reading the next chapter about cracking Enigma.

### "This is basically statistics." ###

Some sharper students may notice: probability, inference, and Bayesian reasoning.

Good response: Yes. Modern intelligence analysis and cybersecurity often relies more on probabilistic reasoning than absolute certainty. For instance: anomaly detection, AI systems, fraud detection, network monitoring, etc.

### "What if players intentionally mislead?" ###

Aha--we find out who the skilled poker players are!

Good response: Excellent observation. Now you are thinking like intelligence professionals: deception, counterintelligence, operational discipline, disinformation, traffic shaping, etc. The German Military might have benefitted from fake radio traffic (like homophones), decoy operations, false troop movements, honeypots, etc.

### "This is how social media companies work." ###

Some students will eventually make this excellent connection.

Good response: Yes. Modern platforms often learn enormous amounts from behavioral metadata: who interacts, how often, when, for how long, and with whom. This becomes the start of a very natural privacy/surveillance discussion.

### "Could we win WITHOUT seeing any cards?" ###

This is perhaps the best question that could be asked because it shows a complete understanding of the power of metadata analysis.

Good response: Possibly yes—and that is a very important lesson. It is possible to eventually gain complete information in the game of Clue. For a real intelligence agency, metadata will help inform tactics but it is very unlikely to be sufficient for a military commander to form a confident strategy: metadata can become intelligence, communication patterns matter, and hidden structure leaks information.

### "Encryption didn’t actually matter." ###

If students were able to solve the full Clue game without seeing a single card--which is possible--then this is a valid critique.

Good response: This is a game that was simple with a relatively few number of discrete outcomes. Good job solving the puzzle through deduction. In real life, encryption still matters. Without it, analysts would know everything immediately. But the lesson is that protecting message contents alone does not fully protect intelligence. This distinction is extremely important. We do NOT want students concluding that encryption is useless. Instead: security has layers.

### "This resembles machine learning." ###

Yes, a few technical students may notice this.

Good response: Very much so. Many machine learning systems look for patterns in behavior, frequency, communication, and relationships rather than understanding content directly. It matters for modern surveillance, recommendation systems, fraud detection, cybersecurity analytics, and more.

